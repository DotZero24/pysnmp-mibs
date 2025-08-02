_Z='adGenPolicer24HrThresholdTotalRedFrames'
_Y='adGenPolicer24HrThresholdTotalYellowFrames'
_X='adGenPolicer24HrThresholdTotalGreenFrames'
_W='adGenPolicer15MinThresholdTotalRedFrames'
_V='adGenPolicer15MinThresholdTotalYellowFrames'
_U='adGenPolicer15MinThresholdTotalGreenFrames'
_T='adGenPolicerQualifiedEVCMapLookupIndex'
_S='adGenPolicerEVCMapLookupIndex'
_R='TruthValue'
_Q='DisplayString'
_P='OctetString'
_O='adGenPolicerFixedLengthName'
_N='not-accessible'
_M='Integer32'
_L='adGenPolicerName'
_K='sysName'
_J='SNMPv2-MIB'
_I='adTrapInformSeqNum'
_H='ADTRAN-GENTRAPINFORM-MIB'
_G='read-write'
_F='read-only'
_E='read-create'
_D='adGenSlotInfoIndex'
_C='ADTRAN-GENSLOT-MIB'
_B='ADTRAN-GENPOLICER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_C,_D)
adTrapInformSeqNum,=mibBuilder.importSymbols(_H,_I)
adGenPolicer,adGenPolicerID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenPolicer','adGenPolicerID')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_Q,'PhysAddress','RowStatus','TextualConvention',_R)
adGenPolicerMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,35,1))
if mibBuilder.loadTexts:adGenPolicerMIB.setRevisions(('2012-01-30 00:00','2010-09-16 00:00'))
_AdGenPolicerEvents_ObjectIdentity=ObjectIdentity
adGenPolicerEvents=_AdGenPolicerEvents_ObjectIdentity((1,3,6,1,4,1,664,5,70,35,0))
_AdGenPolicerProvisioning_ObjectIdentity=ObjectIdentity
adGenPolicerProvisioning=_AdGenPolicerProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,35,1))
_AdGenPolicerTable_Object=MibTable
adGenPolicerTable=_AdGenPolicerTable_Object((1,3,6,1,4,1,664,5,70,35,1,1))
if mibBuilder.loadTexts:adGenPolicerTable.setStatus(_A)
_AdGenPolicerEntry_Object=MibTableRow
adGenPolicerEntry=_AdGenPolicerEntry_Object((1,3,6,1,4,1,664,5,70,35,1,1,1))
adGenPolicerEntry.setIndexNames((0,_C,_D),(1,_B,_L))
if mibBuilder.loadTexts:adGenPolicerEntry.setStatus(_A)
class _AdGenPolicerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_AdGenPolicerName_Type.__name__=_Q
_AdGenPolicerName_Object=MibTableColumn
adGenPolicerName=_AdGenPolicerName_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,1),_AdGenPolicerName_Type())
adGenPolicerName.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenPolicerName.setStatus(_A)
_AdGenPolicerRowStatus_Type=RowStatus
_AdGenPolicerRowStatus_Object=MibTableColumn
adGenPolicerRowStatus=_AdGenPolicerRowStatus_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,2),_AdGenPolicerRowStatus_Type())
adGenPolicerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerRowStatus.setStatus(_A)
_AdGenPolicerStatus_Type=DisplayString
_AdGenPolicerStatus_Object=MibTableColumn
adGenPolicerStatus=_AdGenPolicerStatus_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,3),_AdGenPolicerStatus_Type())
adGenPolicerStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerStatus.setStatus(_A)
class _AdGenPolicerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AdGenPolicerOperStatus_Type.__name__=_M
_AdGenPolicerOperStatus_Object=MibTableColumn
adGenPolicerOperStatus=_AdGenPolicerOperStatus_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,4),_AdGenPolicerOperStatus_Type())
adGenPolicerOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerOperStatus.setStatus(_A)
_AdGenPolicerCIR_Type=Integer32
_AdGenPolicerCIR_Object=MibTableColumn
adGenPolicerCIR=_AdGenPolicerCIR_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,5),_AdGenPolicerCIR_Type())
adGenPolicerCIR.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerCIR.setStatus(_A)
_AdGenPolicerCBS_Type=Integer32
_AdGenPolicerCBS_Object=MibTableColumn
adGenPolicerCBS=_AdGenPolicerCBS_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,6),_AdGenPolicerCBS_Type())
adGenPolicerCBS.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerCBS.setStatus(_A)
_AdGenPolicerEIR_Type=Integer32
_AdGenPolicerEIR_Object=MibTableColumn
adGenPolicerEIR=_AdGenPolicerEIR_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,7),_AdGenPolicerEIR_Type())
adGenPolicerEIR.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerEIR.setStatus(_A)
class _AdGenPolicerEIRNoLimit_Type(TruthValue):defaultValue=2
_AdGenPolicerEIRNoLimit_Type.__name__=_R
_AdGenPolicerEIRNoLimit_Object=MibTableColumn
adGenPolicerEIRNoLimit=_AdGenPolicerEIRNoLimit_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,8),_AdGenPolicerEIRNoLimit_Type())
adGenPolicerEIRNoLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerEIRNoLimit.setStatus(_A)
_AdGenPolicerEBS_Type=Integer32
_AdGenPolicerEBS_Object=MibTableColumn
adGenPolicerEBS=_AdGenPolicerEBS_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,9),_AdGenPolicerEBS_Type())
adGenPolicerEBS.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerEBS.setStatus(_A)
class _AdGenPolicerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unspecified',1),('perUNI',2),('perInterface',3),('perEVC',4),('perMEVC',5),('perEVCMap',6)))
_AdGenPolicerMode_Type.__name__=_M
_AdGenPolicerMode_Object=MibTableColumn
adGenPolicerMode=_AdGenPolicerMode_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,10),_AdGenPolicerMode_Type())
adGenPolicerMode.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerMode.setStatus(_A)
_AdGenPolicerUNIPort_Type=InterfaceIndexOrZero
_AdGenPolicerUNIPort_Object=MibTableColumn
adGenPolicerUNIPort=_AdGenPolicerUNIPort_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,11),_AdGenPolicerUNIPort_Type())
adGenPolicerUNIPort.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerUNIPort.setStatus(_A)
_AdGenPolicerEVCName_Type=DisplayString
_AdGenPolicerEVCName_Object=MibTableColumn
adGenPolicerEVCName=_AdGenPolicerEVCName_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,12),_AdGenPolicerEVCName_Type())
adGenPolicerEVCName.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerEVCName.setStatus(_A)
_AdGenPolicerMEVCName_Type=DisplayString
_AdGenPolicerMEVCName_Object=MibTableColumn
adGenPolicerMEVCName=_AdGenPolicerMEVCName_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,13),_AdGenPolicerMEVCName_Type())
adGenPolicerMEVCName.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerMEVCName.setStatus(_A)
_AdGenPolicerCEVlanPriority_Type=DisplayString
_AdGenPolicerCEVlanPriority_Object=MibTableColumn
adGenPolicerCEVlanPriority=_AdGenPolicerCEVlanPriority_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,14),_AdGenPolicerCEVlanPriority_Type())
adGenPolicerCEVlanPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerCEVlanPriority.setStatus(_A)
_AdGenPolicerAddEvcMap_Type=DisplayString
_AdGenPolicerAddEvcMap_Object=MibTableColumn
adGenPolicerAddEvcMap=_AdGenPolicerAddEvcMap_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,15),_AdGenPolicerAddEvcMap_Type())
adGenPolicerAddEvcMap.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerAddEvcMap.setStatus(_A)
_AdGenPolicerRemoveEvcMap_Type=DisplayString
_AdGenPolicerRemoveEvcMap_Object=MibTableColumn
adGenPolicerRemoveEvcMap=_AdGenPolicerRemoveEvcMap_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,16),_AdGenPolicerRemoveEvcMap_Type())
adGenPolicerRemoveEvcMap.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenPolicerRemoveEvcMap.setStatus(_A)
_AdGenPolicerLastError_Type=DisplayString
_AdGenPolicerLastError_Object=MibTableColumn
adGenPolicerLastError=_AdGenPolicerLastError_Object((1,3,6,1,4,1,664,5,70,35,1,1,1,17),_AdGenPolicerLastError_Type())
adGenPolicerLastError.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerLastError.setStatus(_A)
_AdGenPolicerThresholds_ObjectIdentity=ObjectIdentity
adGenPolicerThresholds=_AdGenPolicerThresholds_ObjectIdentity((1,3,6,1,4,1,664,5,70,35,1,2))
_AdGenPolicer15MinThresholdTable_Object=MibTable
adGenPolicer15MinThresholdTable=_AdGenPolicer15MinThresholdTable_Object((1,3,6,1,4,1,664,5,70,35,1,2,1))
if mibBuilder.loadTexts:adGenPolicer15MinThresholdTable.setStatus(_A)
_AdGenPolicer15MinThresholdEntry_Object=MibTableRow
adGenPolicer15MinThresholdEntry=_AdGenPolicer15MinThresholdEntry_Object((1,3,6,1,4,1,664,5,70,35,1,2,1,1))
adGenPolicer15MinThresholdEntry.setIndexNames((0,_C,_D),(0,_B,_L))
if mibBuilder.loadTexts:adGenPolicer15MinThresholdEntry.setStatus(_A)
_AdGenPolicer15MinThresholdDiscardsGreenFrames_Type=Integer32
_AdGenPolicer15MinThresholdDiscardsGreenFrames_Object=MibTableColumn
adGenPolicer15MinThresholdDiscardsGreenFrames=_AdGenPolicer15MinThresholdDiscardsGreenFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,1,1,1),_AdGenPolicer15MinThresholdDiscardsGreenFrames_Type())
adGenPolicer15MinThresholdDiscardsGreenFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer15MinThresholdDiscardsGreenFrames.setStatus(_A)
_AdGenPolicer15MinThresholdTotalGreenFrames_Type=Integer32
_AdGenPolicer15MinThresholdTotalGreenFrames_Object=MibTableColumn
adGenPolicer15MinThresholdTotalGreenFrames=_AdGenPolicer15MinThresholdTotalGreenFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,1,1,2),_AdGenPolicer15MinThresholdTotalGreenFrames_Type())
adGenPolicer15MinThresholdTotalGreenFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer15MinThresholdTotalGreenFrames.setStatus(_A)
_AdGenPolicer15MinThresholdDiscardsYellowFrames_Type=Integer32
_AdGenPolicer15MinThresholdDiscardsYellowFrames_Object=MibTableColumn
adGenPolicer15MinThresholdDiscardsYellowFrames=_AdGenPolicer15MinThresholdDiscardsYellowFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,1,1,3),_AdGenPolicer15MinThresholdDiscardsYellowFrames_Type())
adGenPolicer15MinThresholdDiscardsYellowFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer15MinThresholdDiscardsYellowFrames.setStatus(_A)
_AdGenPolicer15MinThresholdTotalYellowFrames_Type=Integer32
_AdGenPolicer15MinThresholdTotalYellowFrames_Object=MibTableColumn
adGenPolicer15MinThresholdTotalYellowFrames=_AdGenPolicer15MinThresholdTotalYellowFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,1,1,4),_AdGenPolicer15MinThresholdTotalYellowFrames_Type())
adGenPolicer15MinThresholdTotalYellowFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer15MinThresholdTotalYellowFrames.setStatus(_A)
_AdGenPolicer15MinThresholdTotalRedFrames_Type=Integer32
_AdGenPolicer15MinThresholdTotalRedFrames_Object=MibTableColumn
adGenPolicer15MinThresholdTotalRedFrames=_AdGenPolicer15MinThresholdTotalRedFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,1,1,5),_AdGenPolicer15MinThresholdTotalRedFrames_Type())
adGenPolicer15MinThresholdTotalRedFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer15MinThresholdTotalRedFrames.setStatus(_A)
_AdGenPolicer24HrThresholdTable_Object=MibTable
adGenPolicer24HrThresholdTable=_AdGenPolicer24HrThresholdTable_Object((1,3,6,1,4,1,664,5,70,35,1,2,2))
if mibBuilder.loadTexts:adGenPolicer24HrThresholdTable.setStatus(_A)
_AdGenPolicer24HrThresholdEntry_Object=MibTableRow
adGenPolicer24HrThresholdEntry=_AdGenPolicer24HrThresholdEntry_Object((1,3,6,1,4,1,664,5,70,35,1,2,2,1))
adGenPolicer24HrThresholdEntry.setIndexNames((0,_C,_D),(0,_B,_L))
if mibBuilder.loadTexts:adGenPolicer24HrThresholdEntry.setStatus(_A)
_AdGenPolicer24HrThresholdDiscardsGreenFrames_Type=Integer32
_AdGenPolicer24HrThresholdDiscardsGreenFrames_Object=MibTableColumn
adGenPolicer24HrThresholdDiscardsGreenFrames=_AdGenPolicer24HrThresholdDiscardsGreenFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,2,1,1),_AdGenPolicer24HrThresholdDiscardsGreenFrames_Type())
adGenPolicer24HrThresholdDiscardsGreenFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer24HrThresholdDiscardsGreenFrames.setStatus(_A)
_AdGenPolicer24HrThresholdTotalGreenFrames_Type=Integer32
_AdGenPolicer24HrThresholdTotalGreenFrames_Object=MibTableColumn
adGenPolicer24HrThresholdTotalGreenFrames=_AdGenPolicer24HrThresholdTotalGreenFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,2,1,2),_AdGenPolicer24HrThresholdTotalGreenFrames_Type())
adGenPolicer24HrThresholdTotalGreenFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer24HrThresholdTotalGreenFrames.setStatus(_A)
_AdGenPolicer24HrThresholdDiscardsYellowFrames_Type=Integer32
_AdGenPolicer24HrThresholdDiscardsYellowFrames_Object=MibTableColumn
adGenPolicer24HrThresholdDiscardsYellowFrames=_AdGenPolicer24HrThresholdDiscardsYellowFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,2,1,3),_AdGenPolicer24HrThresholdDiscardsYellowFrames_Type())
adGenPolicer24HrThresholdDiscardsYellowFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer24HrThresholdDiscardsYellowFrames.setStatus(_A)
_AdGenPolicer24HrThresholdTotalYellowFrames_Type=Integer32
_AdGenPolicer24HrThresholdTotalYellowFrames_Object=MibTableColumn
adGenPolicer24HrThresholdTotalYellowFrames=_AdGenPolicer24HrThresholdTotalYellowFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,2,1,4),_AdGenPolicer24HrThresholdTotalYellowFrames_Type())
adGenPolicer24HrThresholdTotalYellowFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer24HrThresholdTotalYellowFrames.setStatus(_A)
_AdGenPolicer24HrThresholdTotalRedFrames_Type=Integer32
_AdGenPolicer24HrThresholdTotalRedFrames_Object=MibTableColumn
adGenPolicer24HrThresholdTotalRedFrames=_AdGenPolicer24HrThresholdTotalRedFrames_Object((1,3,6,1,4,1,664,5,70,35,1,2,2,1,5),_AdGenPolicer24HrThresholdTotalRedFrames_Type())
adGenPolicer24HrThresholdTotalRedFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenPolicer24HrThresholdTotalRedFrames.setStatus(_A)
_AdGenPolicerErrorTable_Object=MibTable
adGenPolicerErrorTable=_AdGenPolicerErrorTable_Object((1,3,6,1,4,1,664,5,70,35,1,3))
if mibBuilder.loadTexts:adGenPolicerErrorTable.setStatus(_A)
_AdGenPolicerErrorEntry_Object=MibTableRow
adGenPolicerErrorEntry=_AdGenPolicerErrorEntry_Object((1,3,6,1,4,1,664,5,70,35,1,3,1))
adGenPolicerErrorEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenPolicerErrorEntry.setStatus(_A)
_AdGenPolicerError_Type=DisplayString
_AdGenPolicerError_Object=MibTableColumn
adGenPolicerError=_AdGenPolicerError_Object((1,3,6,1,4,1,664,5,70,35,1,3,1,1),_AdGenPolicerError_Type())
adGenPolicerError.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerError.setStatus(_A)
_AdGenPolicerLookupTable_Object=MibTable
adGenPolicerLookupTable=_AdGenPolicerLookupTable_Object((1,3,6,1,4,1,664,5,70,35,1,4))
if mibBuilder.loadTexts:adGenPolicerLookupTable.setStatus(_A)
_AdGenPolicerLookupEntry_Object=MibTableRow
adGenPolicerLookupEntry=_AdGenPolicerLookupEntry_Object((1,3,6,1,4,1,664,5,70,35,1,4,1))
adGenPolicerLookupEntry.setIndexNames((0,_C,_D),(0,_B,_L))
if mibBuilder.loadTexts:adGenPolicerLookupEntry.setStatus(_A)
_AdGenPolicerActualCIR_Type=Integer32
_AdGenPolicerActualCIR_Object=MibTableColumn
adGenPolicerActualCIR=_AdGenPolicerActualCIR_Object((1,3,6,1,4,1,664,5,70,35,1,4,1,1),_AdGenPolicerActualCIR_Type())
adGenPolicerActualCIR.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerActualCIR.setStatus(_A)
_AdGenPolicerActualCBS_Type=Integer32
_AdGenPolicerActualCBS_Object=MibTableColumn
adGenPolicerActualCBS=_AdGenPolicerActualCBS_Object((1,3,6,1,4,1,664,5,70,35,1,4,1,2),_AdGenPolicerActualCBS_Type())
adGenPolicerActualCBS.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerActualCBS.setStatus(_A)
_AdGenPolicerActualEIR_Type=Integer32
_AdGenPolicerActualEIR_Object=MibTableColumn
adGenPolicerActualEIR=_AdGenPolicerActualEIR_Object((1,3,6,1,4,1,664,5,70,35,1,4,1,3),_AdGenPolicerActualEIR_Type())
adGenPolicerActualEIR.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerActualEIR.setStatus(_A)
_AdGenPolicerActualEBS_Type=Integer32
_AdGenPolicerActualEBS_Object=MibTableColumn
adGenPolicerActualEBS=_AdGenPolicerActualEBS_Object((1,3,6,1,4,1,664,5,70,35,1,4,1,4),_AdGenPolicerActualEBS_Type())
adGenPolicerActualEBS.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerActualEBS.setStatus(_A)
_AdGenPolicerProvNumberOfEVCMaps_Type=Integer32
_AdGenPolicerProvNumberOfEVCMaps_Object=MibTableColumn
adGenPolicerProvNumberOfEVCMaps=_AdGenPolicerProvNumberOfEVCMaps_Object((1,3,6,1,4,1,664,5,70,35,1,4,1,5),_AdGenPolicerProvNumberOfEVCMaps_Type())
adGenPolicerProvNumberOfEVCMaps.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerProvNumberOfEVCMaps.setStatus(_A)
_AdGenPolicerQualifiedNumberOfEVCMaps_Type=Integer32
_AdGenPolicerQualifiedNumberOfEVCMaps_Object=MibTableColumn
adGenPolicerQualifiedNumberOfEVCMaps=_AdGenPolicerQualifiedNumberOfEVCMaps_Object((1,3,6,1,4,1,664,5,70,35,1,4,1,6),_AdGenPolicerQualifiedNumberOfEVCMaps_Type())
adGenPolicerQualifiedNumberOfEVCMaps.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerQualifiedNumberOfEVCMaps.setStatus(_A)
_AdGenPolicerEVCMapLookupTable_Object=MibTable
adGenPolicerEVCMapLookupTable=_AdGenPolicerEVCMapLookupTable_Object((1,3,6,1,4,1,664,5,70,35,1,5))
if mibBuilder.loadTexts:adGenPolicerEVCMapLookupTable.setStatus(_A)
_AdGenPolicerEVCMapLookupEntry_Object=MibTableRow
adGenPolicerEVCMapLookupEntry=_AdGenPolicerEVCMapLookupEntry_Object((1,3,6,1,4,1,664,5,70,35,1,5,1))
adGenPolicerEVCMapLookupEntry.setIndexNames((0,_C,_D),(0,_B,_O),(0,_B,_S))
if mibBuilder.loadTexts:adGenPolicerEVCMapLookupEntry.setStatus(_A)
class _AdGenPolicerFixedLengthName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(50,50));fixedLength=50
_AdGenPolicerFixedLengthName_Type.__name__=_P
_AdGenPolicerFixedLengthName_Object=MibTableColumn
adGenPolicerFixedLengthName=_AdGenPolicerFixedLengthName_Object((1,3,6,1,4,1,664,5,70,35,1,5,1,1),_AdGenPolicerFixedLengthName_Type())
adGenPolicerFixedLengthName.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenPolicerFixedLengthName.setStatus(_A)
_AdGenPolicerEVCMapLookupIndex_Type=Integer32
_AdGenPolicerEVCMapLookupIndex_Object=MibTableColumn
adGenPolicerEVCMapLookupIndex=_AdGenPolicerEVCMapLookupIndex_Object((1,3,6,1,4,1,664,5,70,35,1,5,1,2),_AdGenPolicerEVCMapLookupIndex_Type())
adGenPolicerEVCMapLookupIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenPolicerEVCMapLookupIndex.setStatus(_A)
_AdGenPolicerEVCMapLookupName_Type=DisplayString
_AdGenPolicerEVCMapLookupName_Object=MibTableColumn
adGenPolicerEVCMapLookupName=_AdGenPolicerEVCMapLookupName_Object((1,3,6,1,4,1,664,5,70,35,1,5,1,3),_AdGenPolicerEVCMapLookupName_Type())
adGenPolicerEVCMapLookupName.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerEVCMapLookupName.setStatus(_A)
_AdGenPolicerQualifiedEVCMapLookupTable_Object=MibTable
adGenPolicerQualifiedEVCMapLookupTable=_AdGenPolicerQualifiedEVCMapLookupTable_Object((1,3,6,1,4,1,664,5,70,35,1,6))
if mibBuilder.loadTexts:adGenPolicerQualifiedEVCMapLookupTable.setStatus(_A)
_AdGenPolicerQualifiedEVCMapLookupEntry_Object=MibTableRow
adGenPolicerQualifiedEVCMapLookupEntry=_AdGenPolicerQualifiedEVCMapLookupEntry_Object((1,3,6,1,4,1,664,5,70,35,1,6,1))
adGenPolicerQualifiedEVCMapLookupEntry.setIndexNames((0,_C,_D),(0,_B,_O),(0,_B,_T))
if mibBuilder.loadTexts:adGenPolicerQualifiedEVCMapLookupEntry.setStatus(_A)
_AdGenPolicerQualifiedEVCMapLookupIndex_Type=Integer32
_AdGenPolicerQualifiedEVCMapLookupIndex_Object=MibTableColumn
adGenPolicerQualifiedEVCMapLookupIndex=_AdGenPolicerQualifiedEVCMapLookupIndex_Object((1,3,6,1,4,1,664,5,70,35,1,6,1,1),_AdGenPolicerQualifiedEVCMapLookupIndex_Type())
adGenPolicerQualifiedEVCMapLookupIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenPolicerQualifiedEVCMapLookupIndex.setStatus(_A)
_AdGenPolicerQualifiedEVCMapLookupName_Type=DisplayString
_AdGenPolicerQualifiedEVCMapLookupName_Object=MibTableColumn
adGenPolicerQualifiedEVCMapLookupName=_AdGenPolicerQualifiedEVCMapLookupName_Object((1,3,6,1,4,1,664,5,70,35,1,6,1,2),_AdGenPolicerQualifiedEVCMapLookupName_Type())
adGenPolicerQualifiedEVCMapLookupName.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerQualifiedEVCMapLookupName.setStatus(_A)
class _AdGenPolicerQualifiedEVCMapLookupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('notApplied',2),('applied',3)))
_AdGenPolicerQualifiedEVCMapLookupStatus_Type.__name__=_M
_AdGenPolicerQualifiedEVCMapLookupStatus_Object=MibTableColumn
adGenPolicerQualifiedEVCMapLookupStatus=_AdGenPolicerQualifiedEVCMapLookupStatus_Object((1,3,6,1,4,1,664,5,70,35,1,6,1,3),_AdGenPolicerQualifiedEVCMapLookupStatus_Type())
adGenPolicerQualifiedEVCMapLookupStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenPolicerQualifiedEVCMapLookupStatus.setStatus(_A)
_AdGenPolicerAlarm_ObjectIdentity=ObjectIdentity
adGenPolicerAlarm=_AdGenPolicerAlarm_ObjectIdentity((1,3,6,1,4,1,664,5,70,35,100))
_AdGenPolicerAlarmEvents_ObjectIdentity=ObjectIdentity
adGenPolicerAlarmEvents=_AdGenPolicerAlarmEvents_ObjectIdentity((1,3,6,1,4,1,664,5,70,35,100,0))
adGenPolicer15MinThresGreenTotalAlarm=NotificationType((1,3,6,1,4,1,664,5,70,35,100,0,1))
adGenPolicer15MinThresGreenTotalAlarm.setObjects(*((_H,_I),(_J,_K),(_C,_D),(_B,_U)))
if mibBuilder.loadTexts:adGenPolicer15MinThresGreenTotalAlarm.setStatus(_A)
adGenPolicer15MinThresYellowTotalAlarm=NotificationType((1,3,6,1,4,1,664,5,70,35,100,0,3))
adGenPolicer15MinThresYellowTotalAlarm.setObjects(*((_H,_I),(_J,_K),(_C,_D),(_B,_V)))
if mibBuilder.loadTexts:adGenPolicer15MinThresYellowTotalAlarm.setStatus(_A)
adGenPolicer15MinThresRedTotalAlarm=NotificationType((1,3,6,1,4,1,664,5,70,35,100,0,5))
adGenPolicer15MinThresRedTotalAlarm.setObjects(*((_H,_I),(_J,_K),(_C,_D),(_B,_W)))
if mibBuilder.loadTexts:adGenPolicer15MinThresRedTotalAlarm.setStatus(_A)
adGenPolicer24HrThresGreenTotalAlarm=NotificationType((1,3,6,1,4,1,664,5,70,35,100,0,7))
adGenPolicer24HrThresGreenTotalAlarm.setObjects(*((_H,_I),(_J,_K),(_C,_D),(_B,_X)))
if mibBuilder.loadTexts:adGenPolicer24HrThresGreenTotalAlarm.setStatus(_A)
adGenPolicer24HrThresYellowTotalAlarm=NotificationType((1,3,6,1,4,1,664,5,70,35,100,0,9))
adGenPolicer24HrThresYellowTotalAlarm.setObjects(*((_H,_I),(_J,_K),(_C,_D),(_B,_Y)))
if mibBuilder.loadTexts:adGenPolicer24HrThresYellowTotalAlarm.setStatus(_A)
adGenPolicer24HrThresRedTotalAlarm=NotificationType((1,3,6,1,4,1,664,5,70,35,100,0,11))
adGenPolicer24HrThresRedTotalAlarm.setObjects(*((_H,_I),(_J,_K),(_C,_D),(_B,_Z)))
if mibBuilder.loadTexts:adGenPolicer24HrThresRedTotalAlarm.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenPolicerEvents':adGenPolicerEvents,'adGenPolicerProvisioning':adGenPolicerProvisioning,'adGenPolicerTable':adGenPolicerTable,'adGenPolicerEntry':adGenPolicerEntry,_L:adGenPolicerName,'adGenPolicerRowStatus':adGenPolicerRowStatus,'adGenPolicerStatus':adGenPolicerStatus,'adGenPolicerOperStatus':adGenPolicerOperStatus,'adGenPolicerCIR':adGenPolicerCIR,'adGenPolicerCBS':adGenPolicerCBS,'adGenPolicerEIR':adGenPolicerEIR,'adGenPolicerEIRNoLimit':adGenPolicerEIRNoLimit,'adGenPolicerEBS':adGenPolicerEBS,'adGenPolicerMode':adGenPolicerMode,'adGenPolicerUNIPort':adGenPolicerUNIPort,'adGenPolicerEVCName':adGenPolicerEVCName,'adGenPolicerMEVCName':adGenPolicerMEVCName,'adGenPolicerCEVlanPriority':adGenPolicerCEVlanPriority,'adGenPolicerAddEvcMap':adGenPolicerAddEvcMap,'adGenPolicerRemoveEvcMap':adGenPolicerRemoveEvcMap,'adGenPolicerLastError':adGenPolicerLastError,'adGenPolicerThresholds':adGenPolicerThresholds,'adGenPolicer15MinThresholdTable':adGenPolicer15MinThresholdTable,'adGenPolicer15MinThresholdEntry':adGenPolicer15MinThresholdEntry,'adGenPolicer15MinThresholdDiscardsGreenFrames':adGenPolicer15MinThresholdDiscardsGreenFrames,_U:adGenPolicer15MinThresholdTotalGreenFrames,'adGenPolicer15MinThresholdDiscardsYellowFrames':adGenPolicer15MinThresholdDiscardsYellowFrames,_V:adGenPolicer15MinThresholdTotalYellowFrames,_W:adGenPolicer15MinThresholdTotalRedFrames,'adGenPolicer24HrThresholdTable':adGenPolicer24HrThresholdTable,'adGenPolicer24HrThresholdEntry':adGenPolicer24HrThresholdEntry,'adGenPolicer24HrThresholdDiscardsGreenFrames':adGenPolicer24HrThresholdDiscardsGreenFrames,_X:adGenPolicer24HrThresholdTotalGreenFrames,'adGenPolicer24HrThresholdDiscardsYellowFrames':adGenPolicer24HrThresholdDiscardsYellowFrames,_Y:adGenPolicer24HrThresholdTotalYellowFrames,_Z:adGenPolicer24HrThresholdTotalRedFrames,'adGenPolicerErrorTable':adGenPolicerErrorTable,'adGenPolicerErrorEntry':adGenPolicerErrorEntry,'adGenPolicerError':adGenPolicerError,'adGenPolicerLookupTable':adGenPolicerLookupTable,'adGenPolicerLookupEntry':adGenPolicerLookupEntry,'adGenPolicerActualCIR':adGenPolicerActualCIR,'adGenPolicerActualCBS':adGenPolicerActualCBS,'adGenPolicerActualEIR':adGenPolicerActualEIR,'adGenPolicerActualEBS':adGenPolicerActualEBS,'adGenPolicerProvNumberOfEVCMaps':adGenPolicerProvNumberOfEVCMaps,'adGenPolicerQualifiedNumberOfEVCMaps':adGenPolicerQualifiedNumberOfEVCMaps,'adGenPolicerEVCMapLookupTable':adGenPolicerEVCMapLookupTable,'adGenPolicerEVCMapLookupEntry':adGenPolicerEVCMapLookupEntry,_O:adGenPolicerFixedLengthName,_S:adGenPolicerEVCMapLookupIndex,'adGenPolicerEVCMapLookupName':adGenPolicerEVCMapLookupName,'adGenPolicerQualifiedEVCMapLookupTable':adGenPolicerQualifiedEVCMapLookupTable,'adGenPolicerQualifiedEVCMapLookupEntry':adGenPolicerQualifiedEVCMapLookupEntry,_T:adGenPolicerQualifiedEVCMapLookupIndex,'adGenPolicerQualifiedEVCMapLookupName':adGenPolicerQualifiedEVCMapLookupName,'adGenPolicerQualifiedEVCMapLookupStatus':adGenPolicerQualifiedEVCMapLookupStatus,'adGenPolicerAlarm':adGenPolicerAlarm,'adGenPolicerAlarmEvents':adGenPolicerAlarmEvents,'adGenPolicer15MinThresGreenTotalAlarm':adGenPolicer15MinThresGreenTotalAlarm,'adGenPolicer15MinThresYellowTotalAlarm':adGenPolicer15MinThresYellowTotalAlarm,'adGenPolicer15MinThresRedTotalAlarm':adGenPolicer15MinThresRedTotalAlarm,'adGenPolicer24HrThresGreenTotalAlarm':adGenPolicer24HrThresGreenTotalAlarm,'adGenPolicer24HrThresYellowTotalAlarm':adGenPolicer24HrThresYellowTotalAlarm,'adGenPolicer24HrThresRedTotalAlarm':adGenPolicer24HrThresRedTotalAlarm,'adGenPolicerMIB':adGenPolicerMIB})