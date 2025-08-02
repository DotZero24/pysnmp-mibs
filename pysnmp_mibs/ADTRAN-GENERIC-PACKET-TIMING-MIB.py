_L='sysName'
_K='SNMPv2-MIB'
_J='adTrapInformSeqNum'
_I='ADTRAN-GENTRAPINFORM-MIB'
_H='adGenSlotInfoIndex'
_G='ADTRAN-GENSLOT-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_G,_H)
adTrapInformSeqNum,=mibBuilder.importSymbols(_I,_J)
adGenPacketTiming,adGenPacketTimingID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenPacketTiming','adGenPacketTimingID')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_K,_L)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
adGenPacketTimingModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,32,1))
if mibBuilder.loadTexts:adGenPacketTimingModuleIdentity.setRevisions(('2011-06-01 00:00',))
_AdGenPacketTimingProv_ObjectIdentity=ObjectIdentity
adGenPacketTimingProv=_AdGenPacketTimingProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,32,1))
_AdGenPacketTimingProvTable_Object=MibTable
adGenPacketTimingProvTable=_AdGenPacketTimingProvTable_Object((1,3,6,1,4,1,664,5,70,32,1,1))
if mibBuilder.loadTexts:adGenPacketTimingProvTable.setStatus(_A)
_AdGenPacketTimingProvTableEntry_Object=MibTableRow
adGenPacketTimingProvTableEntry=_AdGenPacketTimingProvTableEntry_Object((1,3,6,1,4,1,664,5,70,32,1,1,1))
adGenPacketTimingProvTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPacketTimingProvTableEntry.setStatus(_A)
class _AdGenPacketTimingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('server',1),('client',2)))
_AdGenPacketTimingMode_Type.__name__=_C
_AdGenPacketTimingMode_Object=MibTableColumn
adGenPacketTimingMode=_AdGenPacketTimingMode_Object((1,3,6,1,4,1,664,5,70,32,1,1,1,1),_AdGenPacketTimingMode_Type())
adGenPacketTimingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPacketTimingMode.setStatus(_A)
class _AdGenPacketTimingDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AdGenPacketTimingDscp_Type.__name__=_C
_AdGenPacketTimingDscp_Object=MibTableColumn
adGenPacketTimingDscp=_AdGenPacketTimingDscp_Object((1,3,6,1,4,1,664,5,70,32,1,1,1,2),_AdGenPacketTimingDscp_Type())
adGenPacketTimingDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPacketTimingDscp.setStatus(_A)
_AdGenPacketTimingServerIPAddress_Type=IpAddress
_AdGenPacketTimingServerIPAddress_Object=MibTableColumn
adGenPacketTimingServerIPAddress=_AdGenPacketTimingServerIPAddress_Object((1,3,6,1,4,1,664,5,70,32,1,1,1,3),_AdGenPacketTimingServerIPAddress_Type())
adGenPacketTimingServerIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPacketTimingServerIPAddress.setStatus(_A)
_AdGenPacketTimingServerMacAddress_Type=MacAddress
_AdGenPacketTimingServerMacAddress_Object=MibTableColumn
adGenPacketTimingServerMacAddress=_AdGenPacketTimingServerMacAddress_Object((1,3,6,1,4,1,664,5,70,32,1,1,1,4),_AdGenPacketTimingServerMacAddress_Type())
adGenPacketTimingServerMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingServerMacAddress.setStatus(_A)
class _AdGenPacketTimingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inband',1),('sntp',2),('sntpInband',3)))
_AdGenPacketTimingType_Type.__name__=_C
_AdGenPacketTimingType_Object=MibTableColumn
adGenPacketTimingType=_AdGenPacketTimingType_Object((1,3,6,1,4,1,664,5,70,32,1,1,1,5),_AdGenPacketTimingType_Type())
adGenPacketTimingType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPacketTimingType.setStatus(_A)
_AdGenPacketTimingUncorrelate_Type=TruthValue
_AdGenPacketTimingUncorrelate_Object=MibTableColumn
adGenPacketTimingUncorrelate=_AdGenPacketTimingUncorrelate_Object((1,3,6,1,4,1,664,5,70,32,1,1,1,6),_AdGenPacketTimingUncorrelate_Type())
adGenPacketTimingUncorrelate.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPacketTimingUncorrelate.setStatus(_A)
class _AdGenPacketTimingServiceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inService',1),('oosUnassigned',2)))
_AdGenPacketTimingServiceState_Type.__name__=_C
_AdGenPacketTimingServiceState_Object=MibTableColumn
adGenPacketTimingServiceState=_AdGenPacketTimingServiceState_Object((1,3,6,1,4,1,664,5,70,32,1,1,1,7),_AdGenPacketTimingServiceState_Type())
adGenPacketTimingServiceState.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPacketTimingServiceState.setStatus(_A)
_AdGenPacketTimingErrorInfo_Type=DisplayString
_AdGenPacketTimingErrorInfo_Object=MibTableColumn
adGenPacketTimingErrorInfo=_AdGenPacketTimingErrorInfo_Object((1,3,6,1,4,1,664,5,70,32,1,1,1,8),_AdGenPacketTimingErrorInfo_Type())
adGenPacketTimingErrorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingErrorInfo.setStatus(_A)
_AdGenPacketTimingStatus_ObjectIdentity=ObjectIdentity
adGenPacketTimingStatus=_AdGenPacketTimingStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,32,2))
_AdGenPacketTimingClientStatus_ObjectIdentity=ObjectIdentity
adGenPacketTimingClientStatus=_AdGenPacketTimingClientStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,32,2,1))
_AdGenPacketTimingStatTable_Object=MibTable
adGenPacketTimingStatTable=_AdGenPacketTimingStatTable_Object((1,3,6,1,4,1,664,5,70,32,2,1,1))
if mibBuilder.loadTexts:adGenPacketTimingStatTable.setStatus(_A)
_AdGenPacketTimingStatTableEntry_Object=MibTableRow
adGenPacketTimingStatTableEntry=_AdGenPacketTimingStatTableEntry_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1))
adGenPacketTimingStatTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPacketTimingStatTableEntry.setStatus(_A)
class _AdGenPacketTimingStatRxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*(('init',1),('savePhaseError',2),('wait',3),('frequencyEstimate',4),('jamPhaseBuildout',5),('locked',7)))
_AdGenPacketTimingStatRxState_Type.__name__=_C
_AdGenPacketTimingStatRxState_Object=MibTableColumn
adGenPacketTimingStatRxState=_AdGenPacketTimingStatRxState_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,1),_AdGenPacketTimingStatRxState_Type())
adGenPacketTimingStatRxState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatRxState.setStatus(_A)
_AdGenPacketTimingStatReset_Type=Unsigned32
_AdGenPacketTimingStatReset_Object=MibTableColumn
adGenPacketTimingStatReset=_AdGenPacketTimingStatReset_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,2),_AdGenPacketTimingStatReset_Type())
adGenPacketTimingStatReset.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatReset.setStatus(_A)
_AdGenPacketTimingStatTxPackets_Type=Unsigned32
_AdGenPacketTimingStatTxPackets_Object=MibTableColumn
adGenPacketTimingStatTxPackets=_AdGenPacketTimingStatTxPackets_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,3),_AdGenPacketTimingStatTxPackets_Type())
adGenPacketTimingStatTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatTxPackets.setStatus(_A)
_AdGenPacketTimingStatRxGoodPackets_Type=Unsigned32
_AdGenPacketTimingStatRxGoodPackets_Object=MibTableColumn
adGenPacketTimingStatRxGoodPackets=_AdGenPacketTimingStatRxGoodPackets_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,4),_AdGenPacketTimingStatRxGoodPackets_Type())
adGenPacketTimingStatRxGoodPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatRxGoodPackets.setStatus(_A)
_AdGenPacketTimingStatRxBadPackets_Type=Unsigned32
_AdGenPacketTimingStatRxBadPackets_Object=MibTableColumn
adGenPacketTimingStatRxBadPackets=_AdGenPacketTimingStatRxBadPackets_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,5),_AdGenPacketTimingStatRxBadPackets_Type())
adGenPacketTimingStatRxBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatRxBadPackets.setStatus(_A)
_AdGenPacketTimingStatFreqOffset_Type=Unsigned32
_AdGenPacketTimingStatFreqOffset_Object=MibTableColumn
adGenPacketTimingStatFreqOffset=_AdGenPacketTimingStatFreqOffset_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,6),_AdGenPacketTimingStatFreqOffset_Type())
adGenPacketTimingStatFreqOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatFreqOffset.setStatus(_A)
_AdGenPacketTimingStatPDV_Type=Unsigned32
_AdGenPacketTimingStatPDV_Object=MibTableColumn
adGenPacketTimingStatPDV=_AdGenPacketTimingStatPDV_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,7),_AdGenPacketTimingStatPDV_Type())
adGenPacketTimingStatPDV.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatPDV.setStatus(_A)
_AdGenPacketTimingStatMaxDelay_Type=Unsigned32
_AdGenPacketTimingStatMaxDelay_Object=MibTableColumn
adGenPacketTimingStatMaxDelay=_AdGenPacketTimingStatMaxDelay_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,8),_AdGenPacketTimingStatMaxDelay_Type())
adGenPacketTimingStatMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatMaxDelay.setStatus(_A)
_AdGenPacketTimingStatMinDelay_Type=Unsigned32
_AdGenPacketTimingStatMinDelay_Object=MibTableColumn
adGenPacketTimingStatMinDelay=_AdGenPacketTimingStatMinDelay_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,9),_AdGenPacketTimingStatMinDelay_Type())
adGenPacketTimingStatMinDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatMinDelay.setStatus(_A)
_AdGenPacketTimingStatHiCapTxPackets_Type=Counter64
_AdGenPacketTimingStatHiCapTxPackets_Object=MibTableColumn
adGenPacketTimingStatHiCapTxPackets=_AdGenPacketTimingStatHiCapTxPackets_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,10),_AdGenPacketTimingStatHiCapTxPackets_Type())
adGenPacketTimingStatHiCapTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatHiCapTxPackets.setStatus(_A)
_AdGenPacketTimingStatHiCapRxGoodPackets_Type=Counter64
_AdGenPacketTimingStatHiCapRxGoodPackets_Object=MibTableColumn
adGenPacketTimingStatHiCapRxGoodPackets=_AdGenPacketTimingStatHiCapRxGoodPackets_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,11),_AdGenPacketTimingStatHiCapRxGoodPackets_Type())
adGenPacketTimingStatHiCapRxGoodPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatHiCapRxGoodPackets.setStatus(_A)
_AdGenPacketTimingStatHiCapRxBadPackets_Type=Counter64
_AdGenPacketTimingStatHiCapRxBadPackets_Object=MibTableColumn
adGenPacketTimingStatHiCapRxBadPackets=_AdGenPacketTimingStatHiCapRxBadPackets_Object((1,3,6,1,4,1,664,5,70,32,2,1,1,1,12),_AdGenPacketTimingStatHiCapRxBadPackets_Type())
adGenPacketTimingStatHiCapRxBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPacketTimingStatHiCapRxBadPackets.setStatus(_A)
_AdGenPacketTimingResetTable_Object=MibTable
adGenPacketTimingResetTable=_AdGenPacketTimingResetTable_Object((1,3,6,1,4,1,664,5,70,32,2,1,3))
if mibBuilder.loadTexts:adGenPacketTimingResetTable.setStatus(_A)
_AdGenPacketTimingResetTableEntry_Object=MibTableRow
adGenPacketTimingResetTableEntry=_AdGenPacketTimingResetTableEntry_Object((1,3,6,1,4,1,664,5,70,32,2,1,3,1))
adGenPacketTimingResetTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenPacketTimingResetTableEntry.setStatus(_A)
class _AdGenPacketTimingResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenPacketTimingResetCounters_Type.__name__=_C
_AdGenPacketTimingResetCounters_Object=MibTableColumn
adGenPacketTimingResetCounters=_AdGenPacketTimingResetCounters_Object((1,3,6,1,4,1,664,5,70,32,2,1,3,1,1),_AdGenPacketTimingResetCounters_Type())
adGenPacketTimingResetCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPacketTimingResetCounters.setStatus(_A)
_AdGenPacketTimingAlarms_ObjectIdentity=ObjectIdentity
adGenPacketTimingAlarms=_AdGenPacketTimingAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,70,32,3))
_AdGenPacketTimingEvents_ObjectIdentity=ObjectIdentity
adGenPacketTimingEvents=_AdGenPacketTimingEvents_ObjectIdentity((1,3,6,1,4,1,664,5,70,32,3,0))
adGenPacketTimingClientLOPSClear=NotificationType((1,3,6,1,4,1,664,5,70,32,3,0,1))
adGenPacketTimingClientLOPSClear.setObjects(*((_I,_J),(_K,_L),(_G,_H),(_E,_F)))
if mibBuilder.loadTexts:adGenPacketTimingClientLOPSClear.setStatus(_A)
adGenPacketTimingClientLOPSActive=NotificationType((1,3,6,1,4,1,664,5,70,32,3,0,2))
adGenPacketTimingClientLOPSActive.setObjects(*((_I,_J),(_K,_L),(_G,_H),(_E,_F)))
if mibBuilder.loadTexts:adGenPacketTimingClientLOPSActive.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GENERIC-PACKET-TIMING-MIB',**{'adGenPacketTimingProv':adGenPacketTimingProv,'adGenPacketTimingProvTable':adGenPacketTimingProvTable,'adGenPacketTimingProvTableEntry':adGenPacketTimingProvTableEntry,'adGenPacketTimingMode':adGenPacketTimingMode,'adGenPacketTimingDscp':adGenPacketTimingDscp,'adGenPacketTimingServerIPAddress':adGenPacketTimingServerIPAddress,'adGenPacketTimingServerMacAddress':adGenPacketTimingServerMacAddress,'adGenPacketTimingType':adGenPacketTimingType,'adGenPacketTimingUncorrelate':adGenPacketTimingUncorrelate,'adGenPacketTimingServiceState':adGenPacketTimingServiceState,'adGenPacketTimingErrorInfo':adGenPacketTimingErrorInfo,'adGenPacketTimingStatus':adGenPacketTimingStatus,'adGenPacketTimingClientStatus':adGenPacketTimingClientStatus,'adGenPacketTimingStatTable':adGenPacketTimingStatTable,'adGenPacketTimingStatTableEntry':adGenPacketTimingStatTableEntry,'adGenPacketTimingStatRxState':adGenPacketTimingStatRxState,'adGenPacketTimingStatReset':adGenPacketTimingStatReset,'adGenPacketTimingStatTxPackets':adGenPacketTimingStatTxPackets,'adGenPacketTimingStatRxGoodPackets':adGenPacketTimingStatRxGoodPackets,'adGenPacketTimingStatRxBadPackets':adGenPacketTimingStatRxBadPackets,'adGenPacketTimingStatFreqOffset':adGenPacketTimingStatFreqOffset,'adGenPacketTimingStatPDV':adGenPacketTimingStatPDV,'adGenPacketTimingStatMaxDelay':adGenPacketTimingStatMaxDelay,'adGenPacketTimingStatMinDelay':adGenPacketTimingStatMinDelay,'adGenPacketTimingStatHiCapTxPackets':adGenPacketTimingStatHiCapTxPackets,'adGenPacketTimingStatHiCapRxGoodPackets':adGenPacketTimingStatHiCapRxGoodPackets,'adGenPacketTimingStatHiCapRxBadPackets':adGenPacketTimingStatHiCapRxBadPackets,'adGenPacketTimingResetTable':adGenPacketTimingResetTable,'adGenPacketTimingResetTableEntry':adGenPacketTimingResetTableEntry,'adGenPacketTimingResetCounters':adGenPacketTimingResetCounters,'adGenPacketTimingAlarms':adGenPacketTimingAlarms,'adGenPacketTimingEvents':adGenPacketTimingEvents,'adGenPacketTimingClientLOPSClear':adGenPacketTimingClientLOPSClear,'adGenPacketTimingClientLOPSActive':adGenPacketTimingClientLOPSActive,'adGenPacketTimingModuleIdentity':adGenPacketTimingModuleIdentity})