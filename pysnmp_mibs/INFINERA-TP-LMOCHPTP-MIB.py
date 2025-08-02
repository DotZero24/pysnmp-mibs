_d='lmOchPtpGroup'
_c='lmOchPtpFwUpgradeStatus'
_b='lmOchPtpCDCompEnd'
_a='lmOchPtpCDCompStart'
_Z='lmOchPtpCDSearchStepSize'
_Y='lmOchPtpCDCompMode'
_X='lmOchPtpInstalledModulation'
_W='lmOchPtpModulation'
_V='lmOchPtpFFCRBlockSize'
_U='lmOchPtpPmHistStatsEnable'
_T='lmOchPtpRemoteOcgPortId'
_S='lmOchPtpDiscoveredOchPortId'
_R='lmOchPtpInstalledWavelength'
_Q='lmOchPtpInstalledOcgNumber'
_P='lmOchPtpInstalledOchNumber'
_O='lmOchPtpTuneableOcgNumber'
_N='lmOchPtpTuneableOchNumber'
_M='lmOchPtpRate'
_L='lmOchPtpAutoDiscoveryState'
_K='pm-Bpsk'
_J='pm-Qpsk'
_I='failed'
_H='completed'
_G='inProgress'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='INFINERA-TP-LMOCHPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
lmOchPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,27))
if mibBuilder.loadTexts:lmOchPtpMIB.setRevisions(('2011-05-23 00:00',))
_LmOchPtpTable_Object=MibTable
lmOchPtpTable=_LmOchPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1))
if mibBuilder.loadTexts:lmOchPtpTable.setStatus(_A)
_LmOchPtpEntry_Object=MibTableRow
lmOchPtpEntry=_LmOchPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1))
lmOchPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:lmOchPtpEntry.setStatus(_A)
class _LmOchPtpAutoDiscoveryState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_H,2),('unknown',3),('notValidOrShutdown',4),(_I,5)))
_LmOchPtpAutoDiscoveryState_Type.__name__=_D
_LmOchPtpAutoDiscoveryState_Object=MibTableColumn
lmOchPtpAutoDiscoveryState=_LmOchPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,1),_LmOchPtpAutoDiscoveryState_Type())
lmOchPtpAutoDiscoveryState.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpAutoDiscoveryState.setStatus(_A)
_LmOchPtpRate_Type=Integer32
_LmOchPtpRate_Object=MibTableColumn
lmOchPtpRate=_LmOchPtpRate_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,2),_LmOchPtpRate_Type())
lmOchPtpRate.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpRate.setStatus(_A)
_LmOchPtpTuneableOchNumber_Type=Integer32
_LmOchPtpTuneableOchNumber_Object=MibTableColumn
lmOchPtpTuneableOchNumber=_LmOchPtpTuneableOchNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,3),_LmOchPtpTuneableOchNumber_Type())
lmOchPtpTuneableOchNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpTuneableOchNumber.setStatus(_A)
_LmOchPtpTuneableOcgNumber_Type=Integer32
_LmOchPtpTuneableOcgNumber_Object=MibTableColumn
lmOchPtpTuneableOcgNumber=_LmOchPtpTuneableOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,4),_LmOchPtpTuneableOcgNumber_Type())
lmOchPtpTuneableOcgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpTuneableOcgNumber.setStatus(_A)
_LmOchPtpInstalledOchNumber_Type=Integer32
_LmOchPtpInstalledOchNumber_Object=MibTableColumn
lmOchPtpInstalledOchNumber=_LmOchPtpInstalledOchNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,5),_LmOchPtpInstalledOchNumber_Type())
lmOchPtpInstalledOchNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpInstalledOchNumber.setStatus(_A)
_LmOchPtpInstalledOcgNumber_Type=Integer32
_LmOchPtpInstalledOcgNumber_Object=MibTableColumn
lmOchPtpInstalledOcgNumber=_LmOchPtpInstalledOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,6),_LmOchPtpInstalledOcgNumber_Type())
lmOchPtpInstalledOcgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpInstalledOcgNumber.setStatus(_A)
_LmOchPtpInstalledWavelength_Type=FloatTenths
_LmOchPtpInstalledWavelength_Object=MibTableColumn
lmOchPtpInstalledWavelength=_LmOchPtpInstalledWavelength_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,7),_LmOchPtpInstalledWavelength_Type())
lmOchPtpInstalledWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpInstalledWavelength.setStatus(_A)
_LmOchPtpDiscoveredOchPortId_Type=DisplayString
_LmOchPtpDiscoveredOchPortId_Object=MibTableColumn
lmOchPtpDiscoveredOchPortId=_LmOchPtpDiscoveredOchPortId_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,8),_LmOchPtpDiscoveredOchPortId_Type())
lmOchPtpDiscoveredOchPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpDiscoveredOchPortId.setStatus(_A)
_LmOchPtpRemoteOcgPortId_Type=DisplayString
_LmOchPtpRemoteOcgPortId_Object=MibTableColumn
lmOchPtpRemoteOcgPortId=_LmOchPtpRemoteOcgPortId_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,9),_LmOchPtpRemoteOcgPortId_Type())
lmOchPtpRemoteOcgPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpRemoteOcgPortId.setStatus(_A)
class _LmOchPtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_LmOchPtpPmHistStatsEnable_Type.__name__=_D
_LmOchPtpPmHistStatsEnable_Object=MibTableColumn
lmOchPtpPmHistStatsEnable=_LmOchPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,10),_LmOchPtpPmHistStatsEnable_Type())
lmOchPtpPmHistStatsEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:lmOchPtpPmHistStatsEnable.setStatus(_A)
_LmOchPtpFFCRBlockSize_Type=Integer32
_LmOchPtpFFCRBlockSize_Object=MibTableColumn
lmOchPtpFFCRBlockSize=_LmOchPtpFFCRBlockSize_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,11),_LmOchPtpFFCRBlockSize_Type())
lmOchPtpFFCRBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpFFCRBlockSize.setStatus(_A)
class _LmOchPtpModulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LmOchPtpModulation_Type.__name__=_D
_LmOchPtpModulation_Object=MibTableColumn
lmOchPtpModulation=_LmOchPtpModulation_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,12),_LmOchPtpModulation_Type())
lmOchPtpModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpModulation.setStatus(_A)
class _LmOchPtpInstalledModulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LmOchPtpInstalledModulation_Type.__name__=_D
_LmOchPtpInstalledModulation_Object=MibTableColumn
lmOchPtpInstalledModulation=_LmOchPtpInstalledModulation_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,13),_LmOchPtpInstalledModulation_Type())
lmOchPtpInstalledModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpInstalledModulation.setStatus(_A)
class _LmOchPtpCDCompMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('automatic',1),('manual',2),('disable',3)))
_LmOchPtpCDCompMode_Type.__name__=_D
_LmOchPtpCDCompMode_Object=MibTableColumn
lmOchPtpCDCompMode=_LmOchPtpCDCompMode_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,14),_LmOchPtpCDCompMode_Type())
lmOchPtpCDCompMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpCDCompMode.setStatus(_A)
_LmOchPtpCDSearchStepSize_Type=Integer32
_LmOchPtpCDSearchStepSize_Object=MibTableColumn
lmOchPtpCDSearchStepSize=_LmOchPtpCDSearchStepSize_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,15),_LmOchPtpCDSearchStepSize_Type())
lmOchPtpCDSearchStepSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpCDSearchStepSize.setStatus(_A)
_LmOchPtpCDCompStart_Type=Integer32
_LmOchPtpCDCompStart_Object=MibTableColumn
lmOchPtpCDCompStart=_LmOchPtpCDCompStart_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,16),_LmOchPtpCDCompStart_Type())
lmOchPtpCDCompStart.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpCDCompStart.setStatus(_A)
_LmOchPtpCDCompEnd_Type=Integer32
_LmOchPtpCDCompEnd_Object=MibTableColumn
lmOchPtpCDCompEnd=_LmOchPtpCDCompEnd_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,17),_LmOchPtpCDCompEnd_Type())
lmOchPtpCDCompEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpCDCompEnd.setStatus(_A)
class _LmOchPtpFwUpgradeStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_G,2),(_H,3),(_I,4)))
_LmOchPtpFwUpgradeStatus_Type.__name__=_D
_LmOchPtpFwUpgradeStatus_Object=MibTableColumn
lmOchPtpFwUpgradeStatus=_LmOchPtpFwUpgradeStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,27,1,1,18),_LmOchPtpFwUpgradeStatus_Type())
lmOchPtpFwUpgradeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpFwUpgradeStatus.setStatus(_A)
_LmOchPtpConformance_ObjectIdentity=ObjectIdentity
lmOchPtpConformance=_LmOchPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,27,3))
_LmOchPtpCompliances_ObjectIdentity=ObjectIdentity
lmOchPtpCompliances=_LmOchPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,27,3,1))
_LmOchPtpGroups_ObjectIdentity=ObjectIdentity
lmOchPtpGroups=_LmOchPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,27,3,2))
lmOchPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,27,3,2,1))
lmOchPtpGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:lmOchPtpGroup.setStatus(_A)
lmOchPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,27,3,1,1))
lmOchPtpCompliance.setObjects((_B,_d))
if mibBuilder.loadTexts:lmOchPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lmOchPtpMIB':lmOchPtpMIB,'lmOchPtpTable':lmOchPtpTable,'lmOchPtpEntry':lmOchPtpEntry,_L:lmOchPtpAutoDiscoveryState,_M:lmOchPtpRate,_N:lmOchPtpTuneableOchNumber,_O:lmOchPtpTuneableOcgNumber,_P:lmOchPtpInstalledOchNumber,_Q:lmOchPtpInstalledOcgNumber,_R:lmOchPtpInstalledWavelength,_S:lmOchPtpDiscoveredOchPortId,_T:lmOchPtpRemoteOcgPortId,_U:lmOchPtpPmHistStatsEnable,_V:lmOchPtpFFCRBlockSize,_W:lmOchPtpModulation,_X:lmOchPtpInstalledModulation,_Y:lmOchPtpCDCompMode,_Z:lmOchPtpCDSearchStepSize,_a:lmOchPtpCDCompStart,_b:lmOchPtpCDCompEnd,_c:lmOchPtpFwUpgradeStatus,'lmOchPtpConformance':lmOchPtpConformance,'lmOchPtpCompliances':lmOchPtpCompliances,'lmOchPtpCompliance':lmOchPtpCompliance,'lmOchPtpGroups':lmOchPtpGroups,_d:lmOchPtpGroup})