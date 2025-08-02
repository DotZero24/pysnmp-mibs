_D='Integer32'
_C='current'
_B='read-write'
_A='Unsigned32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtBase,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtBase')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snmpMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,1,2))
if mibBuilder.loadTexts:snmpMgmt.setRevisions(('2007-02-05 00:00','2006-10-05 00:00','2003-04-29 00:00'))
class _SnmpUdpPort_Type(Unsigned32):defaultValue=161;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpUdpPort_Type.__name__=_A
_SnmpUdpPort_Object=MibScalar
snmpUdpPort=_SnmpUdpPort_Object((1,3,6,1,4,1,4413,2,2,2,1,1,2,1),_SnmpUdpPort_Type())
snmpUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpUdpPort.setStatus(_C)
class _SnmpNotifyUdpPort_Type(Unsigned32):defaultValue=162;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpNotifyUdpPort_Type.__name__=_A
_SnmpNotifyUdpPort_Object=MibScalar
snmpNotifyUdpPort=_SnmpNotifyUdpPort_Object((1,3,6,1,4,1,4413,2,2,2,1,1,2,2),_SnmpNotifyUdpPort_Type())
snmpNotifyUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpNotifyUdpPort.setStatus(_C)
class _SnmpDscpTag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SnmpDscpTag_Type.__name__=_D
_SnmpDscpTag_Object=MibScalar
snmpDscpTag=_SnmpDscpTag_Object((1,3,6,1,4,1,4413,2,2,2,1,1,2,3),_SnmpDscpTag_Type())
snmpDscpTag.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpDscpTag.setStatus(_C)
mibBuilder.exportSymbols('BRCM-SNMP-MGMT-MIB',**{'snmpMgmt':snmpMgmt,'snmpUdpPort':snmpUdpPort,'snmpNotifyUdpPort':snmpNotifyUdpPort,'snmpDscpTag':snmpDscpTag})