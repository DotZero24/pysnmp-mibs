_J='netSnmpPassIndex'
_I='NET-SNMP-PASS-MIB'
_H='TimeTicks'
_G='IpAddress'
_F='Integer32'
_E='Gauge32'
_D='SnmpAdminString'
_C='ObjectIdentifier'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString',_C)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netSnmpExamples,=mibBuilder.importSymbols('NET-SNMP-EXAMPLES-MIB','netSnmpExamples')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_E,_F,_G,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netSnmpPassExamples=ModuleIdentity((1,3,6,1,4,1,8072,2,255))
class _NetSnmpPassString_Type(SnmpAdminString):defaultValue=OctetString('Life, the Universe, and Everything')
_NetSnmpPassString_Type.__name__=_D
_NetSnmpPassString_Object=MibScalar
netSnmpPassString=_NetSnmpPassString_Object((1,3,6,1,4,1,8072,2,255,1),_NetSnmpPassString_Type())
netSnmpPassString.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpPassString.setStatus(_A)
_NetSnmpPassTable_Object=MibTable
netSnmpPassTable=_NetSnmpPassTable_Object((1,3,6,1,4,1,8072,2,255,2))
if mibBuilder.loadTexts:netSnmpPassTable.setStatus(_A)
_NetSnmpPassEntry_Object=MibTableRow
netSnmpPassEntry=_NetSnmpPassEntry_Object((1,3,6,1,4,1,8072,2,255,2,1))
netSnmpPassEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:netSnmpPassEntry.setStatus(_A)
_NetSnmpPassIndex_Type=Integer32
_NetSnmpPassIndex_Object=MibTableColumn
netSnmpPassIndex=_NetSnmpPassIndex_Object((1,3,6,1,4,1,8072,2,255,2,1,1),_NetSnmpPassIndex_Type())
netSnmpPassIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:netSnmpPassIndex.setStatus(_A)
class _NetSnmpPassInteger_Type(Integer32):defaultValue=42
_NetSnmpPassInteger_Type.__name__=_F
_NetSnmpPassInteger_Object=MibTableColumn
netSnmpPassInteger=_NetSnmpPassInteger_Object((1,3,6,1,4,1,8072,2,255,2,1,2),_NetSnmpPassInteger_Type())
netSnmpPassInteger.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpPassInteger.setStatus(_A)
class _NetSnmpPassOID_Type(ObjectIdentifier):defaultValue=1,3,6,1,4,1,8072,2,255,99
_NetSnmpPassOID_Type.__name__=_C
_NetSnmpPassOID_Object=MibTableColumn
netSnmpPassOID=_NetSnmpPassOID_Object((1,3,6,1,4,1,8072,2,255,2,1,3),_NetSnmpPassOID_Type())
netSnmpPassOID.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpPassOID.setStatus(_A)
class _NetSnmpPassTimeTicks_Type(TimeTicks):defaultValue=363136200
_NetSnmpPassTimeTicks_Type.__name__=_H
_NetSnmpPassTimeTicks_Object=MibScalar
netSnmpPassTimeTicks=_NetSnmpPassTimeTicks_Object((1,3,6,1,4,1,8072,2,255,3),_NetSnmpPassTimeTicks_Type())
netSnmpPassTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpPassTimeTicks.setStatus(_A)
class _NetSnmpPassIpAddress_Type(IpAddress):defaultHexValue='7f000001'
_NetSnmpPassIpAddress_Type.__name__=_G
_NetSnmpPassIpAddress_Object=MibScalar
netSnmpPassIpAddress=_NetSnmpPassIpAddress_Object((1,3,6,1,4,1,8072,2,255,4),_NetSnmpPassIpAddress_Type())
netSnmpPassIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpPassIpAddress.setStatus(_A)
_NetSnmpPassCounter_Type=Counter32
_NetSnmpPassCounter_Object=MibScalar
netSnmpPassCounter=_NetSnmpPassCounter_Object((1,3,6,1,4,1,8072,2,255,5),_NetSnmpPassCounter_Type())
netSnmpPassCounter.setMaxAccess('read-only')
if mibBuilder.loadTexts:netSnmpPassCounter.setStatus(_A)
class _NetSnmpPassGauge_Type(Gauge32):defaultValue=42
_NetSnmpPassGauge_Type.__name__=_E
_NetSnmpPassGauge_Object=MibScalar
netSnmpPassGauge=_NetSnmpPassGauge_Object((1,3,6,1,4,1,8072,2,255,6),_NetSnmpPassGauge_Type())
netSnmpPassGauge.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpPassGauge.setStatus(_A)
_NetSnmpPassOIDValue_ObjectIdentity=ObjectIdentity
netSnmpPassOIDValue=_NetSnmpPassOIDValue_ObjectIdentity((1,3,6,1,4,1,8072,2,255,99))
mibBuilder.exportSymbols(_I,**{'netSnmpPassExamples':netSnmpPassExamples,'netSnmpPassString':netSnmpPassString,'netSnmpPassTable':netSnmpPassTable,'netSnmpPassEntry':netSnmpPassEntry,_J:netSnmpPassIndex,'netSnmpPassInteger':netSnmpPassInteger,'netSnmpPassOID':netSnmpPassOID,'netSnmpPassTimeTicks':netSnmpPassTimeTicks,'netSnmpPassIpAddress':netSnmpPassIpAddress,'netSnmpPassCounter':netSnmpPassCounter,'netSnmpPassGauge':netSnmpPassGauge,'netSnmpPassOIDValue':netSnmpPassOIDValue})