_E='zxDslRadiusClientAuthSvrIndex'
_D='ZET-DSL-RADIUS-MIB'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
zxDslRadiusMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,34))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxDsl_ObjectIdentity=ObjectIdentity
zxDsl=_ZxDsl_ObjectIdentity((1,3,6,1,4,1,3902,1004))
_ZxDslRadiusClient_ObjectIdentity=ObjectIdentity
zxDslRadiusClient=_ZxDslRadiusClient_ObjectIdentity((1,3,6,1,4,1,3902,1004,34,1))
_ZxDslRadiusClientAuthSvrTable_Object=MibTable
zxDslRadiusClientAuthSvrTable=_ZxDslRadiusClientAuthSvrTable_Object((1,3,6,1,4,1,3902,1004,34,1,1))
if mibBuilder.loadTexts:zxDslRadiusClientAuthSvrTable.setStatus(_A)
_ZxDslRadiusClientAuthSvrEntry_Object=MibTableRow
zxDslRadiusClientAuthSvrEntry=_ZxDslRadiusClientAuthSvrEntry_Object((1,3,6,1,4,1,3902,1004,34,1,1,1))
zxDslRadiusClientAuthSvrEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxDslRadiusClientAuthSvrEntry.setStatus(_A)
_ZxDslRadiusClientAuthSvrIndex_Type=Integer32
_ZxDslRadiusClientAuthSvrIndex_Object=MibTableColumn
zxDslRadiusClientAuthSvrIndex=_ZxDslRadiusClientAuthSvrIndex_Object((1,3,6,1,4,1,3902,1004,34,1,1,1,1),_ZxDslRadiusClientAuthSvrIndex_Type())
zxDslRadiusClientAuthSvrIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxDslRadiusClientAuthSvrIndex.setStatus(_A)
_ZxDslRadiusClientAuthAddress_Type=IpAddress
_ZxDslRadiusClientAuthAddress_Object=MibTableColumn
zxDslRadiusClientAuthAddress=_ZxDslRadiusClientAuthAddress_Object((1,3,6,1,4,1,3902,1004,34,1,1,1,2),_ZxDslRadiusClientAuthAddress_Type())
zxDslRadiusClientAuthAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslRadiusClientAuthAddress.setStatus(_A)
_ZxDslRadiusClientAuthPortNumber_Type=Integer32
_ZxDslRadiusClientAuthPortNumber_Object=MibTableColumn
zxDslRadiusClientAuthPortNumber=_ZxDslRadiusClientAuthPortNumber_Object((1,3,6,1,4,1,3902,1004,34,1,1,1,3),_ZxDslRadiusClientAuthPortNumber_Type())
zxDslRadiusClientAuthPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslRadiusClientAuthPortNumber.setStatus(_A)
class _ZxDslRadiusClientAuthSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxDslRadiusClientAuthSecret_Type.__name__=_C
_ZxDslRadiusClientAuthSecret_Object=MibTableColumn
zxDslRadiusClientAuthSecret=_ZxDslRadiusClientAuthSecret_Object((1,3,6,1,4,1,3902,1004,34,1,1,1,4),_ZxDslRadiusClientAuthSecret_Type())
zxDslRadiusClientAuthSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslRadiusClientAuthSecret.setStatus(_A)
_ZxDslRadiusClientAuthRowStatus_Type=RowStatus
_ZxDslRadiusClientAuthRowStatus_Object=MibTableColumn
zxDslRadiusClientAuthRowStatus=_ZxDslRadiusClientAuthRowStatus_Object((1,3,6,1,4,1,3902,1004,34,1,1,1,5),_ZxDslRadiusClientAuthRowStatus_Type())
zxDslRadiusClientAuthRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslRadiusClientAuthRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zte':zte,'zxDsl':zxDsl,'zxDslRadiusMib':zxDslRadiusMib,'zxDslRadiusClient':zxDslRadiusClient,'zxDslRadiusClientAuthSvrTable':zxDslRadiusClientAuthSvrTable,'zxDslRadiusClientAuthSvrEntry':zxDslRadiusClientAuthSvrEntry,_E:zxDslRadiusClientAuthSvrIndex,'zxDslRadiusClientAuthAddress':zxDslRadiusClientAuthAddress,'zxDslRadiusClientAuthPortNumber':zxDslRadiusClientAuthPortNumber,'zxDslRadiusClientAuthSecret':zxDslRadiusClientAuthSecret,'zxDslRadiusClientAuthRowStatus':zxDslRadiusClientAuthRowStatus})