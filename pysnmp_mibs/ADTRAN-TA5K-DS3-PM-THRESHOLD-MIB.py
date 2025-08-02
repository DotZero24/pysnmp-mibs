_A9='adTA5kds3PMDayCSESThresholdCrossed'
_A8='adTA5kds3PMDayCESThresholdCrossed'
_A7='adTA5kds3PMDayCCVThresholdCrossed'
_A6='adTA5kds3PMDayLESThresholdCrossed'
_A5='adTA5kds3PMDayPCVThresholdCrossed'
_A4='adTA5kds3PMDayLCVThresholdCrossed'
_A3='adTA5kds3PMDayUASThresholdCrossed'
_A2='adTA5kds3PMDaySEFSThresholdCrossed'
_A1='adTA5kds3PMDayPSESThresholdCrossed'
_A0='adTA5kds3PMDayPESThresholdCrossed'
_z='adTA5kds3almQtrCSESThresholdCrossed'
_y='adTA5kds3almQtrCESThresholdCrossed'
_x='adTA5kds3almQtrCCVThresholdCrossed'
_w='adTA5kds3almQtrLESThresholdCrossed'
_v='adTA5kds3almQtrPCVThresholdCrossed'
_u='adTA5kds3almQtrLCVThresholdCrossed'
_t='adTA5kds3almQtrUASThresholdCrossed'
_s='adTA5kds3almQtrSEFSThresholdCrossed'
_r='adTA5kds3almQtrPSESThresholdCrossed'
_q='adTA5kds3almQtrPESThresholdCrossed'
_p='adTA5kds3AISTrapClear'
_o='adTA5kds3AISTrapActive'
_n='adTA5kds3RAITrapClear'
_m='adTA5kds3RAITrapActive'
_l='adTA5kds3LOFTrapClear'
_k='adTA5kds3LOFTrapActive'
_j='adTA5kds3LOSTrapClear'
_i='adTA5kds3LOSTrapActive'
_h='adTa5kDs3PMDayThresholdCSES'
_g='adTa5kDs3PMDayThresholdCES'
_f='adTa5kDs3PMDayThresholdCCV'
_e='adTa5kDs3PMDayThresholdLES'
_d='adTa5kDs3PMDayThresholdPCV'
_c='adTa5kDs3PMDayThresholdLCV'
_b='adTa5kDs3PMDayThresholdUAS'
_a='adTa5kDs3PMDayThresholdSEFS'
_Z='adTa5kDs3PMDayThresholdPSES'
_Y='adTa5kDs3PMDayThresholdPES'
_X='adTa5kDs3PMqtrThresholdCSESs'
_W='adTa5kDs3PMqtrThresholdCESs'
_V='adTa5kDs3PMqtrThresholdCCVs'
_U='adTa5kDs3PMqtrThresholdLESs'
_T='adTa5kDs3PMqtrThresholdPCVs'
_S='adTa5kDs3PMqtrThresholdLCVs'
_R='adTa5kDs3PMqtrThresholdUASs'
_Q='adTa5kDs3PMqtrThresholdSEFSs'
_P='adTa5kDs3PMqtrThresholdPSESs'
_O='adTa5kDs3PMqtrThresholdPESs'
_N='ifIndex'
_M='IF-MIB'
_L='adGenPortInfoIndex'
_K='read-write'
_J='adGenPortTrapIdentifier'
_I='sysName'
_H='SNMPv2-MIB'
_G='adTrapInformSeqNum'
_F='ADTRAN-GENTRAPINFORM-MIB'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='ADTRAN-GENPORT-MIB'
_B='ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortInfoIndex,adGenPortTrapIdentifier=mibBuilder.importSymbols(_C,_L,_J)
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adGenTa5kDs3,adGenTa5kDs3ID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kDs3','adGenTa5kDs3ID')
adTrapInformSeqNum,=mibBuilder.importSymbols(_F,_G)
adIdentity,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adMgmt','adProducts')
ifIndex,=mibBuilder.importSymbols(_M,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_H,_I)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adTa5kDs3PMThresholdModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,21,1))
_AdTA5kds3TrapsPrefix_ObjectIdentity=ObjectIdentity
adTA5kds3TrapsPrefix=_AdTA5kds3TrapsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,21,1))
_AdTA5kds3Traps_ObjectIdentity=ObjectIdentity
adTA5kds3Traps=_AdTA5kds3Traps_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,21,1,0))
_AdTA5kds3PMThreshold_ObjectIdentity=ObjectIdentity
adTA5kds3PMThreshold=_AdTA5kds3PMThreshold_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,21,2))
_AdTa5kDS3PMqtrThresholdTable_Object=MibTable
adTa5kDS3PMqtrThresholdTable=_AdTa5kDS3PMqtrThresholdTable_Object((1,3,6,1,4,1,664,5,67,1,21,2,1))
if mibBuilder.loadTexts:adTa5kDS3PMqtrThresholdTable.setStatus(_A)
_AdTa5kDS3PMqtrThresholdEntry_Object=MibTableRow
adTa5kDS3PMqtrThresholdEntry=_AdTa5kDS3PMqtrThresholdEntry_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1))
adTa5kDS3PMqtrThresholdEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:adTa5kDS3PMqtrThresholdEntry.setStatus(_A)
_AdTa5kDs3PMqtrThresholdPESs_Type=Integer32
_AdTa5kDs3PMqtrThresholdPESs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdPESs=_AdTa5kDs3PMqtrThresholdPESs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,1),_AdTa5kDs3PMqtrThresholdPESs_Type())
adTa5kDs3PMqtrThresholdPESs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdPESs.setStatus(_A)
_AdTa5kDs3PMqtrThresholdPSESs_Type=Integer32
_AdTa5kDs3PMqtrThresholdPSESs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdPSESs=_AdTa5kDs3PMqtrThresholdPSESs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,2),_AdTa5kDs3PMqtrThresholdPSESs_Type())
adTa5kDs3PMqtrThresholdPSESs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdPSESs.setStatus(_A)
_AdTa5kDs3PMqtrThresholdSEFSs_Type=Integer32
_AdTa5kDs3PMqtrThresholdSEFSs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdSEFSs=_AdTa5kDs3PMqtrThresholdSEFSs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,3),_AdTa5kDs3PMqtrThresholdSEFSs_Type())
adTa5kDs3PMqtrThresholdSEFSs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdSEFSs.setStatus(_A)
_AdTa5kDs3PMqtrThresholdUASs_Type=Integer32
_AdTa5kDs3PMqtrThresholdUASs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdUASs=_AdTa5kDs3PMqtrThresholdUASs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,4),_AdTa5kDs3PMqtrThresholdUASs_Type())
adTa5kDs3PMqtrThresholdUASs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdUASs.setStatus(_A)
_AdTa5kDs3PMqtrThresholdLCVs_Type=Integer32
_AdTa5kDs3PMqtrThresholdLCVs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdLCVs=_AdTa5kDs3PMqtrThresholdLCVs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,5),_AdTa5kDs3PMqtrThresholdLCVs_Type())
adTa5kDs3PMqtrThresholdLCVs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdLCVs.setStatus(_A)
_AdTa5kDs3PMqtrThresholdPCVs_Type=Integer32
_AdTa5kDs3PMqtrThresholdPCVs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdPCVs=_AdTa5kDs3PMqtrThresholdPCVs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,6),_AdTa5kDs3PMqtrThresholdPCVs_Type())
adTa5kDs3PMqtrThresholdPCVs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdPCVs.setStatus(_A)
_AdTa5kDs3PMqtrThresholdLESs_Type=Integer32
_AdTa5kDs3PMqtrThresholdLESs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdLESs=_AdTa5kDs3PMqtrThresholdLESs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,7),_AdTa5kDs3PMqtrThresholdLESs_Type())
adTa5kDs3PMqtrThresholdLESs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdLESs.setStatus(_A)
_AdTa5kDs3PMqtrThresholdCCVs_Type=Integer32
_AdTa5kDs3PMqtrThresholdCCVs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdCCVs=_AdTa5kDs3PMqtrThresholdCCVs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,8),_AdTa5kDs3PMqtrThresholdCCVs_Type())
adTa5kDs3PMqtrThresholdCCVs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdCCVs.setStatus(_A)
_AdTa5kDs3PMqtrThresholdCESs_Type=Integer32
_AdTa5kDs3PMqtrThresholdCESs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdCESs=_AdTa5kDs3PMqtrThresholdCESs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,9),_AdTa5kDs3PMqtrThresholdCESs_Type())
adTa5kDs3PMqtrThresholdCESs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdCESs.setStatus(_A)
_AdTa5kDs3PMqtrThresholdCSESs_Type=Integer32
_AdTa5kDs3PMqtrThresholdCSESs_Object=MibTableColumn
adTa5kDs3PMqtrThresholdCSESs=_AdTa5kDs3PMqtrThresholdCSESs_Object((1,3,6,1,4,1,664,5,67,1,21,2,1,1,10),_AdTa5kDs3PMqtrThresholdCSESs_Type())
adTa5kDs3PMqtrThresholdCSESs.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMqtrThresholdCSESs.setStatus(_A)
_AdTa5kDs3PMDayThresholdTable_Object=MibTable
adTa5kDs3PMDayThresholdTable=_AdTa5kDs3PMDayThresholdTable_Object((1,3,6,1,4,1,664,5,67,1,21,2,2))
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdTable.setStatus(_A)
_AdTa5kDs3PMDayThresholdEntry_Object=MibTableRow
adTa5kDs3PMDayThresholdEntry=_AdTa5kDs3PMDayThresholdEntry_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1))
adTa5kDs3PMDayThresholdEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdEntry.setStatus(_A)
_AdTa5kDs3PMDayThresholdPES_Type=Integer32
_AdTa5kDs3PMDayThresholdPES_Object=MibTableColumn
adTa5kDs3PMDayThresholdPES=_AdTa5kDs3PMDayThresholdPES_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,1),_AdTa5kDs3PMDayThresholdPES_Type())
adTa5kDs3PMDayThresholdPES.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdPES.setStatus(_A)
_AdTa5kDs3PMDayThresholdPSES_Type=Integer32
_AdTa5kDs3PMDayThresholdPSES_Object=MibTableColumn
adTa5kDs3PMDayThresholdPSES=_AdTa5kDs3PMDayThresholdPSES_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,2),_AdTa5kDs3PMDayThresholdPSES_Type())
adTa5kDs3PMDayThresholdPSES.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdPSES.setStatus(_A)
_AdTa5kDs3PMDayThresholdSEFS_Type=Integer32
_AdTa5kDs3PMDayThresholdSEFS_Object=MibTableColumn
adTa5kDs3PMDayThresholdSEFS=_AdTa5kDs3PMDayThresholdSEFS_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,3),_AdTa5kDs3PMDayThresholdSEFS_Type())
adTa5kDs3PMDayThresholdSEFS.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdSEFS.setStatus(_A)
_AdTa5kDs3PMDayThresholdUAS_Type=Integer32
_AdTa5kDs3PMDayThresholdUAS_Object=MibTableColumn
adTa5kDs3PMDayThresholdUAS=_AdTa5kDs3PMDayThresholdUAS_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,4),_AdTa5kDs3PMDayThresholdUAS_Type())
adTa5kDs3PMDayThresholdUAS.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdUAS.setStatus(_A)
_AdTa5kDs3PMDayThresholdLCV_Type=Integer32
_AdTa5kDs3PMDayThresholdLCV_Object=MibTableColumn
adTa5kDs3PMDayThresholdLCV=_AdTa5kDs3PMDayThresholdLCV_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,5),_AdTa5kDs3PMDayThresholdLCV_Type())
adTa5kDs3PMDayThresholdLCV.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdLCV.setStatus(_A)
_AdTa5kDs3PMDayThresholdPCV_Type=Integer32
_AdTa5kDs3PMDayThresholdPCV_Object=MibTableColumn
adTa5kDs3PMDayThresholdPCV=_AdTa5kDs3PMDayThresholdPCV_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,6),_AdTa5kDs3PMDayThresholdPCV_Type())
adTa5kDs3PMDayThresholdPCV.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdPCV.setStatus(_A)
_AdTa5kDs3PMDayThresholdLES_Type=Integer32
_AdTa5kDs3PMDayThresholdLES_Object=MibTableColumn
adTa5kDs3PMDayThresholdLES=_AdTa5kDs3PMDayThresholdLES_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,7),_AdTa5kDs3PMDayThresholdLES_Type())
adTa5kDs3PMDayThresholdLES.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdLES.setStatus(_A)
_AdTa5kDs3PMDayThresholdCCV_Type=Integer32
_AdTa5kDs3PMDayThresholdCCV_Object=MibTableColumn
adTa5kDs3PMDayThresholdCCV=_AdTa5kDs3PMDayThresholdCCV_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,8),_AdTa5kDs3PMDayThresholdCCV_Type())
adTa5kDs3PMDayThresholdCCV.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdCCV.setStatus(_A)
_AdTa5kDs3PMDayThresholdCES_Type=Integer32
_AdTa5kDs3PMDayThresholdCES_Object=MibTableColumn
adTa5kDs3PMDayThresholdCES=_AdTa5kDs3PMDayThresholdCES_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,9),_AdTa5kDs3PMDayThresholdCES_Type())
adTa5kDs3PMDayThresholdCES.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdCES.setStatus(_A)
_AdTa5kDs3PMDayThresholdCSES_Type=Integer32
_AdTa5kDs3PMDayThresholdCSES_Object=MibTableColumn
adTa5kDs3PMDayThresholdCSES=_AdTa5kDs3PMDayThresholdCSES_Object((1,3,6,1,4,1,664,5,67,1,21,2,2,1,10),_AdTa5kDs3PMDayThresholdCSES_Type())
adTa5kDs3PMDayThresholdCSES.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kDs3PMDayThresholdCSES.setStatus(_A)
_AdTA5kds3MibConformance_ObjectIdentity=ObjectIdentity
adTA5kds3MibConformance=_AdTA5kds3MibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,21,3))
_AdTA5kds3MibGroups_ObjectIdentity=ObjectIdentity
adTA5kds3MibGroups=_AdTA5kds3MibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,21,3,1))
adTa5kDS3PMqtrThresholdGroup=ObjectGroup((1,3,6,1,4,1,664,5,67,1,21,3,1,1))
adTa5kDS3PMqtrThresholdGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:adTa5kDS3PMqtrThresholdGroup.setStatus(_A)
adTa5kDS3PMdayThresholdGroup=ObjectGroup((1,3,6,1,4,1,664,5,67,1,21,3,1,2))
adTa5kDS3PMdayThresholdGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:adTa5kDS3PMdayThresholdGroup.setStatus(_A)
adTA5kds3LOSTrapActive=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,1))
adTA5kds3LOSTrapActive.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_L)))
if mibBuilder.loadTexts:adTA5kds3LOSTrapActive.setStatus(_A)
adTA5kds3LOSTrapClear=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,2))
adTA5kds3LOSTrapClear.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J),(_C,_L)))
if mibBuilder.loadTexts:adTA5kds3LOSTrapClear.setStatus(_A)
adTA5kds3LOFTrapActive=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,3))
adTA5kds3LOFTrapActive.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_L)))
if mibBuilder.loadTexts:adTA5kds3LOFTrapActive.setStatus(_A)
adTA5kds3LOFTrapClear=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,4))
adTA5kds3LOFTrapClear.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_L)))
if mibBuilder.loadTexts:adTA5kds3LOFTrapClear.setStatus(_A)
adTA5kds3RAITrapActive=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,5))
adTA5kds3RAITrapActive.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_L)))
if mibBuilder.loadTexts:adTA5kds3RAITrapActive.setStatus(_A)
adTA5kds3RAITrapClear=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,6))
adTA5kds3RAITrapClear.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_L)))
if mibBuilder.loadTexts:adTA5kds3RAITrapClear.setStatus(_A)
adTA5kds3AISTrapActive=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,7))
adTA5kds3AISTrapActive.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_L)))
if mibBuilder.loadTexts:adTA5kds3AISTrapActive.setStatus(_A)
adTA5kds3AISTrapClear=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,8))
adTA5kds3AISTrapClear.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_L)))
if mibBuilder.loadTexts:adTA5kds3AISTrapClear.setStatus(_A)
adTA5kds3almQtrPESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,9))
adTA5kds3almQtrPESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrPESThresholdCrossed.setStatus(_A)
adTA5kds3almQtrPSESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,10))
adTA5kds3almQtrPSESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrPSESThresholdCrossed.setStatus(_A)
adTA5kds3almQtrSEFSThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,11))
adTA5kds3almQtrSEFSThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrSEFSThresholdCrossed.setStatus(_A)
adTA5kds3almQtrUASThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,12))
adTA5kds3almQtrUASThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrUASThresholdCrossed.setStatus(_A)
adTA5kds3almQtrLCVThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,13))
adTA5kds3almQtrLCVThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrLCVThresholdCrossed.setStatus(_A)
adTA5kds3almQtrPCVThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,14))
adTA5kds3almQtrPCVThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrPCVThresholdCrossed.setStatus(_A)
adTA5kds3almQtrLESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,15))
adTA5kds3almQtrLESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrLESThresholdCrossed.setStatus(_A)
adTA5kds3almQtrCCVThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,16))
adTA5kds3almQtrCCVThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrCCVThresholdCrossed.setStatus(_A)
adTA5kds3almQtrCESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,17))
adTA5kds3almQtrCESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrCESThresholdCrossed.setStatus(_A)
adTA5kds3almQtrCSESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,18))
adTA5kds3almQtrCSESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3almQtrCSESThresholdCrossed.setStatus(_A)
adTA5kds3PMDayPESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,19))
adTA5kds3PMDayPESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDayPESThresholdCrossed.setStatus(_A)
adTA5kds3PMDayPSESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,20))
adTA5kds3PMDayPSESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDayPSESThresholdCrossed.setStatus(_A)
adTA5kds3PMDaySEFSThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,21))
adTA5kds3PMDaySEFSThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDaySEFSThresholdCrossed.setStatus(_A)
adTA5kds3PMDayUASThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,22))
adTA5kds3PMDayUASThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDayUASThresholdCrossed.setStatus(_A)
adTA5kds3PMDayLCVThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,23))
adTA5kds3PMDayLCVThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDayLCVThresholdCrossed.setStatus(_A)
adTA5kds3PMDayPCVThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,24))
adTA5kds3PMDayPCVThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDayPCVThresholdCrossed.setStatus(_A)
adTA5kds3PMDayLESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,25))
adTA5kds3PMDayLESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDayLESThresholdCrossed.setStatus(_A)
adTA5kds3PMDayCCVThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,26))
adTA5kds3PMDayCCVThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDayCCVThresholdCrossed.setStatus(_A)
adTA5kds3PMDayCESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,27))
adTA5kds3PMDayCESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDayCESThresholdCrossed.setStatus(_A)
adTA5kds3PMDayCSESThresholdCrossed=NotificationType((1,3,6,1,4,1,664,5,67,1,21,1,0,28))
adTA5kds3PMDayCSESThresholdCrossed.setObjects(*((_F,_G),(_H,_I),(_D,_E),(_C,_J)))
if mibBuilder.loadTexts:adTA5kds3PMDayCSESThresholdCrossed.setStatus(_A)
adTa5kDS3EventGroup=NotificationGroup((1,3,6,1,4,1,664,5,67,1,21,3,1,3))
adTa5kDS3EventGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:adTa5kDS3EventGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adTA5kds3TrapsPrefix':adTA5kds3TrapsPrefix,'adTA5kds3Traps':adTA5kds3Traps,_i:adTA5kds3LOSTrapActive,_j:adTA5kds3LOSTrapClear,_k:adTA5kds3LOFTrapActive,_l:adTA5kds3LOFTrapClear,_m:adTA5kds3RAITrapActive,_n:adTA5kds3RAITrapClear,_o:adTA5kds3AISTrapActive,_p:adTA5kds3AISTrapClear,_q:adTA5kds3almQtrPESThresholdCrossed,_r:adTA5kds3almQtrPSESThresholdCrossed,_s:adTA5kds3almQtrSEFSThresholdCrossed,_t:adTA5kds3almQtrUASThresholdCrossed,_u:adTA5kds3almQtrLCVThresholdCrossed,_v:adTA5kds3almQtrPCVThresholdCrossed,_w:adTA5kds3almQtrLESThresholdCrossed,_x:adTA5kds3almQtrCCVThresholdCrossed,_y:adTA5kds3almQtrCESThresholdCrossed,_z:adTA5kds3almQtrCSESThresholdCrossed,_A0:adTA5kds3PMDayPESThresholdCrossed,_A1:adTA5kds3PMDayPSESThresholdCrossed,_A2:adTA5kds3PMDaySEFSThresholdCrossed,_A3:adTA5kds3PMDayUASThresholdCrossed,_A4:adTA5kds3PMDayLCVThresholdCrossed,_A5:adTA5kds3PMDayPCVThresholdCrossed,_A6:adTA5kds3PMDayLESThresholdCrossed,_A7:adTA5kds3PMDayCCVThresholdCrossed,_A8:adTA5kds3PMDayCESThresholdCrossed,_A9:adTA5kds3PMDayCSESThresholdCrossed,'adTA5kds3PMThreshold':adTA5kds3PMThreshold,'adTa5kDS3PMqtrThresholdTable':adTa5kDS3PMqtrThresholdTable,'adTa5kDS3PMqtrThresholdEntry':adTa5kDS3PMqtrThresholdEntry,_O:adTa5kDs3PMqtrThresholdPESs,_P:adTa5kDs3PMqtrThresholdPSESs,_Q:adTa5kDs3PMqtrThresholdSEFSs,_R:adTa5kDs3PMqtrThresholdUASs,_S:adTa5kDs3PMqtrThresholdLCVs,_T:adTa5kDs3PMqtrThresholdPCVs,_U:adTa5kDs3PMqtrThresholdLESs,_V:adTa5kDs3PMqtrThresholdCCVs,_W:adTa5kDs3PMqtrThresholdCESs,_X:adTa5kDs3PMqtrThresholdCSESs,'adTa5kDs3PMDayThresholdTable':adTa5kDs3PMDayThresholdTable,'adTa5kDs3PMDayThresholdEntry':adTa5kDs3PMDayThresholdEntry,_Y:adTa5kDs3PMDayThresholdPES,_Z:adTa5kDs3PMDayThresholdPSES,_a:adTa5kDs3PMDayThresholdSEFS,_b:adTa5kDs3PMDayThresholdUAS,_c:adTa5kDs3PMDayThresholdLCV,_d:adTa5kDs3PMDayThresholdPCV,_e:adTa5kDs3PMDayThresholdLES,_f:adTa5kDs3PMDayThresholdCCV,_g:adTa5kDs3PMDayThresholdCES,_h:adTa5kDs3PMDayThresholdCSES,'adTA5kds3MibConformance':adTA5kds3MibConformance,'adTA5kds3MibGroups':adTA5kds3MibGroups,'adTa5kDS3PMqtrThresholdGroup':adTa5kDS3PMqtrThresholdGroup,'adTa5kDS3PMdayThresholdGroup':adTa5kDS3PMdayThresholdGroup,'adTa5kDS3EventGroup':adTa5kDS3EventGroup,'adTa5kDs3PMThresholdModuleIdentity':adTa5kDs3PMThresholdModuleIdentity})