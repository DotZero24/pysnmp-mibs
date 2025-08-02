_L='backupSetRecid'
_K='backupSetPeid'
_J='inactive'
_I='active'
_H='backupTransportIndex'
_G='enable'
_F='DisplayString'
_E='CISCO-DMN-DSG-DR-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
ciscoDSGDR=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,43))
if mibBuilder.loadTexts:ciscoDSGDR.setRevisions(('2014-08-30 08:00',))
_DrGlobalCfg_ObjectIdentity=ObjectIdentity
drGlobalCfg=_DrGlobalCfg_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,43,1))
class _Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),(_G,2)))
_Enable_Type.__name__=_B
_Enable_Object=MibScalar
enable=_Enable_Object((1,3,6,1,4,1,1429,2,2,5,43,1,1),_Enable_Type())
enable.setMaxAccess(_C)
if mibBuilder.loadTexts:enable.setStatus(_A)
class _SigLockTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,255))
_SigLockTime_Type.__name__=_B
_SigLockTime_Object=MibScalar
sigLockTime=_SigLockTime_Object((1,3,6,1,4,1,1429,2,2,5,43,1,2),_SigLockTime_Type())
sigLockTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sigLockTime.setStatus(_A)
class _SigLossTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,2160000))
_SigLossTime_Type.__name__=_B
_SigLossTime_Object=MibScalar
sigLossTime=_SigLossTime_Object((1,3,6,1,4,1,1429,2,2,5,43,1,3),_SigLossTime_Type())
sigLossTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sigLossTime.setStatus(_A)
class _VerifyTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_VerifyTimer_Type.__name__=_B
_VerifyTimer_Object=MibScalar
verifyTimer=_VerifyTimer_Object((1,3,6,1,4,1,1429,2,2,5,43,1,4),_VerifyTimer_Type())
verifyTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:verifyTimer.setStatus(_A)
class _Profile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('uplink',2)))
_Profile_Type.__name__=_B
_Profile_Object=MibScalar
profile=_Profile_Object((1,3,6,1,4,1,1429,2,2,5,43,1,5),_Profile_Type())
profile.setMaxAccess(_C)
if mibBuilder.loadTexts:profile.setStatus(_A)
_BackupTransportTable_Object=MibTable
backupTransportTable=_BackupTransportTable_Object((1,3,6,1,4,1,1429,2,2,5,43,2))
if mibBuilder.loadTexts:backupTransportTable.setStatus(_A)
_BackupTransportEntry_Object=MibTableRow
backupTransportEntry=_BackupTransportEntry_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1))
backupTransportEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:backupTransportEntry.setStatus(_A)
class _BackupTransportIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_BackupTransportIndex_Type.__name__=_B
_BackupTransportIndex_Object=MibTableColumn
backupTransportIndex=_BackupTransportIndex_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,1),_BackupTransportIndex_Type())
backupTransportIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:backupTransportIndex.setStatus(_A)
class _BackupTransportSetIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BackupTransportSetIdx_Type.__name__=_B
_BackupTransportSetIdx_Object=MibTableColumn
backupTransportSetIdx=_BackupTransportSetIdx_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,2),_BackupTransportSetIdx_Type())
backupTransportSetIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportSetIdx.setStatus(_A)
class _BackupTransportDvbsFec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,6,7,10)));namedValues=NamedValues(*(('oneHalf',1),('twoThirds',3),('threeQuarters',4),('fiveSixths',6),('sevenEigths',7),('auto',10)))
_BackupTransportDvbsFec_Type.__name__=_B
_BackupTransportDvbsFec_Object=MibTableColumn
backupTransportDvbsFec=_BackupTransportDvbsFec_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,3),_BackupTransportDvbsFec_Type())
backupTransportDvbsFec.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportDvbsFec.setStatus(_A)
class _BackupTransportEwFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('east',1),('west',2),('notApplicable',3)))
_BackupTransportEwFlag_Type.__name__=_B
_BackupTransportEwFlag_Object=MibTableColumn
backupTransportEwFlag=_BackupTransportEwFlag_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,4),_BackupTransportEwFlag_Type())
backupTransportEwFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportEwFlag.setStatus(_A)
class _BackupTransportFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000000))
_BackupTransportFrequency_Type.__name__=_B
_BackupTransportFrequency_Object=MibTableColumn
backupTransportFrequency=_BackupTransportFrequency_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,5),_BackupTransportFrequency_Type())
backupTransportFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportFrequency.setStatus(_A)
class _BackupTransportRFInput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rf1',1),('rf2',2),('rf3',3),('rf4',4)))
_BackupTransportRFInput_Type.__name__=_B
_BackupTransportRFInput_Object=MibTableColumn
backupTransportRFInput=_BackupTransportRFInput_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,6),_BackupTransportRFInput_Type())
backupTransportRFInput.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportRFInput.setStatus(_A)
class _BackupTransportModSys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('qpsk_dvb-s',1),('qpsk_dvb-S2',2)))
_BackupTransportModSys_Type.__name__=_B
_BackupTransportModSys_Object=MibTableColumn
backupTransportModSys=_BackupTransportModSys_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,7),_BackupTransportModSys_Type())
backupTransportModSys.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportModSys.setStatus(_A)
class _BackupTransportNetId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BackupTransportNetId_Type.__name__=_B
_BackupTransportNetId_Object=MibTableColumn
backupTransportNetId=_BackupTransportNetId_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,8),_BackupTransportNetId_Type())
backupTransportNetId.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportNetId.setStatus(_A)
class _BackupTransportOrbitalPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_BackupTransportOrbitalPos_Type.__name__=_B
_BackupTransportOrbitalPos_Object=MibTableColumn
backupTransportOrbitalPos=_BackupTransportOrbitalPos_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,9),_BackupTransportOrbitalPos_Type())
backupTransportOrbitalPos.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportOrbitalPos.setStatus(_A)
class _BackupTransportOrbpolarization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_BackupTransportOrbpolarization_Type.__name__=_B
_BackupTransportOrbpolarization_Object=MibTableColumn
backupTransportOrbpolarization=_BackupTransportOrbpolarization_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,10),_BackupTransportOrbpolarization_Type())
backupTransportOrbpolarization.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportOrbpolarization.setStatus(_A)
class _BackupTransportSymbRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10000,450000))
_BackupTransportSymbRate_Type.__name__=_B
_BackupTransportSymbRate_Object=MibTableColumn
backupTransportSymbRate=_BackupTransportSymbRate_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,11),_BackupTransportSymbRate_Type())
backupTransportSymbRate.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportSymbRate.setStatus(_A)
class _BackupTransportRollOffFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,25)));namedValues=NamedValues(*(('f35',1),('f20',3),('f25',25)))
_BackupTransportRollOffFactor_Type.__name__=_B
_BackupTransportRollOffFactor_Object=MibTableColumn
backupTransportRollOffFactor=_BackupTransportRollOffFactor_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,12),_BackupTransportRollOffFactor_Type())
backupTransportRollOffFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportRollOffFactor.setStatus(_A)
class _BackupTransportRowstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),('delete',3),('add',4)))
_BackupTransportRowstatus_Type.__name__=_B
_BackupTransportRowstatus_Object=MibTableColumn
backupTransportRowstatus=_BackupTransportRowstatus_Object((1,3,6,1,4,1,1429,2,2,5,43,2,1,13),_BackupTransportRowstatus_Type())
backupTransportRowstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:backupTransportRowstatus.setStatus(_A)
_BackupSetTable_Object=MibTable
backupSetTable=_BackupSetTable_Object((1,3,6,1,4,1,1429,2,2,5,43,3))
if mibBuilder.loadTexts:backupSetTable.setStatus(_A)
_BackupSetEntry_Object=MibTableRow
backupSetEntry=_BackupSetEntry_Object((1,3,6,1,4,1,1429,2,2,5,43,3,1))
backupSetEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:backupSetEntry.setStatus(_A)
class _BackupSetPeid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BackupSetPeid_Type.__name__=_B
_BackupSetPeid_Object=MibTableColumn
backupSetPeid=_BackupSetPeid_Object((1,3,6,1,4,1,1429,2,2,5,43,3,1,1),_BackupSetPeid_Type())
backupSetPeid.setMaxAccess(_D)
if mibBuilder.loadTexts:backupSetPeid.setStatus(_A)
class _BackupSetRecid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BackupSetRecid_Type.__name__=_B
_BackupSetRecid_Object=MibTableColumn
backupSetRecid=_BackupSetRecid_Object((1,3,6,1,4,1,1429,2,2,5,43,3,1,2),_BackupSetRecid_Type())
backupSetRecid.setMaxAccess(_D)
if mibBuilder.loadTexts:backupSetRecid.setStatus(_A)
class _BackupSetCsiidx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BackupSetCsiidx_Type.__name__=_B
_BackupSetCsiidx_Object=MibTableColumn
backupSetCsiidx=_BackupSetCsiidx_Object((1,3,6,1,4,1,1429,2,2,5,43,3,1,3),_BackupSetCsiidx_Type())
backupSetCsiidx.setMaxAccess(_D)
if mibBuilder.loadTexts:backupSetCsiidx.setStatus(_A)
class _BackupSetBkpch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BackupSetBkpch_Type.__name__=_B
_BackupSetBkpch_Object=MibTableColumn
backupSetBkpch=_BackupSetBkpch_Object((1,3,6,1,4,1,1429,2,2,5,43,3,1,4),_BackupSetBkpch_Type())
backupSetBkpch.setMaxAccess(_C)
if mibBuilder.loadTexts:backupSetBkpch.setStatus(_A)
class _BackupSetBkpchDispText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_BackupSetBkpchDispText_Type.__name__=_F
_BackupSetBkpchDispText_Object=MibTableColumn
backupSetBkpchDispText=_BackupSetBkpchDispText_Object((1,3,6,1,4,1,1429,2,2,5,43,3,1,5),_BackupSetBkpchDispText_Type())
backupSetBkpchDispText.setMaxAccess(_D)
if mibBuilder.loadTexts:backupSetBkpchDispText.setStatus(_A)
class _BackupSetRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_BackupSetRowStatus_Type.__name__=_B
_BackupSetRowStatus_Object=MibTableColumn
backupSetRowStatus=_BackupSetRowStatus_Object((1,3,6,1,4,1,1429,2,2,5,43,3,1,6),_BackupSetRowStatus_Type())
backupSetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:backupSetRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGDR':ciscoDSGDR,'drGlobalCfg':drGlobalCfg,_G:enable,'sigLockTime':sigLockTime,'sigLossTime':sigLossTime,'verifyTimer':verifyTimer,'profile':profile,'backupTransportTable':backupTransportTable,'backupTransportEntry':backupTransportEntry,_H:backupTransportIndex,'backupTransportSetIdx':backupTransportSetIdx,'backupTransportDvbsFec':backupTransportDvbsFec,'backupTransportEwFlag':backupTransportEwFlag,'backupTransportFrequency':backupTransportFrequency,'backupTransportRFInput':backupTransportRFInput,'backupTransportModSys':backupTransportModSys,'backupTransportNetId':backupTransportNetId,'backupTransportOrbitalPos':backupTransportOrbitalPos,'backupTransportOrbpolarization':backupTransportOrbpolarization,'backupTransportSymbRate':backupTransportSymbRate,'backupTransportRollOffFactor':backupTransportRollOffFactor,'backupTransportRowstatus':backupTransportRowstatus,'backupSetTable':backupSetTable,'backupSetEntry':backupSetEntry,_K:backupSetPeid,_L:backupSetRecid,'backupSetCsiidx':backupSetCsiidx,'backupSetBkpch':backupSetBkpch,'backupSetBkpchDispText':backupSetBkpchDispText,'backupSetRowStatus':backupSetRowStatus})