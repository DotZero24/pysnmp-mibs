_I='pingSrcAddress-ces'
_H='pingPacketSize-ces'
_G='pingRepetitions-ces'
_F='pingAddress-ces'
_E='Integer32'
_D='not-accessible'
_C='CONTIVITY-INFO-V1-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
contivity,=mibBuilder.importSymbols('NEWOAK-MIB','contivity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snmpAgentInfo_ces=ModuleIdentity((1,3,6,1,4,1,2505,1,15))
if mibBuilder.loadTexts:snmpAgentInfo_ces.setRevisions(('1900-08-07 22:30',))
_SnmpAgentInfo_Utilities_ces_ObjectIdentity=ObjectIdentity
snmpAgentInfo_Utilities_ces=_SnmpAgentInfo_Utilities_ces_ObjectIdentity((1,3,6,1,4,1,2505,1,15,1))
_SnmpAgentInfo_Utilities_Ping_ces_ObjectIdentity=ObjectIdentity
snmpAgentInfo_Utilities_Ping_ces=_SnmpAgentInfo_Utilities_Ping_ces_ObjectIdentity((1,3,6,1,4,1,2505,1,15,1,1))
_SnmpAgentInfo_Utilities_RevDate_ces_Type=DisplayString
_SnmpAgentInfo_Utilities_RevDate_ces_Object=MibScalar
snmpAgentInfo_Utilities_RevDate_ces=_SnmpAgentInfo_Utilities_RevDate_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,1),_SnmpAgentInfo_Utilities_RevDate_ces_Type())
snmpAgentInfo_Utilities_RevDate_ces.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAgentInfo_Utilities_RevDate_ces.setStatus(_A)
_SnmpAgentInfo_Utilities_Rev_ces_Type=Integer32
_SnmpAgentInfo_Utilities_Rev_ces_Object=MibScalar
snmpAgentInfo_Utilities_Rev_ces=_SnmpAgentInfo_Utilities_Rev_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,2),_SnmpAgentInfo_Utilities_Rev_ces_Type())
snmpAgentInfo_Utilities_Rev_ces.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAgentInfo_Utilities_Rev_ces.setStatus(_A)
_SnmpAgentInfo_Utilities_ServerRev_ces_Type=DisplayString
_SnmpAgentInfo_Utilities_ServerRev_ces_Object=MibScalar
snmpAgentInfo_Utilities_ServerRev_ces=_SnmpAgentInfo_Utilities_ServerRev_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,3),_SnmpAgentInfo_Utilities_ServerRev_ces_Type())
snmpAgentInfo_Utilities_ServerRev_ces.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAgentInfo_Utilities_ServerRev_ces.setStatus(_A)
_PingAddress_ces_Type=IpAddress
_PingAddress_ces_Object=MibScalar
pingAddress_ces=_PingAddress_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,4),_PingAddress_ces_Type())
pingAddress_ces.setMaxAccess(_D)
if mibBuilder.loadTexts:pingAddress_ces.setStatus(_A)
class _PingRepetitions_ces_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PingRepetitions_ces_Type.__name__=_E
_PingRepetitions_ces_Object=MibScalar
pingRepetitions_ces=_PingRepetitions_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,5),_PingRepetitions_ces_Type())
pingRepetitions_ces.setMaxAccess(_D)
if mibBuilder.loadTexts:pingRepetitions_ces.setStatus(_A)
class _PingPacketSize_ces_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,4076))
_PingPacketSize_ces_Type.__name__=_E
_PingPacketSize_ces_Object=MibScalar
pingPacketSize_ces=_PingPacketSize_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,6),_PingPacketSize_ces_Type())
pingPacketSize_ces.setMaxAccess(_D)
if mibBuilder.loadTexts:pingPacketSize_ces.setStatus(_A)
_PingSrcAddress_ces_Type=IpAddress
_PingSrcAddress_ces_Object=MibScalar
pingSrcAddress_ces=_PingSrcAddress_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,7),_PingSrcAddress_ces_Type())
pingSrcAddress_ces.setMaxAccess(_D)
if mibBuilder.loadTexts:pingSrcAddress_ces.setStatus(_A)
_PingTable_ces_Object=MibTable
pingTable_ces=_PingTable_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,8))
if mibBuilder.loadTexts:pingTable_ces.setStatus(_A)
_PingEntry_ces_Object=MibTableRow
pingEntry_ces=_PingEntry_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,8,1))
pingEntry_ces.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:pingEntry_ces.setStatus(_A)
_PingAverageTime_ces_Type=Integer32
_PingAverageTime_ces_Object=MibTableColumn
pingAverageTime_ces=_PingAverageTime_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,8,1,1),_PingAverageTime_ces_Type())
pingAverageTime_ces.setMaxAccess(_B)
if mibBuilder.loadTexts:pingAverageTime_ces.setStatus(_A)
_PingPercentLoss_ces_Type=Integer32
_PingPercentLoss_ces_Object=MibTableColumn
pingPercentLoss_ces=_PingPercentLoss_ces_Object((1,3,6,1,4,1,2505,1,15,1,1,8,1,2),_PingPercentLoss_ces_Type())
pingPercentLoss_ces.setMaxAccess(_B)
if mibBuilder.loadTexts:pingPercentLoss_ces.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'snmpAgentInfo-ces':snmpAgentInfo_ces,'snmpAgentInfo-Utilities-ces':snmpAgentInfo_Utilities_ces,'snmpAgentInfo-Utilities-Ping-ces':snmpAgentInfo_Utilities_Ping_ces,'snmpAgentInfo-Utilities-RevDate-ces':snmpAgentInfo_Utilities_RevDate_ces,'snmpAgentInfo-Utilities-Rev-ces':snmpAgentInfo_Utilities_Rev_ces,'snmpAgentInfo-Utilities-ServerRev-ces':snmpAgentInfo_Utilities_ServerRev_ces,_F:pingAddress_ces,_G:pingRepetitions_ces,_H:pingPacketSize_ces,_I:pingSrcAddress_ces,'pingTable-ces':pingTable_ces,'pingEntry-ces':pingEntry_ces,'pingAverageTime-ces':pingAverageTime_ces,'pingPercentLoss-ces':pingPercentLoss_ces})