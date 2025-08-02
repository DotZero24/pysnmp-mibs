_I='Integer32'
_H='InetAddressType'
_G='InetAddress'
_F='pingCtlTestName'
_E='pingCtlOwnerIndex'
_D='DISMAN-PING-MIB'
_C='milliseconds'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pingCtlOwnerIndex,pingCtlTestName=mibBuilder.importSymbols(_D,_E,_F)
fsRouterQoSMIB,=mibBuilder.importSymbols('FS-ROUTER-QOS-MIB','fsRouterQoSMIB')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_H)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsIpSlaMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,5))
if mibBuilder.loadTexts:fsIpSlaMIB.setRevisions(('2014-09-12 00:00',))
_FsIpSlaMIBObjects_ObjectIdentity=ObjectIdentity
fsIpSlaMIBObjects=_FsIpSlaMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,106,5,1))
_FsIpSlaResultsTable_Object=MibTable
fsIpSlaResultsTable=_FsIpSlaResultsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1))
if mibBuilder.loadTexts:fsIpSlaResultsTable.setStatus(_A)
_FsIpSlaResultsEntry_Object=MibTableRow
fsIpSlaResultsEntry=_FsIpSlaResultsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1))
fsIpSlaResultsEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:fsIpSlaResultsEntry.setStatus(_A)
class _FsIpSlaResultsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('completed',3)))
_FsIpSlaResultsOperStatus_Type.__name__=_I
_FsIpSlaResultsOperStatus_Object=MibTableColumn
fsIpSlaResultsOperStatus=_FsIpSlaResultsOperStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,1),_FsIpSlaResultsOperStatus_Type())
fsIpSlaResultsOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsOperStatus.setStatus(_A)
class _FsIpSlaResultsIpTargetAddressType_Type(InetAddressType):defaultValue=0
_FsIpSlaResultsIpTargetAddressType_Type.__name__=_H
_FsIpSlaResultsIpTargetAddressType_Object=MibTableColumn
fsIpSlaResultsIpTargetAddressType=_FsIpSlaResultsIpTargetAddressType_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,2),_FsIpSlaResultsIpTargetAddressType_Type())
fsIpSlaResultsIpTargetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsIpTargetAddressType.setStatus(_A)
class _FsIpSlaResultsIpTargetAddress_Type(InetAddress):defaultHexValue=''
_FsIpSlaResultsIpTargetAddress_Type.__name__=_G
_FsIpSlaResultsIpTargetAddress_Object=MibTableColumn
fsIpSlaResultsIpTargetAddress=_FsIpSlaResultsIpTargetAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,3),_FsIpSlaResultsIpTargetAddress_Type())
fsIpSlaResultsIpTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsIpTargetAddress.setStatus(_A)
_FsIpSlaResultsMaxRtt_Type=Unsigned32
_FsIpSlaResultsMaxRtt_Object=MibTableColumn
fsIpSlaResultsMaxRtt=_FsIpSlaResultsMaxRtt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,4),_FsIpSlaResultsMaxRtt_Type())
fsIpSlaResultsMaxRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:fsIpSlaResultsMaxRtt.setUnits(_C)
_FsIpSlaResultsMinRtt_Type=Unsigned32
_FsIpSlaResultsMinRtt_Object=MibTableColumn
fsIpSlaResultsMinRtt=_FsIpSlaResultsMinRtt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,5),_FsIpSlaResultsMinRtt_Type())
fsIpSlaResultsMinRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsMinRtt.setStatus(_A)
if mibBuilder.loadTexts:fsIpSlaResultsMinRtt.setUnits(_C)
_FsIpSlaResultsAverageRtt_Type=Unsigned32
_FsIpSlaResultsAverageRtt_Object=MibTableColumn
fsIpSlaResultsAverageRtt=_FsIpSlaResultsAverageRtt_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,6),_FsIpSlaResultsAverageRtt_Type())
fsIpSlaResultsAverageRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsAverageRtt.setStatus(_A)
if mibBuilder.loadTexts:fsIpSlaResultsAverageRtt.setUnits(_C)
_FsIpSlaResultsDelayJitter_Type=Unsigned32
_FsIpSlaResultsDelayJitter_Object=MibTableColumn
fsIpSlaResultsDelayJitter=_FsIpSlaResultsDelayJitter_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,7),_FsIpSlaResultsDelayJitter_Type())
fsIpSlaResultsDelayJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsDelayJitter.setStatus(_A)
if mibBuilder.loadTexts:fsIpSlaResultsDelayJitter.setUnits(_C)
_FsIpSlaResultsPktsLossRate_Type=Unsigned32
_FsIpSlaResultsPktsLossRate_Object=MibTableColumn
fsIpSlaResultsPktsLossRate=_FsIpSlaResultsPktsLossRate_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,8),_FsIpSlaResultsPktsLossRate_Type())
fsIpSlaResultsPktsLossRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsPktsLossRate.setStatus(_A)
_FsIpSlaResultsNetworkAF_Type=Unsigned32
_FsIpSlaResultsNetworkAF_Object=MibTableColumn
fsIpSlaResultsNetworkAF=_FsIpSlaResultsNetworkAF_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,9),_FsIpSlaResultsNetworkAF_Type())
fsIpSlaResultsNetworkAF.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsNetworkAF.setStatus(_A)
_FsIpSlaResultsProbeResponses_Type=Gauge32
_FsIpSlaResultsProbeResponses_Object=MibTableColumn
fsIpSlaResultsProbeResponses=_FsIpSlaResultsProbeResponses_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,10),_FsIpSlaResultsProbeResponses_Type())
fsIpSlaResultsProbeResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsProbeResponses.setStatus(_A)
if mibBuilder.loadTexts:fsIpSlaResultsProbeResponses.setUnits('responses')
_FsIpSlaResultsSentProbes_Type=Gauge32
_FsIpSlaResultsSentProbes_Object=MibTableColumn
fsIpSlaResultsSentProbes=_FsIpSlaResultsSentProbes_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,11),_FsIpSlaResultsSentProbes_Type())
fsIpSlaResultsSentProbes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsSentProbes.setStatus(_A)
if mibBuilder.loadTexts:fsIpSlaResultsSentProbes.setUnits('probes')
_FsIpSlaResultsRttSumOfSquares_Type=Unsigned32
_FsIpSlaResultsRttSumOfSquares_Object=MibTableColumn
fsIpSlaResultsRttSumOfSquares=_FsIpSlaResultsRttSumOfSquares_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,12),_FsIpSlaResultsRttSumOfSquares_Type())
fsIpSlaResultsRttSumOfSquares.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsRttSumOfSquares.setStatus(_A)
if mibBuilder.loadTexts:fsIpSlaResultsRttSumOfSquares.setUnits(_C)
_FsIpSlaResultsLastGoodProbe_Type=DateAndTime
_FsIpSlaResultsLastGoodProbe_Object=MibTableColumn
fsIpSlaResultsLastGoodProbe=_FsIpSlaResultsLastGoodProbe_Object((1,3,6,1,4,1,52642,1,1,10,2,106,5,1,1,1,13),_FsIpSlaResultsLastGoodProbe_Type())
fsIpSlaResultsLastGoodProbe.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpSlaResultsLastGoodProbe.setStatus(_A)
mibBuilder.exportSymbols('FS-IP-SLA-MIB',**{'fsIpSlaMIB':fsIpSlaMIB,'fsIpSlaMIBObjects':fsIpSlaMIBObjects,'fsIpSlaResultsTable':fsIpSlaResultsTable,'fsIpSlaResultsEntry':fsIpSlaResultsEntry,'fsIpSlaResultsOperStatus':fsIpSlaResultsOperStatus,'fsIpSlaResultsIpTargetAddressType':fsIpSlaResultsIpTargetAddressType,'fsIpSlaResultsIpTargetAddress':fsIpSlaResultsIpTargetAddress,'fsIpSlaResultsMaxRtt':fsIpSlaResultsMaxRtt,'fsIpSlaResultsMinRtt':fsIpSlaResultsMinRtt,'fsIpSlaResultsAverageRtt':fsIpSlaResultsAverageRtt,'fsIpSlaResultsDelayJitter':fsIpSlaResultsDelayJitter,'fsIpSlaResultsPktsLossRate':fsIpSlaResultsPktsLossRate,'fsIpSlaResultsNetworkAF':fsIpSlaResultsNetworkAF,'fsIpSlaResultsProbeResponses':fsIpSlaResultsProbeResponses,'fsIpSlaResultsSentProbes':fsIpSlaResultsSentProbes,'fsIpSlaResultsRttSumOfSquares':fsIpSlaResultsRttSumOfSquares,'fsIpSlaResultsLastGoodProbe':fsIpSlaResultsLastGoodProbe})