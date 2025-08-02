_Q='busErrLogIndex'
_P='outOfRes'
_O='busVccMtFwdVci'
_N='busVccMtFwdVpi'
_M='busVccAtmIfIndex'
_L='DisplayString'
_K='AtmLaneMask'
_J='Integer'
_I='busLecAtmAddr'
_H='other'
_G='not-accessible'
_F='busConfIndex'
_E='Integer32'
_D='read-write'
_C='LAN-EMULATION-BUS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1',_J,'OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VciInteger,VpiInteger,atmfLanEmulation=mibBuilder.importSymbols('LAN-EMULATION-CLIENT-MIB','VciInteger','VpiInteger','atmfLanEmulation')
AtmLaneMask,IfIndexOrZero,Integer,TIMESTAMP=mibBuilder.importSymbols('LAN-EMULATION-ELAN-MIB',_K,'IfIndexOrZero',_J,'TIMESTAMP')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
class RowStatus(Integer32):0
class AtmLaneAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
_BusMIB_ObjectIdentity=ObjectIdentity
busMIB=_BusMIB_ObjectIdentity((1,3,6,1,4,1,353,5,3,4))
_BusConfGroup_ObjectIdentity=ObjectIdentity
busConfGroup=_BusConfGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,4,1))
_BusConfNextId_Type=Integer32
_BusConfNextId_Object=MibScalar
busConfNextId=_BusConfNextId_Object((1,3,6,1,4,1,353,5,3,4,1,1),_BusConfNextId_Type())
busConfNextId.setMaxAccess(_B)
if mibBuilder.loadTexts:busConfNextId.setStatus(_A)
_BusConfTable_Object=MibTable
busConfTable=_BusConfTable_Object((1,3,6,1,4,1,353,5,3,4,1,2))
if mibBuilder.loadTexts:busConfTable.setStatus(_A)
_BusConfEntry_Object=MibTableRow
busConfEntry=_BusConfEntry_Object((1,3,6,1,4,1,353,5,3,4,1,2,1))
busConfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:busConfEntry.setStatus(_A)
_BusConfIndex_Type=Integer32
_BusConfIndex_Object=MibTableColumn
busConfIndex=_BusConfIndex_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,1),_BusConfIndex_Type())
busConfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:busConfIndex.setStatus(_A)
_BusConfAtmAddrSpec_Type=AtmLaneAddress
_BusConfAtmAddrSpec_Object=MibTableColumn
busConfAtmAddrSpec=_BusConfAtmAddrSpec_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,2),_BusConfAtmAddrSpec_Type())
busConfAtmAddrSpec.setMaxAccess(_D)
if mibBuilder.loadTexts:busConfAtmAddrSpec.setStatus(_A)
class _BusConfAtmAddrMask_Type(AtmLaneMask):defaultHexValue='0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
_BusConfAtmAddrMask_Type.__name__=_K
_BusConfAtmAddrMask_Object=MibTableColumn
busConfAtmAddrMask=_BusConfAtmAddrMask_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,3),_BusConfAtmAddrMask_Type())
busConfAtmAddrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:busConfAtmAddrMask.setStatus(_A)
_BusConfAtmAddrActual_Type=AtmLaneAddress
_BusConfAtmAddrActual_Object=MibTableColumn
busConfAtmAddrActual=_BusConfAtmAddrActual_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,4),_BusConfAtmAddrActual_Type())
busConfAtmAddrActual.setMaxAccess(_B)
if mibBuilder.loadTexts:busConfAtmAddrActual.setStatus(_A)
class _BusConfElanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BusConfElanName_Type.__name__=_L
_BusConfElanName_Object=MibTableColumn
busConfElanName=_BusConfElanName_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,5),_BusConfElanName_Type())
busConfElanName.setMaxAccess(_D)
if mibBuilder.loadTexts:busConfElanName.setStatus(_A)
_BusConfLastChange_Type=TIMESTAMP
_BusConfLastChange_Object=MibTableColumn
busConfLastChange=_BusConfLastChange_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,6),_BusConfLastChange_Type())
busConfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:busConfLastChange.setStatus(_A)
class _BusConfMaxFrameAge_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BusConfMaxFrameAge_Type.__name__=_E
_BusConfMaxFrameAge_Object=MibTableColumn
busConfMaxFrameAge=_BusConfMaxFrameAge_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,7),_BusConfMaxFrameAge_Type())
busConfMaxFrameAge.setMaxAccess(_D)
if mibBuilder.loadTexts:busConfMaxFrameAge.setStatus(_A)
class _BusConfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('up',2),('down',3)))
_BusConfOperStatus_Type.__name__=_E
_BusConfOperStatus_Object=MibTableColumn
busConfOperStatus=_BusConfOperStatus_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,8),_BusConfOperStatus_Type())
busConfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:busConfOperStatus.setStatus(_A)
class _BusConfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('up',2),('down',3)))
_BusConfAdminStatus_Type.__name__=_E
_BusConfAdminStatus_Object=MibTableColumn
busConfAdminStatus=_BusConfAdminStatus_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,9),_BusConfAdminStatus_Type())
busConfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:busConfAdminStatus.setStatus(_A)
_BusConfRowStatus_Type=RowStatus
_BusConfRowStatus_Object=MibTableColumn
busConfRowStatus=_BusConfRowStatus_Object((1,3,6,1,4,1,353,5,3,4,1,2,1,10),_BusConfRowStatus_Type())
busConfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:busConfRowStatus.setStatus(_A)
_BusVccTable_Object=MibTable
busVccTable=_BusVccTable_Object((1,3,6,1,4,1,353,5,3,4,1,3))
if mibBuilder.loadTexts:busVccTable.setStatus(_A)
_BusVccEntry_Object=MibTableRow
busVccEntry=_BusVccEntry_Object((1,3,6,1,4,1,353,5,3,4,1,3,1))
busVccEntry.setIndexNames((0,_C,_F),(0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:busVccEntry.setStatus(_A)
_BusVccAtmIfIndex_Type=IfIndexOrZero
_BusVccAtmIfIndex_Object=MibTableColumn
busVccAtmIfIndex=_BusVccAtmIfIndex_Object((1,3,6,1,4,1,353,5,3,4,1,3,1,1),_BusVccAtmIfIndex_Type())
busVccAtmIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:busVccAtmIfIndex.setStatus(_A)
_BusVccMtFwdVpi_Type=VpiInteger
_BusVccMtFwdVpi_Object=MibTableColumn
busVccMtFwdVpi=_BusVccMtFwdVpi_Object((1,3,6,1,4,1,353,5,3,4,1,3,1,2),_BusVccMtFwdVpi_Type())
busVccMtFwdVpi.setMaxAccess(_G)
if mibBuilder.loadTexts:busVccMtFwdVpi.setStatus(_A)
_BusVccMtFwdVci_Type=VciInteger
_BusVccMtFwdVci_Object=MibTableColumn
busVccMtFwdVci=_BusVccMtFwdVci_Object((1,3,6,1,4,1,353,5,3,4,1,3,1,3),_BusVccMtFwdVci_Type())
busVccMtFwdVci.setMaxAccess(_G)
if mibBuilder.loadTexts:busVccMtFwdVci.setStatus(_A)
_BusVccRowStatus_Type=RowStatus
_BusVccRowStatus_Object=MibTableColumn
busVccRowStatus=_BusVccRowStatus_Object((1,3,6,1,4,1,353,5,3,4,1,3,1,4),_BusVccRowStatus_Type())
busVccRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:busVccRowStatus.setStatus(_A)
_BusLecTableLastChange_Type=TIMESTAMP
_BusLecTableLastChange_Object=MibScalar
busLecTableLastChange=_BusLecTableLastChange_Object((1,3,6,1,4,1,353,5,3,4,1,4),_BusLecTableLastChange_Type())
busLecTableLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:busLecTableLastChange.setStatus(_A)
_BusLecTable_Object=MibTable
busLecTable=_BusLecTable_Object((1,3,6,1,4,1,353,5,3,4,1,5))
if mibBuilder.loadTexts:busLecTable.setStatus(_A)
_BusLecEntry_Object=MibTableRow
busLecEntry=_BusLecEntry_Object((1,3,6,1,4,1,353,5,3,4,1,5,1))
busLecEntry.setIndexNames((0,_C,_F),(0,_C,_I))
if mibBuilder.loadTexts:busLecEntry.setStatus(_A)
_BusLecAtmAddr_Type=AtmLaneAddress
_BusLecAtmAddr_Object=MibTableColumn
busLecAtmAddr=_BusLecAtmAddr_Object((1,3,6,1,4,1,353,5,3,4,1,5,1,1),_BusLecAtmAddr_Type())
busLecAtmAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:busLecAtmAddr.setStatus(_A)
_BusLecMcastSendAtmIfIndex_Type=IfIndexOrZero
_BusLecMcastSendAtmIfIndex_Object=MibTableColumn
busLecMcastSendAtmIfIndex=_BusLecMcastSendAtmIfIndex_Object((1,3,6,1,4,1,353,5,3,4,1,5,1,2),_BusLecMcastSendAtmIfIndex_Type())
busLecMcastSendAtmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:busLecMcastSendAtmIfIndex.setStatus(_A)
_BusLecMcastSendVpi_Type=VpiInteger
_BusLecMcastSendVpi_Object=MibTableColumn
busLecMcastSendVpi=_BusLecMcastSendVpi_Object((1,3,6,1,4,1,353,5,3,4,1,5,1,4),_BusLecMcastSendVpi_Type())
busLecMcastSendVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:busLecMcastSendVpi.setStatus(_A)
_BusLecMcastSendVci_Type=VciInteger
_BusLecMcastSendVci_Object=MibTableColumn
busLecMcastSendVci=_BusLecMcastSendVci_Object((1,3,6,1,4,1,353,5,3,4,1,5,1,5),_BusLecMcastSendVci_Type())
busLecMcastSendVci.setMaxAccess(_D)
if mibBuilder.loadTexts:busLecMcastSendVci.setStatus(_A)
_BusLecRowStatus_Type=RowStatus
_BusLecRowStatus_Object=MibTableColumn
busLecRowStatus=_BusLecRowStatus_Object((1,3,6,1,4,1,353,5,3,4,1,5,1,6),_BusLecRowStatus_Type())
busLecRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:busLecRowStatus.setStatus(_A)
_BusStatGroup_ObjectIdentity=ObjectIdentity
busStatGroup=_BusStatGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,4,2))
_BusStatTable_Object=MibTable
busStatTable=_BusStatTable_Object((1,3,6,1,4,1,353,5,3,4,2,1))
if mibBuilder.loadTexts:busStatTable.setStatus(_A)
_BusStatEntry_Object=MibTableRow
busStatEntry=_BusStatEntry_Object((1,3,6,1,4,1,353,5,3,4,2,1,1))
busStatEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:busStatEntry.setStatus(_A)
_BusStatInDiscards_Type=Counter32
_BusStatInDiscards_Object=MibTableColumn
busStatInDiscards=_BusStatInDiscards_Object((1,3,6,1,4,1,353,5,3,4,2,1,1,1),_BusStatInDiscards_Type())
busStatInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:busStatInDiscards.setStatus(_A)
_BusStatInOctets_Type=Counter32
_BusStatInOctets_Object=MibTableColumn
busStatInOctets=_BusStatInOctets_Object((1,3,6,1,4,1,353,5,3,4,2,1,1,2),_BusStatInOctets_Type())
busStatInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:busStatInOctets.setStatus(_A)
_BusStatInUcastFrms_Type=Counter32
_BusStatInUcastFrms_Object=MibTableColumn
busStatInUcastFrms=_BusStatInUcastFrms_Object((1,3,6,1,4,1,353,5,3,4,2,1,1,3),_BusStatInUcastFrms_Type())
busStatInUcastFrms.setMaxAccess(_B)
if mibBuilder.loadTexts:busStatInUcastFrms.setStatus(_A)
_BusStatInMcastFrms_Type=Counter32
_BusStatInMcastFrms_Object=MibTableColumn
busStatInMcastFrms=_BusStatInMcastFrms_Object((1,3,6,1,4,1,353,5,3,4,2,1,1,4),_BusStatInMcastFrms_Type())
busStatInMcastFrms.setMaxAccess(_B)
if mibBuilder.loadTexts:busStatInMcastFrms.setStatus(_A)
_BusStatFrmTimeOuts_Type=Counter32
_BusStatFrmTimeOuts_Object=MibTableColumn
busStatFrmTimeOuts=_BusStatFrmTimeOuts_Object((1,3,6,1,4,1,353,5,3,4,2,1,1,5),_BusStatFrmTimeOuts_Type())
busStatFrmTimeOuts.setMaxAccess(_B)
if mibBuilder.loadTexts:busStatFrmTimeOuts.setStatus(_A)
_BusStatMcastSendRefused_Type=Counter32
_BusStatMcastSendRefused_Object=MibTableColumn
busStatMcastSendRefused=_BusStatMcastSendRefused_Object((1,3,6,1,4,1,353,5,3,4,2,1,1,6),_BusStatMcastSendRefused_Type())
busStatMcastSendRefused.setMaxAccess(_B)
if mibBuilder.loadTexts:busStatMcastSendRefused.setStatus(_A)
_BusStatMcastFwdFailure_Type=Counter32
_BusStatMcastFwdFailure_Object=MibTableColumn
busStatMcastFwdFailure=_BusStatMcastFwdFailure_Object((1,3,6,1,4,1,353,5,3,4,2,1,1,7),_BusStatMcastFwdFailure_Type())
busStatMcastFwdFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:busStatMcastFwdFailure.setStatus(_A)
_BusLecStatTable_Object=MibTable
busLecStatTable=_BusLecStatTable_Object((1,3,6,1,4,1,353,5,3,4,2,2))
if mibBuilder.loadTexts:busLecStatTable.setStatus(_A)
_BusLecStatEntry_Object=MibTableRow
busLecStatEntry=_BusLecStatEntry_Object((1,3,6,1,4,1,353,5,3,4,2,2,1))
busLecStatEntry.setIndexNames((0,_C,_F),(0,_C,_I))
if mibBuilder.loadTexts:busLecStatEntry.setStatus(_A)
_BusLecRecvs_Type=Counter32
_BusLecRecvs_Object=MibTableColumn
busLecRecvs=_BusLecRecvs_Object((1,3,6,1,4,1,353,5,3,4,2,2,1,1),_BusLecRecvs_Type())
busLecRecvs.setMaxAccess(_B)
if mibBuilder.loadTexts:busLecRecvs.setStatus(_A)
_BusLecForwards_Type=Counter32
_BusLecForwards_Object=MibTableColumn
busLecForwards=_BusLecForwards_Object((1,3,6,1,4,1,353,5,3,4,2,2,1,2),_BusLecForwards_Type())
busLecForwards.setMaxAccess(_B)
if mibBuilder.loadTexts:busLecForwards.setStatus(_A)
_BusLecDiscards_Type=Counter32
_BusLecDiscards_Object=MibTableColumn
busLecDiscards=_BusLecDiscards_Object((1,3,6,1,4,1,353,5,3,4,2,2,1,3),_BusLecDiscards_Type())
busLecDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:busLecDiscards.setStatus(_A)
_BusFaultGroup_ObjectIdentity=ObjectIdentity
busFaultGroup=_BusFaultGroup_ObjectIdentity((1,3,6,1,4,1,353,5,3,4,3))
_BusErrCtlTable_Object=MibTable
busErrCtlTable=_BusErrCtlTable_Object((1,3,6,1,4,1,353,5,3,4,3,1))
if mibBuilder.loadTexts:busErrCtlTable.setStatus(_A)
_BusErrCtlEntry_Object=MibTableRow
busErrCtlEntry=_BusErrCtlEntry_Object((1,3,6,1,4,1,353,5,3,4,3,1,1))
busErrCtlEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:busErrCtlEntry.setStatus(_A)
class _BusErrCtlAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_BusErrCtlAdminStatus_Type.__name__=_E
_BusErrCtlAdminStatus_Object=MibTableColumn
busErrCtlAdminStatus=_BusErrCtlAdminStatus_Object((1,3,6,1,4,1,353,5,3,4,3,1,1,1),_BusErrCtlAdminStatus_Type())
busErrCtlAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:busErrCtlAdminStatus.setStatus(_A)
class _BusErrCtlOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('active',2),(_P,3),('failed',4),('disabled',5)))
_BusErrCtlOperStatus_Type.__name__=_E
_BusErrCtlOperStatus_Object=MibTableColumn
busErrCtlOperStatus=_BusErrCtlOperStatus_Object((1,3,6,1,4,1,353,5,3,4,3,1,1,2),_BusErrCtlOperStatus_Type())
busErrCtlOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:busErrCtlOperStatus.setStatus(_A)
class _BusErrCtlClearLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('clear',2)))
_BusErrCtlClearLog_Type.__name__=_E
_BusErrCtlClearLog_Object=MibTableColumn
busErrCtlClearLog=_BusErrCtlClearLog_Object((1,3,6,1,4,1,353,5,3,4,3,1,1,3),_BusErrCtlClearLog_Type())
busErrCtlClearLog.setMaxAccess(_D)
if mibBuilder.loadTexts:busErrCtlClearLog.setStatus(_A)
class _BusErrCtlMaxEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BusErrCtlMaxEntries_Type.__name__=_E
_BusErrCtlMaxEntries_Object=MibTableColumn
busErrCtlMaxEntries=_BusErrCtlMaxEntries_Object((1,3,6,1,4,1,353,5,3,4,3,1,1,4),_BusErrCtlMaxEntries_Type())
busErrCtlMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:busErrCtlMaxEntries.setStatus(_A)
class _BusErrCtlLastEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BusErrCtlLastEntry_Type.__name__=_E
_BusErrCtlLastEntry_Object=MibTableColumn
busErrCtlLastEntry=_BusErrCtlLastEntry_Object((1,3,6,1,4,1,353,5,3,4,3,1,1,5),_BusErrCtlLastEntry_Type())
busErrCtlLastEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:busErrCtlLastEntry.setStatus(_A)
_BusErrLogTable_Object=MibTable
busErrLogTable=_BusErrLogTable_Object((1,3,6,1,4,1,353,5,3,4,3,2))
if mibBuilder.loadTexts:busErrLogTable.setStatus(_A)
_BusErrLogEntry_Object=MibTableRow
busErrLogEntry=_BusErrLogEntry_Object((1,3,6,1,4,1,353,5,3,4,3,2,1))
busErrLogEntry.setIndexNames((0,_C,_F),(0,_C,_Q))
if mibBuilder.loadTexts:busErrLogEntry.setStatus(_A)
class _BusErrLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BusErrLogIndex_Type.__name__=_E
_BusErrLogIndex_Object=MibTableColumn
busErrLogIndex=_BusErrLogIndex_Object((1,3,6,1,4,1,353,5,3,4,3,2,1,1),_BusErrLogIndex_Type())
busErrLogIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:busErrLogIndex.setStatus(_A)
_BusErrLogAtmAddr_Type=AtmLaneAddress
_BusErrLogAtmAddr_Object=MibTableColumn
busErrLogAtmAddr=_BusErrLogAtmAddr_Object((1,3,6,1,4,1,353,5,3,4,3,2,1,2),_BusErrLogAtmAddr_Type())
busErrLogAtmAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:busErrLogAtmAddr.setStatus(_A)
class _BusErrLogErrCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('badCtlFrame',2),('badDataFrame',3),(_H,4)))
_BusErrLogErrCode_Type.__name__=_E
_BusErrLogErrCode_Object=MibTableColumn
busErrLogErrCode=_BusErrLogErrCode_Object((1,3,6,1,4,1,353,5,3,4,3,2,1,3),_BusErrLogErrCode_Type())
busErrLogErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:busErrLogErrCode.setStatus(_A)
_BusErrLogTime_Type=TIMESTAMP
_BusErrLogTime_Object=MibTableColumn
busErrLogTime=_BusErrLogTime_Object((1,3,6,1,4,1,353,5,3,4,3,2,1,4),_BusErrLogTime_Type())
busErrLogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:busErrLogTime.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RowStatus':RowStatus,'AtmLaneAddress':AtmLaneAddress,'busMIB':busMIB,'busConfGroup':busConfGroup,'busConfNextId':busConfNextId,'busConfTable':busConfTable,'busConfEntry':busConfEntry,_F:busConfIndex,'busConfAtmAddrSpec':busConfAtmAddrSpec,'busConfAtmAddrMask':busConfAtmAddrMask,'busConfAtmAddrActual':busConfAtmAddrActual,'busConfElanName':busConfElanName,'busConfLastChange':busConfLastChange,'busConfMaxFrameAge':busConfMaxFrameAge,'busConfOperStatus':busConfOperStatus,'busConfAdminStatus':busConfAdminStatus,'busConfRowStatus':busConfRowStatus,'busVccTable':busVccTable,'busVccEntry':busVccEntry,_M:busVccAtmIfIndex,_N:busVccMtFwdVpi,_O:busVccMtFwdVci,'busVccRowStatus':busVccRowStatus,'busLecTableLastChange':busLecTableLastChange,'busLecTable':busLecTable,'busLecEntry':busLecEntry,_I:busLecAtmAddr,'busLecMcastSendAtmIfIndex':busLecMcastSendAtmIfIndex,'busLecMcastSendVpi':busLecMcastSendVpi,'busLecMcastSendVci':busLecMcastSendVci,'busLecRowStatus':busLecRowStatus,'busStatGroup':busStatGroup,'busStatTable':busStatTable,'busStatEntry':busStatEntry,'busStatInDiscards':busStatInDiscards,'busStatInOctets':busStatInOctets,'busStatInUcastFrms':busStatInUcastFrms,'busStatInMcastFrms':busStatInMcastFrms,'busStatFrmTimeOuts':busStatFrmTimeOuts,'busStatMcastSendRefused':busStatMcastSendRefused,'busStatMcastFwdFailure':busStatMcastFwdFailure,'busLecStatTable':busLecStatTable,'busLecStatEntry':busLecStatEntry,'busLecRecvs':busLecRecvs,'busLecForwards':busLecForwards,'busLecDiscards':busLecDiscards,'busFaultGroup':busFaultGroup,'busErrCtlTable':busErrCtlTable,'busErrCtlEntry':busErrCtlEntry,'busErrCtlAdminStatus':busErrCtlAdminStatus,'busErrCtlOperStatus':busErrCtlOperStatus,'busErrCtlClearLog':busErrCtlClearLog,'busErrCtlMaxEntries':busErrCtlMaxEntries,'busErrCtlLastEntry':busErrCtlLastEntry,'busErrLogTable':busErrLogTable,'busErrLogEntry':busErrLogEntry,_Q:busErrLogIndex,'busErrLogAtmAddr':busErrLogAtmAddr,'busErrLogErrCode':busErrLogErrCode,'busErrLogTime':busErrLogTime})