_p='pdnAtmIfConfExtIngressLineRateAlarmClear'
_o='pdnAtmIfConfExtIngressLineRateAlarmSet'
_n='pdnAtmIfConfExtVclNoBandwidthAvail'
_m='pdnAtmIfConfExtVplNoBandwidthAvail'
_l='pdnAtmIfConfExtEgressLineRateAlarmClear'
_k='pdnAtmIfConfExtEgressLineRateAlarmSet'
_j='pdnAtmIfConfExtExcessInvalidCellsAlarm'
_i='pdnAal5VccExtOutPDUs'
_h='pdnAal5VccExtInPDUs'
_g='pdnAtmTrafficShaping'
_f='pdnAtmTrafficPolicing'
_e='pdnAtmTrafficDescrParamName'
_d='pdnAtmIfConfExtRateShape'
_c='pdnAtmIfConfExtBandwidthUtilUbrAssigned'
_b='pdnAtmIfConfExtBandwidthUtilUbrReserved'
_a='pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned'
_Z='pdnAtmIfConfExtBandwidthUtilVbrNrtReserved'
_Y='pdnAtmIfConfExtBandwidthUtilVbrRtAssigned'
_X='pdnAtmIfConfExtBandwidthUtilVbrRtReserved'
_W='pdnAtmIfConfExtBandwidthUtilCbrAssigned'
_V='pdnAtmIfConfExtBandwidthUtilCbrReserved'
_U='pdnAtmIfConfExtOcdEventThreshold'
_T='pdnAtmIfConfExtHecErrorThreshold'
_S='pdnAtmIfConfExtVbrNrtBandwidthUtil'
_R='pdnAtmIfConfExtVbrRtBandwidthUtil'
_Q='pdnAal5VccExtEntry'
_P='pdnAtmTrafficDescrParamExtEntry'
_O='pdnAtmIfConfExtEntry'
_N='DisplayString'
_M='ifOperStatus'
_L='atmVpCrossConnectAdminStatus'
_K='atmVcCrossConnectAdminStatus'
_J='pdnAtmIfConfExtUnknownCellThreshold'
_I='read-create'
_H='ATM-MIB'
_G='ifIndex'
_F='read-only'
_E='IF-MIB'
_D='Integer32'
_C='read-write'
_B='PDN-ATMEXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aal5VccEntry,atmInterfaceConfEntry,atmTrafficDescrParamEntry,atmVcCrossConnectAdminStatus,atmVpCrossConnectAdminStatus=mibBuilder.importSymbols(_H,'aal5VccEntry','atmInterfaceConfEntry','atmTrafficDescrParamEntry',_K,_L)
ifIndex,ifOperStatus=mibBuilder.importSymbols(_E,_G,_M)
pdnAtm,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnAtm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention','TruthValue')
pdnAtmExtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5))
if mibBuilder.loadTexts:pdnAtmExtMIB.setRevisions(('2003-05-15 00:00','2003-05-11 00:00','1970-01-01 00:00','2003-03-31 00:00','2002-03-27 00:00','2000-12-29 00:00','2000-12-01 00:00','2000-07-06 00:00','2000-04-28 00:00','2000-03-11 00:00','2000-02-18 00:00'))
_PdnAtmExtMIBObjects_ObjectIdentity=ObjectIdentity
pdnAtmExtMIBObjects=_PdnAtmExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5,1))
_PdnAtmIfConfExtTable_Object=MibTable
pdnAtmIfConfExtTable=_PdnAtmIfConfExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1))
if mibBuilder.loadTexts:pdnAtmIfConfExtTable.setStatus(_A)
_PdnAtmIfConfExtEntry_Object=MibTableRow
pdnAtmIfConfExtEntry=_PdnAtmIfConfExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1))
if mibBuilder.loadTexts:pdnAtmIfConfExtEntry.setStatus(_A)
class _PdnAtmIfConfExtVbrRtBandwidthUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_PdnAtmIfConfExtVbrRtBandwidthUtil_Type.__name__=_D
_PdnAtmIfConfExtVbrRtBandwidthUtil_Object=MibTableColumn
pdnAtmIfConfExtVbrRtBandwidthUtil=_PdnAtmIfConfExtVbrRtBandwidthUtil_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,1),_PdnAtmIfConfExtVbrRtBandwidthUtil_Type())
pdnAtmIfConfExtVbrRtBandwidthUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtVbrRtBandwidthUtil.setStatus(_A)
class _PdnAtmIfConfExtVbrNrtBandwidthUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_PdnAtmIfConfExtVbrNrtBandwidthUtil_Type.__name__=_D
_PdnAtmIfConfExtVbrNrtBandwidthUtil_Object=MibTableColumn
pdnAtmIfConfExtVbrNrtBandwidthUtil=_PdnAtmIfConfExtVbrNrtBandwidthUtil_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,2),_PdnAtmIfConfExtVbrNrtBandwidthUtil_Type())
pdnAtmIfConfExtVbrNrtBandwidthUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtVbrNrtBandwidthUtil.setStatus(_A)
class _PdnAtmIfConfExtHecErrorThreshold_Type(Integer32):defaultValue=100
_PdnAtmIfConfExtHecErrorThreshold_Type.__name__=_D
_PdnAtmIfConfExtHecErrorThreshold_Object=MibTableColumn
pdnAtmIfConfExtHecErrorThreshold=_PdnAtmIfConfExtHecErrorThreshold_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,3),_PdnAtmIfConfExtHecErrorThreshold_Type())
pdnAtmIfConfExtHecErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtHecErrorThreshold.setStatus(_A)
class _PdnAtmIfConfExtUnknownCellThreshold_Type(Integer32):defaultValue=10
_PdnAtmIfConfExtUnknownCellThreshold_Type.__name__=_D
_PdnAtmIfConfExtUnknownCellThreshold_Object=MibTableColumn
pdnAtmIfConfExtUnknownCellThreshold=_PdnAtmIfConfExtUnknownCellThreshold_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,4),_PdnAtmIfConfExtUnknownCellThreshold_Type())
pdnAtmIfConfExtUnknownCellThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtUnknownCellThreshold.setStatus(_A)
class _PdnAtmIfConfExtOcdEventThreshold_Type(Integer32):defaultValue=0
_PdnAtmIfConfExtOcdEventThreshold_Type.__name__=_D
_PdnAtmIfConfExtOcdEventThreshold_Object=MibTableColumn
pdnAtmIfConfExtOcdEventThreshold=_PdnAtmIfConfExtOcdEventThreshold_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,5),_PdnAtmIfConfExtOcdEventThreshold_Type())
pdnAtmIfConfExtOcdEventThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtOcdEventThreshold.setStatus(_A)
_PdnAtmIfConfExtBandwidthUtilCbrReserved_Type=Integer32
_PdnAtmIfConfExtBandwidthUtilCbrReserved_Object=MibTableColumn
pdnAtmIfConfExtBandwidthUtilCbrReserved=_PdnAtmIfConfExtBandwidthUtilCbrReserved_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,6),_PdnAtmIfConfExtBandwidthUtilCbrReserved_Type())
pdnAtmIfConfExtBandwidthUtilCbrReserved.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtBandwidthUtilCbrReserved.setStatus(_A)
_PdnAtmIfConfExtBandwidthUtilCbrAssigned_Type=Integer32
_PdnAtmIfConfExtBandwidthUtilCbrAssigned_Object=MibTableColumn
pdnAtmIfConfExtBandwidthUtilCbrAssigned=_PdnAtmIfConfExtBandwidthUtilCbrAssigned_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,7),_PdnAtmIfConfExtBandwidthUtilCbrAssigned_Type())
pdnAtmIfConfExtBandwidthUtilCbrAssigned.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAtmIfConfExtBandwidthUtilCbrAssigned.setStatus(_A)
_PdnAtmIfConfExtBandwidthUtilVbrRtReserved_Type=Integer32
_PdnAtmIfConfExtBandwidthUtilVbrRtReserved_Object=MibTableColumn
pdnAtmIfConfExtBandwidthUtilVbrRtReserved=_PdnAtmIfConfExtBandwidthUtilVbrRtReserved_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,8),_PdnAtmIfConfExtBandwidthUtilVbrRtReserved_Type())
pdnAtmIfConfExtBandwidthUtilVbrRtReserved.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtBandwidthUtilVbrRtReserved.setStatus(_A)
_PdnAtmIfConfExtBandwidthUtilVbrRtAssigned_Type=Integer32
_PdnAtmIfConfExtBandwidthUtilVbrRtAssigned_Object=MibTableColumn
pdnAtmIfConfExtBandwidthUtilVbrRtAssigned=_PdnAtmIfConfExtBandwidthUtilVbrRtAssigned_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,9),_PdnAtmIfConfExtBandwidthUtilVbrRtAssigned_Type())
pdnAtmIfConfExtBandwidthUtilVbrRtAssigned.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAtmIfConfExtBandwidthUtilVbrRtAssigned.setStatus(_A)
_PdnAtmIfConfExtBandwidthUtilVbrNrtReserved_Type=Integer32
_PdnAtmIfConfExtBandwidthUtilVbrNrtReserved_Object=MibTableColumn
pdnAtmIfConfExtBandwidthUtilVbrNrtReserved=_PdnAtmIfConfExtBandwidthUtilVbrNrtReserved_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,10),_PdnAtmIfConfExtBandwidthUtilVbrNrtReserved_Type())
pdnAtmIfConfExtBandwidthUtilVbrNrtReserved.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtBandwidthUtilVbrNrtReserved.setStatus(_A)
_PdnAtmIfConfExtBandwidthUtilVbrNrtAssigned_Type=Integer32
_PdnAtmIfConfExtBandwidthUtilVbrNrtAssigned_Object=MibTableColumn
pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned=_PdnAtmIfConfExtBandwidthUtilVbrNrtAssigned_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,11),_PdnAtmIfConfExtBandwidthUtilVbrNrtAssigned_Type())
pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned.setStatus(_A)
_PdnAtmIfConfExtBandwidthUtilUbrReserved_Type=Integer32
_PdnAtmIfConfExtBandwidthUtilUbrReserved_Object=MibTableColumn
pdnAtmIfConfExtBandwidthUtilUbrReserved=_PdnAtmIfConfExtBandwidthUtilUbrReserved_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,12),_PdnAtmIfConfExtBandwidthUtilUbrReserved_Type())
pdnAtmIfConfExtBandwidthUtilUbrReserved.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtBandwidthUtilUbrReserved.setStatus(_A)
_PdnAtmIfConfExtBandwidthUtilUbrAssigned_Type=Integer32
_PdnAtmIfConfExtBandwidthUtilUbrAssigned_Object=MibTableColumn
pdnAtmIfConfExtBandwidthUtilUbrAssigned=_PdnAtmIfConfExtBandwidthUtilUbrAssigned_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,13),_PdnAtmIfConfExtBandwidthUtilUbrAssigned_Type())
pdnAtmIfConfExtBandwidthUtilUbrAssigned.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAtmIfConfExtBandwidthUtilUbrAssigned.setStatus(_A)
class _PdnAtmIfConfExtRateShape_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,46080))
_PdnAtmIfConfExtRateShape_Type.__name__=_D
_PdnAtmIfConfExtRateShape_Object=MibTableColumn
pdnAtmIfConfExtRateShape=_PdnAtmIfConfExtRateShape_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,1,1,14),_PdnAtmIfConfExtRateShape_Type())
pdnAtmIfConfExtRateShape.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmIfConfExtRateShape.setStatus(_A)
if mibBuilder.loadTexts:pdnAtmIfConfExtRateShape.setUnits('Kbps')
_PdnAtmTrafficDescrParamExtTable_Object=MibTable
pdnAtmTrafficDescrParamExtTable=_PdnAtmTrafficDescrParamExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,2))
if mibBuilder.loadTexts:pdnAtmTrafficDescrParamExtTable.setStatus(_A)
_PdnAtmTrafficDescrParamExtEntry_Object=MibTableRow
pdnAtmTrafficDescrParamExtEntry=_PdnAtmTrafficDescrParamExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,2,1))
if mibBuilder.loadTexts:pdnAtmTrafficDescrParamExtEntry.setStatus(_A)
class _PdnAtmTrafficDescrParamName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_PdnAtmTrafficDescrParamName_Type.__name__=_N
_PdnAtmTrafficDescrParamName_Object=MibTableColumn
pdnAtmTrafficDescrParamName=_PdnAtmTrafficDescrParamName_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,2,1,1),_PdnAtmTrafficDescrParamName_Type())
pdnAtmTrafficDescrParamName.setMaxAccess(_I)
if mibBuilder.loadTexts:pdnAtmTrafficDescrParamName.setStatus(_A)
_PdnAtmTrafficPolicing_Type=TruthValue
_PdnAtmTrafficPolicing_Object=MibTableColumn
pdnAtmTrafficPolicing=_PdnAtmTrafficPolicing_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,2,1,2),_PdnAtmTrafficPolicing_Type())
pdnAtmTrafficPolicing.setMaxAccess(_I)
if mibBuilder.loadTexts:pdnAtmTrafficPolicing.setStatus(_A)
_PdnAtmTrafficShaping_Type=TruthValue
_PdnAtmTrafficShaping_Object=MibTableColumn
pdnAtmTrafficShaping=_PdnAtmTrafficShaping_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,2,1,3),_PdnAtmTrafficShaping_Type())
pdnAtmTrafficShaping.setMaxAccess(_I)
if mibBuilder.loadTexts:pdnAtmTrafficShaping.setStatus(_A)
_PdnAal5VccExtTable_Object=MibTable
pdnAal5VccExtTable=_PdnAal5VccExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,3))
if mibBuilder.loadTexts:pdnAal5VccExtTable.setStatus(_A)
_PdnAal5VccExtEntry_Object=MibTableRow
pdnAal5VccExtEntry=_PdnAal5VccExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,3,1))
if mibBuilder.loadTexts:pdnAal5VccExtEntry.setStatus(_A)
_PdnAal5VccExtOutPDUs_Type=Unsigned32
_PdnAal5VccExtOutPDUs_Object=MibTableColumn
pdnAal5VccExtOutPDUs=_PdnAal5VccExtOutPDUs_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,3,1,1),_PdnAal5VccExtOutPDUs_Type())
pdnAal5VccExtOutPDUs.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAal5VccExtOutPDUs.setStatus(_A)
_PdnAal5VccExtInPDUs_Type=Unsigned32
_PdnAal5VccExtInPDUs_Object=MibTableColumn
pdnAal5VccExtInPDUs=_PdnAal5VccExtInPDUs_Object((1,3,6,1,4,1,1795,2,24,2,6,11,5,1,3,1,2),_PdnAal5VccExtInPDUs_Type())
pdnAal5VccExtInPDUs.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAal5VccExtInPDUs.setStatus(_A)
_PdnAtmExtMIBTraps_ObjectIdentity=ObjectIdentity
pdnAtmExtMIBTraps=_PdnAtmExtMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5,2))
_PdnAtmExtMIBTrapPrefix_ObjectIdentity=ObjectIdentity
pdnAtmExtMIBTrapPrefix=_PdnAtmExtMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5,2,0))
_PdnAtmExtMIBConformance_ObjectIdentity=ObjectIdentity
pdnAtmExtMIBConformance=_PdnAtmExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5,3))
_PdnAtmExtMibCompliances_ObjectIdentity=ObjectIdentity
pdnAtmExtMibCompliances=_PdnAtmExtMibCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5,3,1))
_PdnAtmExtMibGroups_ObjectIdentity=ObjectIdentity
pdnAtmExtMibGroups=_PdnAtmExtMibGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5,3,2))
_PdnAtmExtMIBTrafficDescriptorTypes_ObjectIdentity=ObjectIdentity
pdnAtmExtMIBTrafficDescriptorTypes=_PdnAtmExtMIBTrafficDescriptorTypes_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5,4))
_PdnAtmNoClpTaggingNoScrCdvtMdcr_ObjectIdentity=ObjectIdentity
pdnAtmNoClpTaggingNoScrCdvtMdcr=_PdnAtmNoClpTaggingNoScrCdvtMdcr_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5,4,1))
if mibBuilder.loadTexts:pdnAtmNoClpTaggingNoScrCdvtMdcr.setStatus(_A)
_PdnAtmNoClpNoScrCdvtMdcr_ObjectIdentity=ObjectIdentity
pdnAtmNoClpNoScrCdvtMdcr=_PdnAtmNoClpNoScrCdvtMdcr_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,5,4,2))
if mibBuilder.loadTexts:pdnAtmNoClpNoScrCdvtMdcr.setStatus(_A)
atmInterfaceConfEntry.registerAugmentions((_B,_O))
pdnAtmIfConfExtEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
atmTrafficDescrParamEntry.registerAugmentions((_B,_P))
pdnAtmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
aal5VccEntry.registerAugmentions((_B,_Q))
pdnAal5VccExtEntry.setIndexNames(*aal5VccEntry.getIndexNames())
pdnAtmIfConfExtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,11,5,3,2,1))
pdnAtmIfConfExtGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_J),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:pdnAtmIfConfExtGroup.setStatus(_A)
pdnAtmTrafficDescrParamExtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,11,5,3,2,2))
pdnAtmTrafficDescrParamExtGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:pdnAtmTrafficDescrParamExtGroup.setStatus(_A)
pdnAal5VccExtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,11,5,3,2,3))
pdnAal5VccExtGroup.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:pdnAal5VccExtGroup.setStatus(_A)
pdnAtmIfConfExtExcessInvalidCellsAlarm=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,11,5,2,0,1))
pdnAtmIfConfExtExcessInvalidCellsAlarm.setObjects(*((_E,_M),(_B,_J)))
if mibBuilder.loadTexts:pdnAtmIfConfExtExcessInvalidCellsAlarm.setStatus(_A)
pdnAtmIfConfExtEgressLineRateAlarmSet=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,11,5,2,0,2))
pdnAtmIfConfExtEgressLineRateAlarmSet.setObjects((_E,_G))
if mibBuilder.loadTexts:pdnAtmIfConfExtEgressLineRateAlarmSet.setStatus(_A)
pdnAtmIfConfExtVplNoBandwidthAvail=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,11,5,2,0,3))
pdnAtmIfConfExtVplNoBandwidthAvail.setObjects((_H,_L))
if mibBuilder.loadTexts:pdnAtmIfConfExtVplNoBandwidthAvail.setStatus(_A)
pdnAtmIfConfExtVclNoBandwidthAvail=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,11,5,2,0,4))
pdnAtmIfConfExtVclNoBandwidthAvail.setObjects((_H,_K))
if mibBuilder.loadTexts:pdnAtmIfConfExtVclNoBandwidthAvail.setStatus(_A)
pdnAtmIfConfExtIngressLineRateAlarmSet=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,11,5,2,0,5))
pdnAtmIfConfExtIngressLineRateAlarmSet.setObjects((_E,_G))
if mibBuilder.loadTexts:pdnAtmIfConfExtIngressLineRateAlarmSet.setStatus(_A)
pdnAtmIfConfExtEgressLineRateAlarmClear=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,11,5,2,0,102))
pdnAtmIfConfExtEgressLineRateAlarmClear.setObjects((_E,_G))
if mibBuilder.loadTexts:pdnAtmIfConfExtEgressLineRateAlarmClear.setStatus(_A)
pdnAtmIfConfExtIngressLineRateAlarmClear=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,11,5,2,0,105))
pdnAtmIfConfExtIngressLineRateAlarmClear.setObjects((_E,_G))
if mibBuilder.loadTexts:pdnAtmIfConfExtIngressLineRateAlarmClear.setStatus(_A)
pdnAtmExtNotificationGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,6,11,5,3,2,4))
pdnAtmExtNotificationGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:pdnAtmExtNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnAtmExtMIB':pdnAtmExtMIB,'pdnAtmExtMIBObjects':pdnAtmExtMIBObjects,'pdnAtmIfConfExtTable':pdnAtmIfConfExtTable,_O:pdnAtmIfConfExtEntry,_R:pdnAtmIfConfExtVbrRtBandwidthUtil,_S:pdnAtmIfConfExtVbrNrtBandwidthUtil,_T:pdnAtmIfConfExtHecErrorThreshold,_J:pdnAtmIfConfExtUnknownCellThreshold,_U:pdnAtmIfConfExtOcdEventThreshold,_V:pdnAtmIfConfExtBandwidthUtilCbrReserved,_W:pdnAtmIfConfExtBandwidthUtilCbrAssigned,_X:pdnAtmIfConfExtBandwidthUtilVbrRtReserved,_Y:pdnAtmIfConfExtBandwidthUtilVbrRtAssigned,_Z:pdnAtmIfConfExtBandwidthUtilVbrNrtReserved,_a:pdnAtmIfConfExtBandwidthUtilVbrNrtAssigned,_b:pdnAtmIfConfExtBandwidthUtilUbrReserved,_c:pdnAtmIfConfExtBandwidthUtilUbrAssigned,_d:pdnAtmIfConfExtRateShape,'pdnAtmTrafficDescrParamExtTable':pdnAtmTrafficDescrParamExtTable,_P:pdnAtmTrafficDescrParamExtEntry,_e:pdnAtmTrafficDescrParamName,_f:pdnAtmTrafficPolicing,_g:pdnAtmTrafficShaping,'pdnAal5VccExtTable':pdnAal5VccExtTable,_Q:pdnAal5VccExtEntry,_i:pdnAal5VccExtOutPDUs,_h:pdnAal5VccExtInPDUs,'pdnAtmExtMIBTraps':pdnAtmExtMIBTraps,'pdnAtmExtMIBTrapPrefix':pdnAtmExtMIBTrapPrefix,_j:pdnAtmIfConfExtExcessInvalidCellsAlarm,_k:pdnAtmIfConfExtEgressLineRateAlarmSet,_m:pdnAtmIfConfExtVplNoBandwidthAvail,_n:pdnAtmIfConfExtVclNoBandwidthAvail,_o:pdnAtmIfConfExtIngressLineRateAlarmSet,_l:pdnAtmIfConfExtEgressLineRateAlarmClear,_p:pdnAtmIfConfExtIngressLineRateAlarmClear,'pdnAtmExtMIBConformance':pdnAtmExtMIBConformance,'pdnAtmExtMibCompliances':pdnAtmExtMibCompliances,'pdnAtmExtMibGroups':pdnAtmExtMibGroups,'pdnAtmIfConfExtGroup':pdnAtmIfConfExtGroup,'pdnAtmTrafficDescrParamExtGroup':pdnAtmTrafficDescrParamExtGroup,'pdnAal5VccExtGroup':pdnAal5VccExtGroup,'pdnAtmExtNotificationGroup':pdnAtmExtNotificationGroup,'pdnAtmExtMIBTrafficDescriptorTypes':pdnAtmExtMIBTrafficDescriptorTypes,'pdnAtmNoClpTaggingNoScrCdvtMdcr':pdnAtmNoClpTaggingNoScrCdvtMdcr,'pdnAtmNoClpNoScrCdvtMdcr':pdnAtmNoClpNoScrCdvtMdcr})