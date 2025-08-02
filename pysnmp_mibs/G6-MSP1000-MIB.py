_BM='bertStatusIndex'
_BL='emStatusIndex'
_BK='portStatusPortIndex'
_BJ='moduleStatusIndex'
_BI='moduleInventoryIndex'
_BH='systemStatusIndex'
_BG='moduleControlIndex'
_BF='emConfigIndex'
_BE='signalLow'
_BD='lp1ConfigIndex'
_BC='om1ConfigIndex'
_BB='m2gConfigIndex'
_BA='infiniband'
_B9='t4gConfigIndex'
_B8='cxgConfigIndex'
_B7='cxgPlusConfigIndex'
_B6='txgConfigIndex'
_B5='signalLoss'
_B4='bertPort4'
_B3='x2gConfigIndex'
_B2='slotConfigIndex'
_B1='systemConfigIndex'
_B0='ms4xFc'
_A_='ms10xFc16xFc'
_Az='transponder'
_Ay='ms15Minutes'
_Ax='ms15Seconds'
_Aw='noDelay'
_Av='ms8b10bCnt'
_Au='crPat'
_At='cjPat'
_As='ms231'
_Ar='ms223'
_Aq='passive'
_Ap='none'
_Ao='ms1310nm'
_An='ms1550nm'
_Am='ms8xFc'
_Al='manually'
_Ak='Bits'
_Aj='ms10gEth'
_Ai='otu1'
_Ah='hdtv'
_Ag='sdi'
_Af='fix100'
_Ae='m2g'
_Ad='ms5Db'
_Ac='ms3Db'
_Ab='ms2Db'
_Aa='ms15Db'
_AZ='ms1Db'
_AY='ms05Db'
_AX='ms240Sec'
_AW='ms60Sec'
_AV='ms30Sec'
_AU='ms10Sec'
_AT='ms5Sec'
_AS='ms1Sec'
_AR='percolate'
_AQ='local'
_AP='oc48'
_AO='ms2xFc'
_AN='oc12'
_AM='escon'
_AL='oc3'
_AK='ms100mEth'
_AJ='ch63'
_AI='ch62'
_AH='ch61'
_AG='ch60'
_AF='ch59'
_AE='ch58'
_AD='ch57'
_AC='ch56'
_AB='ch55'
_AA='ch54'
_A9='ch53'
_A8='ch52'
_A7='ch51'
_A6='ch50'
_A5='ch49'
_A4='ch48'
_A3='ch47'
_A2='ch46'
_A1='ch45'
_A0='ch44'
_z='ch43'
_y='ch42'
_x='ch41'
_w='ch40'
_v='ch39'
_u='ch38'
_t='ch37'
_s='ch36'
_r='ch35'
_q='ch34'
_p='ch33'
_o='ch32'
_n='ch31'
_m='ch30'
_l='ch29'
_k='ch28'
_j='ch27'
_i='ch26'
_h='ch25'
_g='ch24'
_f='ch23'
_e='ch22'
_d='ch21'
_c='ch20'
_b='ch19'
_a='ch18'
_Z='ch17'
_Y='ch16'
_X='ch15'
_W='ch14'
_V='ch13'
_U='ch12'
_T='ch11'
_S='fixed'
_R='remote'
_Q='extendedLocked'
_P='normalLocked'
_O='extended'
_N='true'
_M='false'
_L='normal'
_K='ms1gEth'
_J='ms1xFc'
_I='transparent'
_H='not-accessible'
_G='G6-MSP1000-MIB'
_F='enabled'
_E='disabled'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_Ak,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
device=ModuleIdentity((1,3,6,1,4,1,3181,10,6,1))
if mibBuilder.loadTexts:device.setRevisions(('2018-02-12 16:19',))
_Msp1000_ObjectIdentity=ObjectIdentity
msp1000=_Msp1000_ObjectIdentity((1,3,6,1,4,1,3181,10,6,1,94))
_SystemConfigTable_Object=MibTable
systemConfigTable=_SystemConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,1))
if mibBuilder.loadTexts:systemConfigTable.setStatus(_A)
_SystemConfigEntry_Object=MibTableRow
systemConfigEntry=_SystemConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,1,1))
systemConfigEntry.setIndexNames((0,_G,_B1))
if mibBuilder.loadTexts:systemConfigEntry.setStatus(_A)
class _SystemConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_SystemConfigIndex_Type.__name__=_B
_SystemConfigIndex_Object=MibTableColumn
systemConfigIndex=_SystemConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,1,1,1),_SystemConfigIndex_Type())
systemConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:systemConfigIndex.setStatus(_A)
class _SystemConfigNmsOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Aq,0),('active',1)))
_SystemConfigNmsOperationMode_Type.__name__=_B
_SystemConfigNmsOperationMode_Object=MibTableColumn
systemConfigNmsOperationMode=_SystemConfigNmsOperationMode_Object((1,3,6,1,4,1,3181,10,6,1,94,1,1,2),_SystemConfigNmsOperationMode_Type())
systemConfigNmsOperationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:systemConfigNmsOperationMode.setStatus(_A)
class _SystemConfigCoreMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('v1',0),('v2',1)))
_SystemConfigCoreMode_Type.__name__=_B
_SystemConfigCoreMode_Object=MibTableColumn
systemConfigCoreMode=_SystemConfigCoreMode_Object((1,3,6,1,4,1,3181,10,6,1,94,1,1,3),_SystemConfigCoreMode_Type())
systemConfigCoreMode.setMaxAccess(_C)
if mibBuilder.loadTexts:systemConfigCoreMode.setStatus(_A)
_SystemConfigNodeId_Type=Unsigned32
_SystemConfigNodeId_Object=MibTableColumn
systemConfigNodeId=_SystemConfigNodeId_Object((1,3,6,1,4,1,3181,10,6,1,94,1,1,4),_SystemConfigNodeId_Type())
systemConfigNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:systemConfigNodeId.setStatus(_A)
class _SystemConfigDisableLegacyAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SystemConfigDisableLegacyAccess_Type.__name__=_B
_SystemConfigDisableLegacyAccess_Object=MibTableColumn
systemConfigDisableLegacyAccess=_SystemConfigDisableLegacyAccess_Object((1,3,6,1,4,1,3181,10,6,1,94,1,1,5),_SystemConfigDisableLegacyAccess_Type())
systemConfigDisableLegacyAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:systemConfigDisableLegacyAccess.setStatus(_A)
_SlotConfigTable_Object=MibTable
slotConfigTable=_SlotConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,2))
if mibBuilder.loadTexts:slotConfigTable.setStatus(_A)
_SlotConfigEntry_Object=MibTableRow
slotConfigEntry=_SlotConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,2,1))
slotConfigEntry.setIndexNames((0,_G,_B2))
if mibBuilder.loadTexts:slotConfigEntry.setStatus(_A)
class _SlotConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_SlotConfigIndex_Type.__name__=_B
_SlotConfigIndex_Object=MibTableColumn
slotConfigIndex=_SlotConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,2,1,1),_SlotConfigIndex_Type())
slotConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:slotConfigIndex.setStatus(_A)
class _SlotConfigModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,10,11,12,13,14,15,16,17,18,19,50,56,57,60,61,62,63,65,66,72,87,88,104,105,106,108,109,110)));namedValues=NamedValues(*(('undefined',0),('empty',1),('legacy',2),(_Aq,3),('fc8Filter',10),('fc8aFilter',11),('fc8xFilter',12),('b4sFilter',13),('b4xFilter',14),('b8mFilter',15),('b8dFilter',16),('fd4Filter',17),('dc1Filter',18),('se1',19),('tdm4',50),(_Ae,56),('wcm2',57),('xcm1',60),('x2g',61),('t4g',62),('txg',63),('nm1',65),('nm2',66),('os1',72),('cxg',87),('cxgp',88),('om1',104),('em2',105),('lp1',106),('nm3',108),('em3',109),('nm3p',110)))
_SlotConfigModule_Type.__name__=_B
_SlotConfigModule_Object=MibTableColumn
slotConfigModule=_SlotConfigModule_Object((1,3,6,1,4,1,3181,10,6,1,94,2,1,2),_SlotConfigModule_Type())
slotConfigModule.setMaxAccess(_C)
if mibBuilder.loadTexts:slotConfigModule.setStatus(_A)
class _SlotConfigSparepartMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SlotConfigSparepartMode_Type.__name__=_B
_SlotConfigSparepartMode_Object=MibTableColumn
slotConfigSparepartMode=_SlotConfigSparepartMode_Object((1,3,6,1,4,1,3181,10,6,1,94,2,1,3),_SlotConfigSparepartMode_Type())
slotConfigSparepartMode.setMaxAccess(_C)
if mibBuilder.loadTexts:slotConfigSparepartMode.setStatus(_A)
_SlotConfigPort1Alias_Type=DisplayString
_SlotConfigPort1Alias_Object=MibTableColumn
slotConfigPort1Alias=_SlotConfigPort1Alias_Object((1,3,6,1,4,1,3181,10,6,1,94,2,1,4),_SlotConfigPort1Alias_Type())
slotConfigPort1Alias.setMaxAccess(_C)
if mibBuilder.loadTexts:slotConfigPort1Alias.setStatus(_A)
_SlotConfigPort2Alias_Type=DisplayString
_SlotConfigPort2Alias_Object=MibTableColumn
slotConfigPort2Alias=_SlotConfigPort2Alias_Object((1,3,6,1,4,1,3181,10,6,1,94,2,1,5),_SlotConfigPort2Alias_Type())
slotConfigPort2Alias.setMaxAccess(_C)
if mibBuilder.loadTexts:slotConfigPort2Alias.setStatus(_A)
_SlotConfigPort3Alias_Type=DisplayString
_SlotConfigPort3Alias_Object=MibTableColumn
slotConfigPort3Alias=_SlotConfigPort3Alias_Object((1,3,6,1,4,1,3181,10,6,1,94,2,1,6),_SlotConfigPort3Alias_Type())
slotConfigPort3Alias.setMaxAccess(_C)
if mibBuilder.loadTexts:slotConfigPort3Alias.setStatus(_A)
_SlotConfigPort4Alias_Type=DisplayString
_SlotConfigPort4Alias_Object=MibTableColumn
slotConfigPort4Alias=_SlotConfigPort4Alias_Object((1,3,6,1,4,1,3181,10,6,1,94,2,1,7),_SlotConfigPort4Alias_Type())
slotConfigPort4Alias.setMaxAccess(_C)
if mibBuilder.loadTexts:slotConfigPort4Alias.setStatus(_A)
_X2gConfigTable_Object=MibTable
x2gConfigTable=_X2gConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,3))
if mibBuilder.loadTexts:x2gConfigTable.setStatus(_A)
_X2gConfigEntry_Object=MibTableRow
x2gConfigEntry=_X2gConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1))
x2gConfigEntry.setIndexNames((0,_G,_B3))
if mibBuilder.loadTexts:x2gConfigEntry.setStatus(_A)
class _X2gConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_X2gConfigIndex_Type.__name__=_B
_X2gConfigIndex_Object=MibTableColumn
x2gConfigIndex=_X2gConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,1),_X2gConfigIndex_Type())
x2gConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:x2gConfigIndex.setStatus(_A)
class _X2gConfigPort1Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_I,0),(_Af,1),(_AK,2),(_AL,3),(_AM,4),(_Ag,5),(_AN,6),(_J,7),(_K,8),(_Ah,9),(_AO,10),(_AP,11),(_Ae,12),(_Ai,13)))
_X2gConfigPort1Datarate_Type.__name__=_B
_X2gConfigPort1Datarate_Object=MibTableColumn
x2gConfigPort1Datarate=_X2gConfigPort1Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,2),_X2gConfigPort1Datarate_Type())
x2gConfigPort1Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigPort1Datarate.setStatus(_A)
class _X2gConfigPort2Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_I,0),(_Af,1),(_AK,2),(_AL,3),(_AM,4),(_Ag,5),(_AN,6),(_J,7),(_K,8),(_Ah,9),(_AO,10),(_AP,11),(_Ae,12),(_Ai,13)))
_X2gConfigPort2Datarate_Type.__name__=_B
_X2gConfigPort2Datarate_Object=MibTableColumn
x2gConfigPort2Datarate=_X2gConfigPort2Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,3),_X2gConfigPort2Datarate_Type())
x2gConfigPort2Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigPort2Datarate.setStatus(_A)
class _X2gConfigPort3Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_I,0),(_Af,1),(_AK,2),(_AL,3),(_AM,4),(_Ag,5),(_AN,6),(_J,7),(_K,8),(_Ah,9),(_AO,10),(_AP,11),(_Ae,12),(_Ai,13)))
_X2gConfigPort3Datarate_Type.__name__=_B
_X2gConfigPort3Datarate_Object=MibTableColumn
x2gConfigPort3Datarate=_X2gConfigPort3Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,4),_X2gConfigPort3Datarate_Type())
x2gConfigPort3Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigPort3Datarate.setStatus(_A)
class _X2gConfigPort4Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_I,0),(_Af,1),(_AK,2),(_AL,3),(_AM,4),(_Ag,5),(_AN,6),(_J,7),(_K,8),(_Ah,9),(_AO,10),(_AP,11),(_Ae,12),(_Ai,13)))
_X2gConfigPort4Datarate_Type.__name__=_B
_X2gConfigPort4Datarate_Object=MibTableColumn
x2gConfigPort4Datarate=_X2gConfigPort4Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,5),_X2gConfigPort4Datarate_Type())
x2gConfigPort4Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigPort4Datarate.setStatus(_A)
class _X2gConfigCrossConnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,5,9,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*(('disconnect',0),('alternate',1),('backup',5),('ringBackupWest',9),('multicast',11),('dropContinue',12),('addDropWest',13),('addDropEast',14),('ringBackupEast',15),('crossOver',16),('switchP1P2',17),('switchP1P3',18),('switchP1P4',19),(_L,20),(_B4,21)))
_X2gConfigCrossConnect_Type.__name__=_B
_X2gConfigCrossConnect_Object=MibTableColumn
x2gConfigCrossConnect=_X2gConfigCrossConnect_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,6),_X2gConfigCrossConnect_Type())
x2gConfigCrossConnect.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigCrossConnect.setStatus(_A)
class _X2gConfigDeactivatePort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_X2gConfigDeactivatePort1_Type.__name__=_B
_X2gConfigDeactivatePort1_Object=MibTableColumn
x2gConfigDeactivatePort1=_X2gConfigDeactivatePort1_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,7),_X2gConfigDeactivatePort1_Type())
x2gConfigDeactivatePort1.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigDeactivatePort1.setStatus(_A)
class _X2gConfigDeactivatePort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_X2gConfigDeactivatePort2_Type.__name__=_B
_X2gConfigDeactivatePort2_Object=MibTableColumn
x2gConfigDeactivatePort2=_X2gConfigDeactivatePort2_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,8),_X2gConfigDeactivatePort2_Type())
x2gConfigDeactivatePort2.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigDeactivatePort2.setStatus(_A)
class _X2gConfigDeactivatePort3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_X2gConfigDeactivatePort3_Type.__name__=_B
_X2gConfigDeactivatePort3_Object=MibTableColumn
x2gConfigDeactivatePort3=_X2gConfigDeactivatePort3_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,9),_X2gConfigDeactivatePort3_Type())
x2gConfigDeactivatePort3.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigDeactivatePort3.setStatus(_A)
class _X2gConfigDeactivatePort4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_X2gConfigDeactivatePort4_Type.__name__=_B
_X2gConfigDeactivatePort4_Object=MibTableColumn
x2gConfigDeactivatePort4=_X2gConfigDeactivatePort4_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,10),_X2gConfigDeactivatePort4_Type())
x2gConfigDeactivatePort4.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigDeactivatePort4.setStatus(_A)
class _X2gConfigFrontPanelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,7)));namedValues=NamedValues(*((_L,0),(_O,1),(_P,4),(_Q,5),(_R,7)))
_X2gConfigFrontPanelMode_Type.__name__=_B
_X2gConfigFrontPanelMode_Object=MibTableColumn
x2gConfigFrontPanelMode=_X2gConfigFrontPanelMode_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,11),_X2gConfigFrontPanelMode_Type())
x2gConfigFrontPanelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigFrontPanelMode.setStatus(_A)
class _X2gConfigLossOfSignalHandling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AQ,0),(_AR,1)))
_X2gConfigLossOfSignalHandling_Type.__name__=_B
_X2gConfigLossOfSignalHandling_Object=MibTableColumn
x2gConfigLossOfSignalHandling=_X2gConfigLossOfSignalHandling_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,12),_X2gConfigLossOfSignalHandling_Type())
x2gConfigLossOfSignalHandling.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigLossOfSignalHandling.setStatus(_A)
class _X2gConfigOptimizedFor8b10b_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_X2gConfigOptimizedFor8b10b_Type.__name__=_B
_X2gConfigOptimizedFor8b10b_Object=MibTableColumn
x2gConfigOptimizedFor8b10b=_X2gConfigOptimizedFor8b10b_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,13),_X2gConfigOptimizedFor8b10b_Type())
x2gConfigOptimizedFor8b10b.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigOptimizedFor8b10b.setStatus(_A)
class _X2gConfigBertPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6)));namedValues=NamedValues(*(('ms27',0),(_Ar,2),(_As,3),(_At,4),(_Au,5),(_Av,6)))
_X2gConfigBertPattern_Type.__name__=_B
_X2gConfigBertPattern_Object=MibTableColumn
x2gConfigBertPattern=_X2gConfigBertPattern_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,14),_X2gConfigBertPattern_Type())
x2gConfigBertPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigBertPattern.setStatus(_A)
class _X2gConfigSfpDeltaInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),(_AS,1),(_AT,2),(_AU,3),(_AV,4),(_AW,5),(_AX,6)))
_X2gConfigSfpDeltaInterval_Type.__name__=_B
_X2gConfigSfpDeltaInterval_Object=MibTableColumn
x2gConfigSfpDeltaInterval=_X2gConfigSfpDeltaInterval_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,15),_X2gConfigSfpDeltaInterval_Type())
x2gConfigSfpDeltaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigSfpDeltaInterval.setStatus(_A)
class _X2gConfigSfpDeltaThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_AY,0),(_AZ,1),(_Aa,2),(_Ab,3),(_Ac,4),(_Ad,5)))
_X2gConfigSfpDeltaThreshold_Type.__name__=_B
_X2gConfigSfpDeltaThreshold_Object=MibTableColumn
x2gConfigSfpDeltaThreshold=_X2gConfigSfpDeltaThreshold_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,16),_X2gConfigSfpDeltaThreshold_Type())
x2gConfigSfpDeltaThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigSfpDeltaThreshold.setStatus(_A)
class _X2gConfigBackupTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_B5,1),('clockLoss',2)))
_X2gConfigBackupTrigger_Type.__name__=_B
_X2gConfigBackupTrigger_Object=MibTableColumn
x2gConfigBackupTrigger=_X2gConfigBackupTrigger_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,17),_X2gConfigBackupTrigger_Type())
x2gConfigBackupTrigger.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigBackupTrigger.setStatus(_A)
class _X2gConfigStayWithLastLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_X2gConfigStayWithLastLink_Type.__name__=_B
_X2gConfigStayWithLastLink_Object=MibTableColumn
x2gConfigStayWithLastLink=_X2gConfigStayWithLastLink_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,18),_X2gConfigStayWithLastLink_Type())
x2gConfigStayWithLastLink.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigStayWithLastLink.setStatus(_A)
class _X2gConfigBackupEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Aw,0),(_Ax,1),(_Ay,2),(_Al,3)))
_X2gConfigBackupEnd_Type.__name__=_B
_X2gConfigBackupEnd_Object=MibTableColumn
x2gConfigBackupEnd=_X2gConfigBackupEnd_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,19),_X2gConfigBackupEnd_Type())
x2gConfigBackupEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigBackupEnd.setStatus(_A)
class _X2gConfigPermitLinkOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_X2gConfigPermitLinkOverride_Type.__name__=_B
_X2gConfigPermitLinkOverride_Object=MibTableColumn
x2gConfigPermitLinkOverride=_X2gConfigPermitLinkOverride_Object((1,3,6,1,4,1,3181,10,6,1,94,3,1,20),_X2gConfigPermitLinkOverride_Type())
x2gConfigPermitLinkOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:x2gConfigPermitLinkOverride.setStatus(_A)
_TxgConfigTable_Object=MibTable
txgConfigTable=_TxgConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,4))
if mibBuilder.loadTexts:txgConfigTable.setStatus(_A)
_TxgConfigEntry_Object=MibTableRow
txgConfigEntry=_TxgConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1))
txgConfigEntry.setIndexNames((0,_G,_B6))
if mibBuilder.loadTexts:txgConfigEntry.setStatus(_A)
class _TxgConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_TxgConfigIndex_Type.__name__=_B
_TxgConfigIndex_Object=MibTableColumn
txgConfigIndex=_TxgConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,1),_TxgConfigIndex_Type())
txgConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:txgConfigIndex.setStatus(_A)
class _TxgConfigTxgDatarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('oc192',1),(_Aj,2),('oc192Fec',3),('otu2',4),('ms10xFc',5),('otu2e',6),('otu1f',7),('otu2f',8)))
_TxgConfigTxgDatarate_Type.__name__=_B
_TxgConfigTxgDatarate_Object=MibTableColumn
txgConfigTxgDatarate=_TxgConfigTxgDatarate_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,2),_TxgConfigTxgDatarate_Type())
txgConfigTxgDatarate.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigTxgDatarate.setStatus(_A)
class _TxgConfigTxgOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5)));namedValues=NamedValues(*((_E,0),(_Az,2),('repeater',3),('bertPort1',4),('bertPort2',5)))
_TxgConfigTxgOperationMode_Type.__name__=_B
_TxgConfigTxgOperationMode_Object=MibTableColumn
txgConfigTxgOperationMode=_TxgConfigTxgOperationMode_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,3),_TxgConfigTxgOperationMode_Type())
txgConfigTxgOperationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigTxgOperationMode.setStatus(_A)
class _TxgConfigPort1ItuChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126)));namedValues=NamedValues(*((_S,0),(_T,22),(_U,24),(_V,26),(_W,28),(_X,30),(_Y,32),(_Z,34),(_a,36),(_b,38),(_c,40),(_d,42),(_e,44),(_f,46),(_g,48),(_h,50),(_i,52),(_j,54),(_k,56),(_l,58),(_m,60),(_n,62),(_o,64),(_p,66),(_q,68),(_r,70),(_s,72),(_t,74),(_u,76),(_v,78),(_w,80),(_x,82),(_y,84),(_z,86),(_A0,88),(_A1,90),(_A2,92),(_A3,94),(_A4,96),(_A5,98),(_A6,100),(_A7,102),(_A8,104),(_A9,106),(_AA,108),(_AB,110),(_AC,112),(_AD,114),(_AE,116),(_AF,118),(_AG,120),(_AH,122),(_AI,124),(_AJ,126)))
_TxgConfigPort1ItuChannel_Type.__name__=_B
_TxgConfigPort1ItuChannel_Object=MibTableColumn
txgConfigPort1ItuChannel=_TxgConfigPort1ItuChannel_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,4),_TxgConfigPort1ItuChannel_Type())
txgConfigPort1ItuChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigPort1ItuChannel.setStatus(_A)
class _TxgConfigPort2ItuChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126)));namedValues=NamedValues(*((_S,0),(_T,22),(_U,24),(_V,26),(_W,28),(_X,30),(_Y,32),(_Z,34),(_a,36),(_b,38),(_c,40),(_d,42),(_e,44),(_f,46),(_g,48),(_h,50),(_i,52),(_j,54),(_k,56),(_l,58),(_m,60),(_n,62),(_o,64),(_p,66),(_q,68),(_r,70),(_s,72),(_t,74),(_u,76),(_v,78),(_w,80),(_x,82),(_y,84),(_z,86),(_A0,88),(_A1,90),(_A2,92),(_A3,94),(_A4,96),(_A5,98),(_A6,100),(_A7,102),(_A8,104),(_A9,106),(_AA,108),(_AB,110),(_AC,112),(_AD,114),(_AE,116),(_AF,118),(_AG,120),(_AH,122),(_AI,124),(_AJ,126)))
_TxgConfigPort2ItuChannel_Type.__name__=_B
_TxgConfigPort2ItuChannel_Object=MibTableColumn
txgConfigPort2ItuChannel=_TxgConfigPort2ItuChannel_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,5),_TxgConfigPort2ItuChannel_Type())
txgConfigPort2ItuChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigPort2ItuChannel.setStatus(_A)
class _TxgConfigDeactivatePort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TxgConfigDeactivatePort1_Type.__name__=_B
_TxgConfigDeactivatePort1_Object=MibTableColumn
txgConfigDeactivatePort1=_TxgConfigDeactivatePort1_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,6),_TxgConfigDeactivatePort1_Type())
txgConfigDeactivatePort1.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigDeactivatePort1.setStatus(_A)
class _TxgConfigDeactivatePort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TxgConfigDeactivatePort2_Type.__name__=_B
_TxgConfigDeactivatePort2_Object=MibTableColumn
txgConfigDeactivatePort2=_TxgConfigDeactivatePort2_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,7),_TxgConfigDeactivatePort2_Type())
txgConfigDeactivatePort2.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigDeactivatePort2.setStatus(_A)
class _TxgConfigFrontPanelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,7)));namedValues=NamedValues(*((_L,0),(_O,1),(_P,4),(_Q,5),(_R,7)))
_TxgConfigFrontPanelMode_Type.__name__=_B
_TxgConfigFrontPanelMode_Object=MibTableColumn
txgConfigFrontPanelMode=_TxgConfigFrontPanelMode_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,8),_TxgConfigFrontPanelMode_Type())
txgConfigFrontPanelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigFrontPanelMode.setStatus(_A)
class _TxgConfigLossOfSignalHandling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AQ,0),(_AR,1)))
_TxgConfigLossOfSignalHandling_Type.__name__=_B
_TxgConfigLossOfSignalHandling_Object=MibTableColumn
txgConfigLossOfSignalHandling=_TxgConfigLossOfSignalHandling_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,9),_TxgConfigLossOfSignalHandling_Type())
txgConfigLossOfSignalHandling.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigLossOfSignalHandling.setStatus(_A)
class _TxgConfigBertPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6)));namedValues=NamedValues(*(('ms27',0),(_Ar,2),(_As,3),(_At,4),(_Au,5),(_Av,6)))
_TxgConfigBertPattern_Type.__name__=_B
_TxgConfigBertPattern_Object=MibTableColumn
txgConfigBertPattern=_TxgConfigBertPattern_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,10),_TxgConfigBertPattern_Type())
txgConfigBertPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigBertPattern.setStatus(_A)
class _TxgConfigSfpDeltaInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),(_AS,1),(_AT,2),(_AU,3),(_AV,4),(_AW,5),(_AX,6)))
_TxgConfigSfpDeltaInterval_Type.__name__=_B
_TxgConfigSfpDeltaInterval_Object=MibTableColumn
txgConfigSfpDeltaInterval=_TxgConfigSfpDeltaInterval_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,11),_TxgConfigSfpDeltaInterval_Type())
txgConfigSfpDeltaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigSfpDeltaInterval.setStatus(_A)
class _TxgConfigSfpDeltaThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_AY,0),(_AZ,1),(_Aa,2),(_Ab,3),(_Ac,4),(_Ad,5)))
_TxgConfigSfpDeltaThreshold_Type.__name__=_B
_TxgConfigSfpDeltaThreshold_Object=MibTableColumn
txgConfigSfpDeltaThreshold=_TxgConfigSfpDeltaThreshold_Object((1,3,6,1,4,1,3181,10,6,1,94,4,1,12),_TxgConfigSfpDeltaThreshold_Type())
txgConfigSfpDeltaThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:txgConfigSfpDeltaThreshold.setStatus(_A)
_CxgPlusConfigTable_Object=MibTable
cxgPlusConfigTable=_CxgPlusConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,5))
if mibBuilder.loadTexts:cxgPlusConfigTable.setStatus(_A)
_CxgPlusConfigEntry_Object=MibTableRow
cxgPlusConfigEntry=_CxgPlusConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1))
cxgPlusConfigEntry.setIndexNames((0,_G,_B7))
if mibBuilder.loadTexts:cxgPlusConfigEntry.setStatus(_A)
class _CxgPlusConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_CxgPlusConfigIndex_Type.__name__=_B
_CxgPlusConfigIndex_Object=MibTableColumn
cxgPlusConfigIndex=_CxgPlusConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,1),_CxgPlusConfigIndex_Type())
cxgPlusConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cxgPlusConfigIndex.setStatus(_A)
class _CxgPlusConfigCxgPort12Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_Am,1),(_Aj,2),(_A_,3)))
_CxgPlusConfigCxgPort12Datarate_Type.__name__=_B
_CxgPlusConfigCxgPort12Datarate_Object=MibTableColumn
cxgPlusConfigCxgPort12Datarate=_CxgPlusConfigCxgPort12Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,2),_CxgPlusConfigCxgPort12Datarate_Type())
cxgPlusConfigCxgPort12Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigCxgPort12Datarate.setStatus(_A)
class _CxgPlusConfigCxgPort34Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_Am,1),(_Aj,2),(_A_,3)))
_CxgPlusConfigCxgPort34Datarate_Type.__name__=_B
_CxgPlusConfigCxgPort34Datarate_Object=MibTableColumn
cxgPlusConfigCxgPort34Datarate=_CxgPlusConfigCxgPort34Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,3),_CxgPlusConfigCxgPort34Datarate_Type())
cxgPlusConfigCxgPort34Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigCxgPort34Datarate.setStatus(_A)
class _CxgPlusConfigPort1ItuChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126)));namedValues=NamedValues(*((_S,0),(_T,22),(_U,24),(_V,26),(_W,28),(_X,30),(_Y,32),(_Z,34),(_a,36),(_b,38),(_c,40),(_d,42),(_e,44),(_f,46),(_g,48),(_h,50),(_i,52),(_j,54),(_k,56),(_l,58),(_m,60),(_n,62),(_o,64),(_p,66),(_q,68),(_r,70),(_s,72),(_t,74),(_u,76),(_v,78),(_w,80),(_x,82),(_y,84),(_z,86),(_A0,88),(_A1,90),(_A2,92),(_A3,94),(_A4,96),(_A5,98),(_A6,100),(_A7,102),(_A8,104),(_A9,106),(_AA,108),(_AB,110),(_AC,112),(_AD,114),(_AE,116),(_AF,118),(_AG,120),(_AH,122),(_AI,124),(_AJ,126)))
_CxgPlusConfigPort1ItuChannel_Type.__name__=_B
_CxgPlusConfigPort1ItuChannel_Object=MibTableColumn
cxgPlusConfigPort1ItuChannel=_CxgPlusConfigPort1ItuChannel_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,4),_CxgPlusConfigPort1ItuChannel_Type())
cxgPlusConfigPort1ItuChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigPort1ItuChannel.setStatus(_A)
class _CxgPlusConfigPort2ItuChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126)));namedValues=NamedValues(*((_S,0),(_T,22),(_U,24),(_V,26),(_W,28),(_X,30),(_Y,32),(_Z,34),(_a,36),(_b,38),(_c,40),(_d,42),(_e,44),(_f,46),(_g,48),(_h,50),(_i,52),(_j,54),(_k,56),(_l,58),(_m,60),(_n,62),(_o,64),(_p,66),(_q,68),(_r,70),(_s,72),(_t,74),(_u,76),(_v,78),(_w,80),(_x,82),(_y,84),(_z,86),(_A0,88),(_A1,90),(_A2,92),(_A3,94),(_A4,96),(_A5,98),(_A6,100),(_A7,102),(_A8,104),(_A9,106),(_AA,108),(_AB,110),(_AC,112),(_AD,114),(_AE,116),(_AF,118),(_AG,120),(_AH,122),(_AI,124),(_AJ,126)))
_CxgPlusConfigPort2ItuChannel_Type.__name__=_B
_CxgPlusConfigPort2ItuChannel_Object=MibTableColumn
cxgPlusConfigPort2ItuChannel=_CxgPlusConfigPort2ItuChannel_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,5),_CxgPlusConfigPort2ItuChannel_Type())
cxgPlusConfigPort2ItuChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigPort2ItuChannel.setStatus(_A)
class _CxgPlusConfigPort3ItuChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126)));namedValues=NamedValues(*((_S,0),(_T,22),(_U,24),(_V,26),(_W,28),(_X,30),(_Y,32),(_Z,34),(_a,36),(_b,38),(_c,40),(_d,42),(_e,44),(_f,46),(_g,48),(_h,50),(_i,52),(_j,54),(_k,56),(_l,58),(_m,60),(_n,62),(_o,64),(_p,66),(_q,68),(_r,70),(_s,72),(_t,74),(_u,76),(_v,78),(_w,80),(_x,82),(_y,84),(_z,86),(_A0,88),(_A1,90),(_A2,92),(_A3,94),(_A4,96),(_A5,98),(_A6,100),(_A7,102),(_A8,104),(_A9,106),(_AA,108),(_AB,110),(_AC,112),(_AD,114),(_AE,116),(_AF,118),(_AG,120),(_AH,122),(_AI,124),(_AJ,126)))
_CxgPlusConfigPort3ItuChannel_Type.__name__=_B
_CxgPlusConfigPort3ItuChannel_Object=MibTableColumn
cxgPlusConfigPort3ItuChannel=_CxgPlusConfigPort3ItuChannel_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,6),_CxgPlusConfigPort3ItuChannel_Type())
cxgPlusConfigPort3ItuChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigPort3ItuChannel.setStatus(_A)
class _CxgPlusConfigPort4ItuChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126)));namedValues=NamedValues(*((_S,0),(_T,22),(_U,24),(_V,26),(_W,28),(_X,30),(_Y,32),(_Z,34),(_a,36),(_b,38),(_c,40),(_d,42),(_e,44),(_f,46),(_g,48),(_h,50),(_i,52),(_j,54),(_k,56),(_l,58),(_m,60),(_n,62),(_o,64),(_p,66),(_q,68),(_r,70),(_s,72),(_t,74),(_u,76),(_v,78),(_w,80),(_x,82),(_y,84),(_z,86),(_A0,88),(_A1,90),(_A2,92),(_A3,94),(_A4,96),(_A5,98),(_A6,100),(_A7,102),(_A8,104),(_A9,106),(_AA,108),(_AB,110),(_AC,112),(_AD,114),(_AE,116),(_AF,118),(_AG,120),(_AH,122),(_AI,124),(_AJ,126)))
_CxgPlusConfigPort4ItuChannel_Type.__name__=_B
_CxgPlusConfigPort4ItuChannel_Object=MibTableColumn
cxgPlusConfigPort4ItuChannel=_CxgPlusConfigPort4ItuChannel_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,7),_CxgPlusConfigPort4ItuChannel_Type())
cxgPlusConfigPort4ItuChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigPort4ItuChannel.setStatus(_A)
class _CxgPlusConfigDeactivatePort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CxgPlusConfigDeactivatePort1_Type.__name__=_B
_CxgPlusConfigDeactivatePort1_Object=MibTableColumn
cxgPlusConfigDeactivatePort1=_CxgPlusConfigDeactivatePort1_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,8),_CxgPlusConfigDeactivatePort1_Type())
cxgPlusConfigDeactivatePort1.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigDeactivatePort1.setStatus(_A)
class _CxgPlusConfigDeactivatePort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CxgPlusConfigDeactivatePort2_Type.__name__=_B
_CxgPlusConfigDeactivatePort2_Object=MibTableColumn
cxgPlusConfigDeactivatePort2=_CxgPlusConfigDeactivatePort2_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,9),_CxgPlusConfigDeactivatePort2_Type())
cxgPlusConfigDeactivatePort2.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigDeactivatePort2.setStatus(_A)
class _CxgPlusConfigDeactivatePort3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CxgPlusConfigDeactivatePort3_Type.__name__=_B
_CxgPlusConfigDeactivatePort3_Object=MibTableColumn
cxgPlusConfigDeactivatePort3=_CxgPlusConfigDeactivatePort3_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,10),_CxgPlusConfigDeactivatePort3_Type())
cxgPlusConfigDeactivatePort3.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigDeactivatePort3.setStatus(_A)
class _CxgPlusConfigDeactivatePort4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CxgPlusConfigDeactivatePort4_Type.__name__=_B
_CxgPlusConfigDeactivatePort4_Object=MibTableColumn
cxgPlusConfigDeactivatePort4=_CxgPlusConfigDeactivatePort4_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,11),_CxgPlusConfigDeactivatePort4_Type())
cxgPlusConfigDeactivatePort4.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigDeactivatePort4.setStatus(_A)
class _CxgPlusConfigFrontPanelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,7)));namedValues=NamedValues(*((_L,0),(_O,1),(_P,4),(_Q,5),(_R,7)))
_CxgPlusConfigFrontPanelMode_Type.__name__=_B
_CxgPlusConfigFrontPanelMode_Object=MibTableColumn
cxgPlusConfigFrontPanelMode=_CxgPlusConfigFrontPanelMode_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,12),_CxgPlusConfigFrontPanelMode_Type())
cxgPlusConfigFrontPanelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigFrontPanelMode.setStatus(_A)
class _CxgPlusConfigLossOfSignalHandling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AQ,0),(_AR,1)))
_CxgPlusConfigLossOfSignalHandling_Type.__name__=_B
_CxgPlusConfigLossOfSignalHandling_Object=MibTableColumn
cxgPlusConfigLossOfSignalHandling=_CxgPlusConfigLossOfSignalHandling_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,13),_CxgPlusConfigLossOfSignalHandling_Type())
cxgPlusConfigLossOfSignalHandling.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigLossOfSignalHandling.setStatus(_A)
class _CxgPlusConfigSfpDeltaInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),(_AS,1),(_AT,2),(_AU,3),(_AV,4),(_AW,5),(_AX,6)))
_CxgPlusConfigSfpDeltaInterval_Type.__name__=_B
_CxgPlusConfigSfpDeltaInterval_Object=MibTableColumn
cxgPlusConfigSfpDeltaInterval=_CxgPlusConfigSfpDeltaInterval_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,14),_CxgPlusConfigSfpDeltaInterval_Type())
cxgPlusConfigSfpDeltaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigSfpDeltaInterval.setStatus(_A)
class _CxgPlusConfigSfpDeltaThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_AY,0),(_AZ,1),(_Aa,2),(_Ab,3),(_Ac,4),(_Ad,5)))
_CxgPlusConfigSfpDeltaThreshold_Type.__name__=_B
_CxgPlusConfigSfpDeltaThreshold_Object=MibTableColumn
cxgPlusConfigSfpDeltaThreshold=_CxgPlusConfigSfpDeltaThreshold_Object((1,3,6,1,4,1,3181,10,6,1,94,5,1,15),_CxgPlusConfigSfpDeltaThreshold_Type())
cxgPlusConfigSfpDeltaThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgPlusConfigSfpDeltaThreshold.setStatus(_A)
_CxgConfigTable_Object=MibTable
cxgConfigTable=_CxgConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,6))
if mibBuilder.loadTexts:cxgConfigTable.setStatus(_A)
_CxgConfigEntry_Object=MibTableRow
cxgConfigEntry=_CxgConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1))
cxgConfigEntry.setIndexNames((0,_G,_B8))
if mibBuilder.loadTexts:cxgConfigEntry.setStatus(_A)
class _CxgConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_CxgConfigIndex_Type.__name__=_B
_CxgConfigIndex_Object=MibTableColumn
cxgConfigIndex=_CxgConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,1),_CxgConfigIndex_Type())
cxgConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cxgConfigIndex.setStatus(_A)
class _CxgConfigCxgPort12Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_Am,1),(_Aj,2),(_A_,3)))
_CxgConfigCxgPort12Datarate_Type.__name__=_B
_CxgConfigCxgPort12Datarate_Object=MibTableColumn
cxgConfigCxgPort12Datarate=_CxgConfigCxgPort12Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,2),_CxgConfigCxgPort12Datarate_Type())
cxgConfigCxgPort12Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgConfigCxgPort12Datarate.setStatus(_A)
class _CxgConfigPort1ItuChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126)));namedValues=NamedValues(*((_S,0),(_T,22),(_U,24),(_V,26),(_W,28),(_X,30),(_Y,32),(_Z,34),(_a,36),(_b,38),(_c,40),(_d,42),(_e,44),(_f,46),(_g,48),(_h,50),(_i,52),(_j,54),(_k,56),(_l,58),(_m,60),(_n,62),(_o,64),(_p,66),(_q,68),(_r,70),(_s,72),(_t,74),(_u,76),(_v,78),(_w,80),(_x,82),(_y,84),(_z,86),(_A0,88),(_A1,90),(_A2,92),(_A3,94),(_A4,96),(_A5,98),(_A6,100),(_A7,102),(_A8,104),(_A9,106),(_AA,108),(_AB,110),(_AC,112),(_AD,114),(_AE,116),(_AF,118),(_AG,120),(_AH,122),(_AI,124),(_AJ,126)))
_CxgConfigPort1ItuChannel_Type.__name__=_B
_CxgConfigPort1ItuChannel_Object=MibTableColumn
cxgConfigPort1ItuChannel=_CxgConfigPort1ItuChannel_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,3),_CxgConfigPort1ItuChannel_Type())
cxgConfigPort1ItuChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgConfigPort1ItuChannel.setStatus(_A)
class _CxgConfigPort2ItuChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126)));namedValues=NamedValues(*((_S,0),(_T,22),(_U,24),(_V,26),(_W,28),(_X,30),(_Y,32),(_Z,34),(_a,36),(_b,38),(_c,40),(_d,42),(_e,44),(_f,46),(_g,48),(_h,50),(_i,52),(_j,54),(_k,56),(_l,58),(_m,60),(_n,62),(_o,64),(_p,66),(_q,68),(_r,70),(_s,72),(_t,74),(_u,76),(_v,78),(_w,80),(_x,82),(_y,84),(_z,86),(_A0,88),(_A1,90),(_A2,92),(_A3,94),(_A4,96),(_A5,98),(_A6,100),(_A7,102),(_A8,104),(_A9,106),(_AA,108),(_AB,110),(_AC,112),(_AD,114),(_AE,116),(_AF,118),(_AG,120),(_AH,122),(_AI,124),(_AJ,126)))
_CxgConfigPort2ItuChannel_Type.__name__=_B
_CxgConfigPort2ItuChannel_Object=MibTableColumn
cxgConfigPort2ItuChannel=_CxgConfigPort2ItuChannel_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,4),_CxgConfigPort2ItuChannel_Type())
cxgConfigPort2ItuChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgConfigPort2ItuChannel.setStatus(_A)
class _CxgConfigDeactivatePort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CxgConfigDeactivatePort1_Type.__name__=_B
_CxgConfigDeactivatePort1_Object=MibTableColumn
cxgConfigDeactivatePort1=_CxgConfigDeactivatePort1_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,5),_CxgConfigDeactivatePort1_Type())
cxgConfigDeactivatePort1.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgConfigDeactivatePort1.setStatus(_A)
class _CxgConfigDeactivatePort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CxgConfigDeactivatePort2_Type.__name__=_B
_CxgConfigDeactivatePort2_Object=MibTableColumn
cxgConfigDeactivatePort2=_CxgConfigDeactivatePort2_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,6),_CxgConfigDeactivatePort2_Type())
cxgConfigDeactivatePort2.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgConfigDeactivatePort2.setStatus(_A)
class _CxgConfigFrontPanelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,7)));namedValues=NamedValues(*((_L,0),(_O,1),(_P,4),(_Q,5),(_R,7)))
_CxgConfigFrontPanelMode_Type.__name__=_B
_CxgConfigFrontPanelMode_Object=MibTableColumn
cxgConfigFrontPanelMode=_CxgConfigFrontPanelMode_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,7),_CxgConfigFrontPanelMode_Type())
cxgConfigFrontPanelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgConfigFrontPanelMode.setStatus(_A)
class _CxgConfigLossOfSignalHandling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AQ,0),(_AR,1)))
_CxgConfigLossOfSignalHandling_Type.__name__=_B
_CxgConfigLossOfSignalHandling_Object=MibTableColumn
cxgConfigLossOfSignalHandling=_CxgConfigLossOfSignalHandling_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,8),_CxgConfigLossOfSignalHandling_Type())
cxgConfigLossOfSignalHandling.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgConfigLossOfSignalHandling.setStatus(_A)
class _CxgConfigSfpDeltaInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),(_AS,1),(_AT,2),(_AU,3),(_AV,4),(_AW,5),(_AX,6)))
_CxgConfigSfpDeltaInterval_Type.__name__=_B
_CxgConfigSfpDeltaInterval_Object=MibTableColumn
cxgConfigSfpDeltaInterval=_CxgConfigSfpDeltaInterval_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,9),_CxgConfigSfpDeltaInterval_Type())
cxgConfigSfpDeltaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgConfigSfpDeltaInterval.setStatus(_A)
class _CxgConfigSfpDeltaThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_AY,0),(_AZ,1),(_Aa,2),(_Ab,3),(_Ac,4),(_Ad,5)))
_CxgConfigSfpDeltaThreshold_Type.__name__=_B
_CxgConfigSfpDeltaThreshold_Object=MibTableColumn
cxgConfigSfpDeltaThreshold=_CxgConfigSfpDeltaThreshold_Object((1,3,6,1,4,1,3181,10,6,1,94,6,1,10),_CxgConfigSfpDeltaThreshold_Type())
cxgConfigSfpDeltaThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cxgConfigSfpDeltaThreshold.setStatus(_A)
_T4gConfigTable_Object=MibTable
t4gConfigTable=_T4gConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,7))
if mibBuilder.loadTexts:t4gConfigTable.setStatus(_A)
_T4gConfigEntry_Object=MibTableRow
t4gConfigEntry=_T4gConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1))
t4gConfigEntry.setIndexNames((0,_G,_B9))
if mibBuilder.loadTexts:t4gConfigEntry.setStatus(_A)
class _T4gConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_T4gConfigIndex_Type.__name__=_B
_T4gConfigIndex_Object=MibTableColumn
t4gConfigIndex=_T4gConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,1),_T4gConfigIndex_Type())
t4gConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:t4gConfigIndex.setStatus(_A)
class _T4gConfigT4gPort12Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,6,7,8,10,11,12,14)));namedValues=NamedValues(*((_I,0),(_AK,2),(_AL,3),(_AM,4),(_AN,6),(_J,7),(_K,8),(_AO,10),(_AP,11),(_BA,12),(_B0,14)))
_T4gConfigT4gPort12Datarate_Type.__name__=_B
_T4gConfigT4gPort12Datarate_Object=MibTableColumn
t4gConfigT4gPort12Datarate=_T4gConfigT4gPort12Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,2),_T4gConfigT4gPort12Datarate_Type())
t4gConfigT4gPort12Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigT4gPort12Datarate.setStatus(_A)
class _T4gConfigT4gPort34Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,6,7,8,10,11,12,14)));namedValues=NamedValues(*((_I,0),(_AK,2),(_AL,3),(_AM,4),(_AN,6),(_J,7),(_K,8),(_AO,10),(_AP,11),(_BA,12),(_B0,14)))
_T4gConfigT4gPort34Datarate_Type.__name__=_B
_T4gConfigT4gPort34Datarate_Object=MibTableColumn
t4gConfigT4gPort34Datarate=_T4gConfigT4gPort34Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,3),_T4gConfigT4gPort34Datarate_Type())
t4gConfigT4gPort34Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigT4gPort34Datarate.setStatus(_A)
class _T4gConfigT4gOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_Az,1),(_B4,2)))
_T4gConfigT4gOperationMode_Type.__name__=_B
_T4gConfigT4gOperationMode_Object=MibTableColumn
t4gConfigT4gOperationMode=_T4gConfigT4gOperationMode_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,4),_T4gConfigT4gOperationMode_Type())
t4gConfigT4gOperationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigT4gOperationMode.setStatus(_A)
class _T4gConfigDeactivatePort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_T4gConfigDeactivatePort1_Type.__name__=_B
_T4gConfigDeactivatePort1_Object=MibTableColumn
t4gConfigDeactivatePort1=_T4gConfigDeactivatePort1_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,5),_T4gConfigDeactivatePort1_Type())
t4gConfigDeactivatePort1.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigDeactivatePort1.setStatus(_A)
class _T4gConfigDeactivatePort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_T4gConfigDeactivatePort2_Type.__name__=_B
_T4gConfigDeactivatePort2_Object=MibTableColumn
t4gConfigDeactivatePort2=_T4gConfigDeactivatePort2_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,6),_T4gConfigDeactivatePort2_Type())
t4gConfigDeactivatePort2.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigDeactivatePort2.setStatus(_A)
class _T4gConfigDeactivatePort3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_T4gConfigDeactivatePort3_Type.__name__=_B
_T4gConfigDeactivatePort3_Object=MibTableColumn
t4gConfigDeactivatePort3=_T4gConfigDeactivatePort3_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,7),_T4gConfigDeactivatePort3_Type())
t4gConfigDeactivatePort3.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigDeactivatePort3.setStatus(_A)
class _T4gConfigDeactivatePort4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_T4gConfigDeactivatePort4_Type.__name__=_B
_T4gConfigDeactivatePort4_Object=MibTableColumn
t4gConfigDeactivatePort4=_T4gConfigDeactivatePort4_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,8),_T4gConfigDeactivatePort4_Type())
t4gConfigDeactivatePort4.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigDeactivatePort4.setStatus(_A)
class _T4gConfigFrontPanelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,7)));namedValues=NamedValues(*((_L,0),(_O,1),(_P,4),(_Q,5),(_R,7)))
_T4gConfigFrontPanelMode_Type.__name__=_B
_T4gConfigFrontPanelMode_Object=MibTableColumn
t4gConfigFrontPanelMode=_T4gConfigFrontPanelMode_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,9),_T4gConfigFrontPanelMode_Type())
t4gConfigFrontPanelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigFrontPanelMode.setStatus(_A)
class _T4gConfigLossOfSignalHandling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AQ,0),(_AR,1)))
_T4gConfigLossOfSignalHandling_Type.__name__=_B
_T4gConfigLossOfSignalHandling_Object=MibTableColumn
t4gConfigLossOfSignalHandling=_T4gConfigLossOfSignalHandling_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,10),_T4gConfigLossOfSignalHandling_Type())
t4gConfigLossOfSignalHandling.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigLossOfSignalHandling.setStatus(_A)
class _T4gConfigBertPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6)));namedValues=NamedValues(*(('ms27',0),(_Ar,2),(_As,3),(_At,4),(_Au,5),(_Av,6)))
_T4gConfigBertPattern_Type.__name__=_B
_T4gConfigBertPattern_Object=MibTableColumn
t4gConfigBertPattern=_T4gConfigBertPattern_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,11),_T4gConfigBertPattern_Type())
t4gConfigBertPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigBertPattern.setStatus(_A)
class _T4gConfigSfpDeltaInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),(_AS,1),(_AT,2),(_AU,3),(_AV,4),(_AW,5),(_AX,6)))
_T4gConfigSfpDeltaInterval_Type.__name__=_B
_T4gConfigSfpDeltaInterval_Object=MibTableColumn
t4gConfigSfpDeltaInterval=_T4gConfigSfpDeltaInterval_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,12),_T4gConfigSfpDeltaInterval_Type())
t4gConfigSfpDeltaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigSfpDeltaInterval.setStatus(_A)
class _T4gConfigSfpDeltaThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_AY,0),(_AZ,1),(_Aa,2),(_Ab,3),(_Ac,4),(_Ad,5)))
_T4gConfigSfpDeltaThreshold_Type.__name__=_B
_T4gConfigSfpDeltaThreshold_Object=MibTableColumn
t4gConfigSfpDeltaThreshold=_T4gConfigSfpDeltaThreshold_Object((1,3,6,1,4,1,3181,10,6,1,94,7,1,13),_T4gConfigSfpDeltaThreshold_Type())
t4gConfigSfpDeltaThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:t4gConfigSfpDeltaThreshold.setStatus(_A)
_M2gConfigTable_Object=MibTable
m2gConfigTable=_M2gConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,8))
if mibBuilder.loadTexts:m2gConfigTable.setStatus(_A)
_M2gConfigEntry_Object=MibTableRow
m2gConfigEntry=_M2gConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1))
m2gConfigEntry.setIndexNames((0,_G,_BB))
if mibBuilder.loadTexts:m2gConfigEntry.setStatus(_A)
class _M2gConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_M2gConfigIndex_Type.__name__=_B
_M2gConfigIndex_Object=MibTableColumn
m2gConfigIndex=_M2gConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,1),_M2gConfigIndex_Type())
m2gConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:m2gConfigIndex.setStatus(_A)
class _M2gConfigChannel1Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_K,1),(_J,2)))
_M2gConfigChannel1Datarate_Type.__name__=_B
_M2gConfigChannel1Datarate_Object=MibTableColumn
m2gConfigChannel1Datarate=_M2gConfigChannel1Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,2),_M2gConfigChannel1Datarate_Type())
m2gConfigChannel1Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigChannel1Datarate.setStatus(_A)
class _M2gConfigChannel2Datarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_K,1),(_J,2)))
_M2gConfigChannel2Datarate_Type.__name__=_B
_M2gConfigChannel2Datarate_Object=MibTableColumn
m2gConfigChannel2Datarate=_M2gConfigChannel2Datarate_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,3),_M2gConfigChannel2Datarate_Type())
m2gConfigChannel2Datarate.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigChannel2Datarate.setStatus(_A)
class _M2gConfigPort1CopperSfp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_M2gConfigPort1CopperSfp_Type.__name__=_B
_M2gConfigPort1CopperSfp_Object=MibTableColumn
m2gConfigPort1CopperSfp=_M2gConfigPort1CopperSfp_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,4),_M2gConfigPort1CopperSfp_Type())
m2gConfigPort1CopperSfp.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigPort1CopperSfp.setStatus(_A)
class _M2gConfigPort2CopperSfp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_M2gConfigPort2CopperSfp_Type.__name__=_B
_M2gConfigPort2CopperSfp_Object=MibTableColumn
m2gConfigPort2CopperSfp=_M2gConfigPort2CopperSfp_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,5),_M2gConfigPort2CopperSfp_Type())
m2gConfigPort2CopperSfp.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigPort2CopperSfp.setStatus(_A)
class _M2gConfigSfpDeltaInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),(_AS,1),(_AT,2),(_AU,3),(_AV,4),(_AW,5),(_AX,6)))
_M2gConfigSfpDeltaInterval_Type.__name__=_B
_M2gConfigSfpDeltaInterval_Object=MibTableColumn
m2gConfigSfpDeltaInterval=_M2gConfigSfpDeltaInterval_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,6),_M2gConfigSfpDeltaInterval_Type())
m2gConfigSfpDeltaInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigSfpDeltaInterval.setStatus(_A)
class _M2gConfigSfpDeltaThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_AY,0),(_AZ,1),(_Aa,2),(_Ab,3),(_Ac,4),(_Ad,5)))
_M2gConfigSfpDeltaThreshold_Type.__name__=_B
_M2gConfigSfpDeltaThreshold_Object=MibTableColumn
m2gConfigSfpDeltaThreshold=_M2gConfigSfpDeltaThreshold_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,7),_M2gConfigSfpDeltaThreshold_Type())
m2gConfigSfpDeltaThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigSfpDeltaThreshold.setStatus(_A)
class _M2gConfigLinkBackupTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_B5,1),('errorBurst',2)))
_M2gConfigLinkBackupTrigger_Type.__name__=_B
_M2gConfigLinkBackupTrigger_Object=MibTableColumn
m2gConfigLinkBackupTrigger=_M2gConfigLinkBackupTrigger_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,8),_M2gConfigLinkBackupTrigger_Type())
m2gConfigLinkBackupTrigger.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigLinkBackupTrigger.setStatus(_A)
class _M2gConfigStayWithLastLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_M2gConfigStayWithLastLink_Type.__name__=_B
_M2gConfigStayWithLastLink_Object=MibTableColumn
m2gConfigStayWithLastLink=_M2gConfigStayWithLastLink_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,9),_M2gConfigStayWithLastLink_Type())
m2gConfigStayWithLastLink.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigStayWithLastLink.setStatus(_A)
class _M2gConfigBackupEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Aw,0),(_Ax,1),(_Ay,2),(_Al,3)))
_M2gConfigBackupEnd_Type.__name__=_B
_M2gConfigBackupEnd_Object=MibTableColumn
m2gConfigBackupEnd=_M2gConfigBackupEnd_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,10),_M2gConfigBackupEnd_Type())
m2gConfigBackupEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigBackupEnd.setStatus(_A)
class _M2gConfigPermitLinkOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_M2gConfigPermitLinkOverride_Type.__name__=_B
_M2gConfigPermitLinkOverride_Object=MibTableColumn
m2gConfigPermitLinkOverride=_M2gConfigPermitLinkOverride_Object((1,3,6,1,4,1,3181,10,6,1,94,8,1,11),_M2gConfigPermitLinkOverride_Type())
m2gConfigPermitLinkOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:m2gConfigPermitLinkOverride.setStatus(_A)
_Om1ConfigTable_Object=MibTable
om1ConfigTable=_Om1ConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,9))
if mibBuilder.loadTexts:om1ConfigTable.setStatus(_A)
_Om1ConfigEntry_Object=MibTableRow
om1ConfigEntry=_Om1ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,9,1))
om1ConfigEntry.setIndexNames((0,_G,_BC))
if mibBuilder.loadTexts:om1ConfigEntry.setStatus(_A)
class _Om1ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Om1ConfigIndex_Type.__name__=_B
_Om1ConfigIndex_Object=MibTableColumn
om1ConfigIndex=_Om1ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,9,1,1),_Om1ConfigIndex_Type())
om1ConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:om1ConfigIndex.setStatus(_A)
class _Om1ConfigWavelengthPortA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_An,0),(_Ao,1),(_E,3)))
_Om1ConfigWavelengthPortA_Type.__name__=_B
_Om1ConfigWavelengthPortA_Object=MibTableColumn
om1ConfigWavelengthPortA=_Om1ConfigWavelengthPortA_Object((1,3,6,1,4,1,3181,10,6,1,94,9,1,2),_Om1ConfigWavelengthPortA_Type())
om1ConfigWavelengthPortA.setMaxAccess(_C)
if mibBuilder.loadTexts:om1ConfigWavelengthPortA.setStatus(_A)
_Om1ConfigLowThresholdPortA_Type=DisplayString
_Om1ConfigLowThresholdPortA_Object=MibTableColumn
om1ConfigLowThresholdPortA=_Om1ConfigLowThresholdPortA_Object((1,3,6,1,4,1,3181,10,6,1,94,9,1,3),_Om1ConfigLowThresholdPortA_Type())
om1ConfigLowThresholdPortA.setMaxAccess(_C)
if mibBuilder.loadTexts:om1ConfigLowThresholdPortA.setStatus(_A)
_Om1ConfigHighThresholdPortA_Type=DisplayString
_Om1ConfigHighThresholdPortA_Object=MibTableColumn
om1ConfigHighThresholdPortA=_Om1ConfigHighThresholdPortA_Object((1,3,6,1,4,1,3181,10,6,1,94,9,1,4),_Om1ConfigHighThresholdPortA_Type())
om1ConfigHighThresholdPortA.setMaxAccess(_C)
if mibBuilder.loadTexts:om1ConfigHighThresholdPortA.setStatus(_A)
class _Om1ConfigWavelengthPortB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_An,0),(_Ao,1),(_E,3)))
_Om1ConfigWavelengthPortB_Type.__name__=_B
_Om1ConfigWavelengthPortB_Object=MibTableColumn
om1ConfigWavelengthPortB=_Om1ConfigWavelengthPortB_Object((1,3,6,1,4,1,3181,10,6,1,94,9,1,5),_Om1ConfigWavelengthPortB_Type())
om1ConfigWavelengthPortB.setMaxAccess(_C)
if mibBuilder.loadTexts:om1ConfigWavelengthPortB.setStatus(_A)
_Om1ConfigLowThresholdPortB_Type=DisplayString
_Om1ConfigLowThresholdPortB_Object=MibTableColumn
om1ConfigLowThresholdPortB=_Om1ConfigLowThresholdPortB_Object((1,3,6,1,4,1,3181,10,6,1,94,9,1,6),_Om1ConfigLowThresholdPortB_Type())
om1ConfigLowThresholdPortB.setMaxAccess(_C)
if mibBuilder.loadTexts:om1ConfigLowThresholdPortB.setStatus(_A)
_Om1ConfigHighThresholdPortB_Type=DisplayString
_Om1ConfigHighThresholdPortB_Object=MibTableColumn
om1ConfigHighThresholdPortB=_Om1ConfigHighThresholdPortB_Object((1,3,6,1,4,1,3181,10,6,1,94,9,1,7),_Om1ConfigHighThresholdPortB_Type())
om1ConfigHighThresholdPortB.setMaxAccess(_C)
if mibBuilder.loadTexts:om1ConfigHighThresholdPortB.setStatus(_A)
class _Om1ConfigFrontPanelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,7)));namedValues=NamedValues(*((_L,0),(_O,1),(_P,4),(_Q,5),(_R,7)))
_Om1ConfigFrontPanelMode_Type.__name__=_B
_Om1ConfigFrontPanelMode_Object=MibTableColumn
om1ConfigFrontPanelMode=_Om1ConfigFrontPanelMode_Object((1,3,6,1,4,1,3181,10,6,1,94,9,1,8),_Om1ConfigFrontPanelMode_Type())
om1ConfigFrontPanelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:om1ConfigFrontPanelMode.setStatus(_A)
_Lp1ConfigTable_Object=MibTable
lp1ConfigTable=_Lp1ConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,10))
if mibBuilder.loadTexts:lp1ConfigTable.setStatus(_A)
_Lp1ConfigEntry_Object=MibTableRow
lp1ConfigEntry=_Lp1ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1))
lp1ConfigEntry.setIndexNames((0,_G,_BD))
if mibBuilder.loadTexts:lp1ConfigEntry.setStatus(_A)
class _Lp1ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_Lp1ConfigIndex_Type.__name__=_B
_Lp1ConfigIndex_Object=MibTableColumn
lp1ConfigIndex=_Lp1ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,1),_Lp1ConfigIndex_Type())
lp1ConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lp1ConfigIndex.setStatus(_A)
class _Lp1ConfigWavelengthPortA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_An,0),(_Ao,1),(_E,3)))
_Lp1ConfigWavelengthPortA_Type.__name__=_B
_Lp1ConfigWavelengthPortA_Object=MibTableColumn
lp1ConfigWavelengthPortA=_Lp1ConfigWavelengthPortA_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,2),_Lp1ConfigWavelengthPortA_Type())
lp1ConfigWavelengthPortA.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigWavelengthPortA.setStatus(_A)
_Lp1ConfigLowThresholdPortA_Type=DisplayString
_Lp1ConfigLowThresholdPortA_Object=MibTableColumn
lp1ConfigLowThresholdPortA=_Lp1ConfigLowThresholdPortA_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,3),_Lp1ConfigLowThresholdPortA_Type())
lp1ConfigLowThresholdPortA.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigLowThresholdPortA.setStatus(_A)
_Lp1ConfigHighThresholdPortA_Type=DisplayString
_Lp1ConfigHighThresholdPortA_Object=MibTableColumn
lp1ConfigHighThresholdPortA=_Lp1ConfigHighThresholdPortA_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,4),_Lp1ConfigHighThresholdPortA_Type())
lp1ConfigHighThresholdPortA.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigHighThresholdPortA.setStatus(_A)
class _Lp1ConfigWavelengthPortB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_An,0),(_Ao,1),(_E,3)))
_Lp1ConfigWavelengthPortB_Type.__name__=_B
_Lp1ConfigWavelengthPortB_Object=MibTableColumn
lp1ConfigWavelengthPortB=_Lp1ConfigWavelengthPortB_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,5),_Lp1ConfigWavelengthPortB_Type())
lp1ConfigWavelengthPortB.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigWavelengthPortB.setStatus(_A)
_Lp1ConfigLowThresholdPortB_Type=DisplayString
_Lp1ConfigLowThresholdPortB_Object=MibTableColumn
lp1ConfigLowThresholdPortB=_Lp1ConfigLowThresholdPortB_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,6),_Lp1ConfigLowThresholdPortB_Type())
lp1ConfigLowThresholdPortB.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigLowThresholdPortB.setStatus(_A)
_Lp1ConfigHighThresholdPortB_Type=DisplayString
_Lp1ConfigHighThresholdPortB_Object=MibTableColumn
lp1ConfigHighThresholdPortB=_Lp1ConfigHighThresholdPortB_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,7),_Lp1ConfigHighThresholdPortB_Type())
lp1ConfigHighThresholdPortB.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigHighThresholdPortB.setStatus(_A)
class _Lp1ConfigBackupCriteria_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_BE,0),('signalHigh',1),(_Al,2)))
_Lp1ConfigBackupCriteria_Type.__name__=_B
_Lp1ConfigBackupCriteria_Object=MibTableColumn
lp1ConfigBackupCriteria=_Lp1ConfigBackupCriteria_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,8),_Lp1ConfigBackupCriteria_Type())
lp1ConfigBackupCriteria.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigBackupCriteria.setStatus(_A)
class _Lp1ConfigStayWithLastLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Lp1ConfigStayWithLastLink_Type.__name__=_B
_Lp1ConfigStayWithLastLink_Object=MibTableColumn
lp1ConfigStayWithLastLink=_Lp1ConfigStayWithLastLink_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,9),_Lp1ConfigStayWithLastLink_Type())
lp1ConfigStayWithLastLink.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigStayWithLastLink.setStatus(_A)
class _Lp1ConfigBackupEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Aw,0),(_Ax,1),(_Ay,2),(_Al,3)))
_Lp1ConfigBackupEnd_Type.__name__=_B
_Lp1ConfigBackupEnd_Object=MibTableColumn
lp1ConfigBackupEnd=_Lp1ConfigBackupEnd_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,10),_Lp1ConfigBackupEnd_Type())
lp1ConfigBackupEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigBackupEnd.setStatus(_A)
class _Lp1ConfigFrontPanelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,7)));namedValues=NamedValues(*((_L,0),(_O,1),(_P,4),(_Q,5),(_R,7)))
_Lp1ConfigFrontPanelMode_Type.__name__=_B
_Lp1ConfigFrontPanelMode_Object=MibTableColumn
lp1ConfigFrontPanelMode=_Lp1ConfigFrontPanelMode_Object((1,3,6,1,4,1,3181,10,6,1,94,10,1,11),_Lp1ConfigFrontPanelMode_Type())
lp1ConfigFrontPanelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lp1ConfigFrontPanelMode.setStatus(_A)
_EmConfigTable_Object=MibTable
emConfigTable=_EmConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,94,11))
if mibBuilder.loadTexts:emConfigTable.setStatus(_A)
_EmConfigEntry_Object=MibTableRow
emConfigEntry=_EmConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1))
emConfigEntry.setIndexNames((0,_G,_BF))
if mibBuilder.loadTexts:emConfigEntry.setStatus(_A)
class _EmConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_EmConfigIndex_Type.__name__=_B
_EmConfigIndex_Object=MibTableColumn
emConfigIndex=_EmConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,1),_EmConfigIndex_Type())
emConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:emConfigIndex.setStatus(_A)
class _EmConfigEdfaOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*(('preAmp',0),('booster',1),('pumpDisabled',3)))
_EmConfigEdfaOperationMode_Type.__name__=_B
_EmConfigEdfaOperationMode_Object=MibTableColumn
emConfigEdfaOperationMode=_EmConfigEdfaOperationMode_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,2),_EmConfigEdfaOperationMode_Type())
emConfigEdfaOperationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:emConfigEdfaOperationMode.setStatus(_A)
class _EmConfigLossOfSignalHandling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AQ,0),(_AR,1)))
_EmConfigLossOfSignalHandling_Type.__name__=_B
_EmConfigLossOfSignalHandling_Object=MibTableColumn
emConfigLossOfSignalHandling=_EmConfigLossOfSignalHandling_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,3),_EmConfigLossOfSignalHandling_Type())
emConfigLossOfSignalHandling.setMaxAccess(_C)
if mibBuilder.loadTexts:emConfigLossOfSignalHandling.setStatus(_A)
_EmConfigSignalGain_Type=DisplayString
_EmConfigSignalGain_Object=MibTableColumn
emConfigSignalGain=_EmConfigSignalGain_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,4),_EmConfigSignalGain_Type())
emConfigSignalGain.setMaxAccess(_C)
if mibBuilder.loadTexts:emConfigSignalGain.setStatus(_A)
_EmConfigMaxOutputPower_Type=DisplayString
_EmConfigMaxOutputPower_Object=MibTableColumn
emConfigMaxOutputPower=_EmConfigMaxOutputPower_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,5),_EmConfigMaxOutputPower_Type())
emConfigMaxOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:emConfigMaxOutputPower.setStatus(_A)
_EmConfigLowThresholdEdfaIn_Type=DisplayString
_EmConfigLowThresholdEdfaIn_Object=MibTableColumn
emConfigLowThresholdEdfaIn=_EmConfigLowThresholdEdfaIn_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,6),_EmConfigLowThresholdEdfaIn_Type())
emConfigLowThresholdEdfaIn.setMaxAccess(_C)
if mibBuilder.loadTexts:emConfigLowThresholdEdfaIn.setStatus(_A)
_EmConfigHighThresholdEdfaIn_Type=DisplayString
_EmConfigHighThresholdEdfaIn_Object=MibTableColumn
emConfigHighThresholdEdfaIn=_EmConfigHighThresholdEdfaIn_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,7),_EmConfigHighThresholdEdfaIn_Type())
emConfigHighThresholdEdfaIn.setMaxAccess(_C)
if mibBuilder.loadTexts:emConfigHighThresholdEdfaIn.setStatus(_A)
_EmConfigLowThresholdPortB_Type=DisplayString
_EmConfigLowThresholdPortB_Object=MibTableColumn
emConfigLowThresholdPortB=_EmConfigLowThresholdPortB_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,8),_EmConfigLowThresholdPortB_Type())
emConfigLowThresholdPortB.setMaxAccess(_C)
if mibBuilder.loadTexts:emConfigLowThresholdPortB.setStatus(_A)
_EmConfigHighThresholdPortB_Type=DisplayString
_EmConfigHighThresholdPortB_Object=MibTableColumn
emConfigHighThresholdPortB=_EmConfigHighThresholdPortB_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,9),_EmConfigHighThresholdPortB_Type())
emConfigHighThresholdPortB.setMaxAccess(_C)
if mibBuilder.loadTexts:emConfigHighThresholdPortB.setStatus(_A)
class _EmConfigFrontPanelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,7)));namedValues=NamedValues(*((_L,0),(_O,1),(_P,4),(_Q,5),(_R,7)))
_EmConfigFrontPanelMode_Type.__name__=_B
_EmConfigFrontPanelMode_Object=MibTableColumn
emConfigFrontPanelMode=_EmConfigFrontPanelMode_Object((1,3,6,1,4,1,3181,10,6,1,94,11,1,10),_EmConfigFrontPanelMode_Type())
emConfigFrontPanelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:emConfigFrontPanelMode.setStatus(_A)
_ModuleControlTable_Object=MibTable
moduleControlTable=_ModuleControlTable_Object((1,3,6,1,4,1,3181,10,6,1,94,12))
if mibBuilder.loadTexts:moduleControlTable.setStatus(_A)
_ModuleControlEntry_Object=MibTableRow
moduleControlEntry=_ModuleControlEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1))
moduleControlEntry.setIndexNames((0,_G,_BG))
if mibBuilder.loadTexts:moduleControlEntry.setStatus(_A)
class _ModuleControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_ModuleControlIndex_Type.__name__=_B
_ModuleControlIndex_Object=MibTableColumn
moduleControlIndex=_ModuleControlIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,1),_ModuleControlIndex_Type())
moduleControlIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:moduleControlIndex.setStatus(_A)
_ModuleControlEnterPassword_Type=DisplayString
_ModuleControlEnterPassword_Object=MibTableColumn
moduleControlEnterPassword=_ModuleControlEnterPassword_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,2),_ModuleControlEnterPassword_Type())
moduleControlEnterPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlEnterPassword.setStatus(_A)
_ModuleControlRebootModule_Type=DisplayString
_ModuleControlRebootModule_Object=MibTableColumn
moduleControlRebootModule=_ModuleControlRebootModule_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,3),_ModuleControlRebootModule_Type())
moduleControlRebootModule.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlRebootModule.setStatus(_A)
_ModuleControlWarmStart_Type=DisplayString
_ModuleControlWarmStart_Object=MibTableColumn
moduleControlWarmStart=_ModuleControlWarmStart_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,4),_ModuleControlWarmStart_Type())
moduleControlWarmStart.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlWarmStart.setStatus(_A)
_ModuleControlClearCounter_Type=DisplayString
_ModuleControlClearCounter_Object=MibTableColumn
moduleControlClearCounter=_ModuleControlClearCounter_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,5),_ModuleControlClearCounter_Type())
moduleControlClearCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlClearCounter.setStatus(_A)
_ModuleControlSwitchOffBackup_Type=DisplayString
_ModuleControlSwitchOffBackup_Object=MibTableColumn
moduleControlSwitchOffBackup=_ModuleControlSwitchOffBackup_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,6),_ModuleControlSwitchOffBackup_Type())
moduleControlSwitchOffBackup.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlSwitchOffBackup.setStatus(_A)
_ModuleControlSwitchToBackup_Type=DisplayString
_ModuleControlSwitchToBackup_Object=MibTableColumn
moduleControlSwitchToBackup=_ModuleControlSwitchToBackup_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,7),_ModuleControlSwitchToBackup_Type())
moduleControlSwitchToBackup.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlSwitchToBackup.setStatus(_A)
_ModuleControlAutomaticBackup_Type=DisplayString
_ModuleControlAutomaticBackup_Object=MibTableColumn
moduleControlAutomaticBackup=_ModuleControlAutomaticBackup_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,8),_ModuleControlAutomaticBackup_Type())
moduleControlAutomaticBackup.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlAutomaticBackup.setStatus(_A)
_ModuleControlWriteDisplay_Type=DisplayString
_ModuleControlWriteDisplay_Object=MibTableColumn
moduleControlWriteDisplay=_ModuleControlWriteDisplay_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,9),_ModuleControlWriteDisplay_Type())
moduleControlWriteDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlWriteDisplay.setStatus(_A)
_ModuleControlLedTest_Type=DisplayString
_ModuleControlLedTest_Object=MibTableColumn
moduleControlLedTest=_ModuleControlLedTest_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,10),_ModuleControlLedTest_Type())
moduleControlLedTest.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlLedTest.setStatus(_A)
_ModuleControlLoopOff_Type=DisplayString
_ModuleControlLoopOff_Object=MibTableColumn
moduleControlLoopOff=_ModuleControlLoopOff_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,11),_ModuleControlLoopOff_Type())
moduleControlLoopOff.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlLoopOff.setStatus(_A)
_ModuleControlLoopPort1_Type=DisplayString
_ModuleControlLoopPort1_Object=MibTableColumn
moduleControlLoopPort1=_ModuleControlLoopPort1_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,12),_ModuleControlLoopPort1_Type())
moduleControlLoopPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlLoopPort1.setStatus(_A)
_ModuleControlLoopPort2_Type=DisplayString
_ModuleControlLoopPort2_Object=MibTableColumn
moduleControlLoopPort2=_ModuleControlLoopPort2_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,13),_ModuleControlLoopPort2_Type())
moduleControlLoopPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlLoopPort2.setStatus(_A)
_ModuleControlLoopPort3_Type=DisplayString
_ModuleControlLoopPort3_Object=MibTableColumn
moduleControlLoopPort3=_ModuleControlLoopPort3_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,14),_ModuleControlLoopPort3_Type())
moduleControlLoopPort3.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlLoopPort3.setStatus(_A)
_ModuleControlLoopPort4_Type=DisplayString
_ModuleControlLoopPort4_Object=MibTableColumn
moduleControlLoopPort4=_ModuleControlLoopPort4_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,15),_ModuleControlLoopPort4_Type())
moduleControlLoopPort4.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlLoopPort4.setStatus(_A)
_ModuleControlBertRestart_Type=DisplayString
_ModuleControlBertRestart_Object=MibTableColumn
moduleControlBertRestart=_ModuleControlBertRestart_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,16),_ModuleControlBertRestart_Type())
moduleControlBertRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlBertRestart.setStatus(_A)
_ModuleControlBertInsertError_Type=DisplayString
_ModuleControlBertInsertError_Object=MibTableColumn
moduleControlBertInsertError=_ModuleControlBertInsertError_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,17),_ModuleControlBertInsertError_Type())
moduleControlBertInsertError.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlBertInsertError.setStatus(_A)
_ModuleControlBertClearCounter_Type=DisplayString
_ModuleControlBertClearCounter_Object=MibTableColumn
moduleControlBertClearCounter=_ModuleControlBertClearCounter_Object((1,3,6,1,4,1,3181,10,6,1,94,12,1,18),_ModuleControlBertClearCounter_Type())
moduleControlBertClearCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleControlBertClearCounter.setStatus(_A)
_SystemStatusTable_Object=MibTable
systemStatusTable=_SystemStatusTable_Object((1,3,6,1,4,1,3181,10,6,1,94,100))
if mibBuilder.loadTexts:systemStatusTable.setStatus(_A)
_SystemStatusEntry_Object=MibTableRow
systemStatusEntry=_SystemStatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,100,1))
systemStatusEntry.setIndexNames((0,_G,_BH))
if mibBuilder.loadTexts:systemStatusEntry.setStatus(_A)
class _SystemStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_SystemStatusIndex_Type.__name__=_B
_SystemStatusIndex_Object=MibTableColumn
systemStatusIndex=_SystemStatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,100,1,1),_SystemStatusIndex_Type())
systemStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:systemStatusIndex.setStatus(_A)
class _SystemStatusAnyErrorCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_SystemStatusAnyErrorCondition_Type.__name__=_B
_SystemStatusAnyErrorCondition_Object=MibTableColumn
systemStatusAnyErrorCondition=_SystemStatusAnyErrorCondition_Object((1,3,6,1,4,1,3181,10,6,1,94,100,1,2),_SystemStatusAnyErrorCondition_Type())
systemStatusAnyErrorCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:systemStatusAnyErrorCondition.setStatus(_A)
class _SystemStatusAnyTestMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_SystemStatusAnyTestMode_Type.__name__=_B
_SystemStatusAnyTestMode_Object=MibTableColumn
systemStatusAnyTestMode=_SystemStatusAnyTestMode_Object((1,3,6,1,4,1,3181,10,6,1,94,100,1,3),_SystemStatusAnyTestMode_Type())
systemStatusAnyTestMode.setMaxAccess(_D)
if mibBuilder.loadTexts:systemStatusAnyTestMode.setStatus(_A)
class _SystemStatusAnySparePart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_SystemStatusAnySparePart_Type.__name__=_B
_SystemStatusAnySparePart_Object=MibTableColumn
systemStatusAnySparePart=_SystemStatusAnySparePart_Object((1,3,6,1,4,1,3181,10,6,1,94,100,1,4),_SystemStatusAnySparePart_Type())
systemStatusAnySparePart.setMaxAccess(_D)
if mibBuilder.loadTexts:systemStatusAnySparePart.setStatus(_A)
_SystemStatusUsedNodeId_Type=Unsigned32
_SystemStatusUsedNodeId_Object=MibTableColumn
systemStatusUsedNodeId=_SystemStatusUsedNodeId_Object((1,3,6,1,4,1,3181,10,6,1,94,100,1,5),_SystemStatusUsedNodeId_Type())
systemStatusUsedNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:systemStatusUsedNodeId.setStatus(_A)
_SystemStatusLocalRack_Type=Unsigned32
_SystemStatusLocalRack_Object=MibTableColumn
systemStatusLocalRack=_SystemStatusLocalRack_Object((1,3,6,1,4,1,3181,10,6,1,94,100,1,6),_SystemStatusLocalRack_Type())
systemStatusLocalRack.setMaxAccess(_D)
if mibBuilder.loadTexts:systemStatusLocalRack.setStatus(_A)
_SystemStatusLocalSlot_Type=Unsigned32
_SystemStatusLocalSlot_Object=MibTableColumn
systemStatusLocalSlot=_SystemStatusLocalSlot_Object((1,3,6,1,4,1,3181,10,6,1,94,100,1,7),_SystemStatusLocalSlot_Type())
systemStatusLocalSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:systemStatusLocalSlot.setStatus(_A)
_ModuleInventoryTable_Object=MibTable
moduleInventoryTable=_ModuleInventoryTable_Object((1,3,6,1,4,1,3181,10,6,1,94,101))
if mibBuilder.loadTexts:moduleInventoryTable.setStatus(_A)
_ModuleInventoryEntry_Object=MibTableRow
moduleInventoryEntry=_ModuleInventoryEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1))
moduleInventoryEntry.setIndexNames((0,_G,_BI))
if mibBuilder.loadTexts:moduleInventoryEntry.setStatus(_A)
class _ModuleInventoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_ModuleInventoryIndex_Type.__name__=_B
_ModuleInventoryIndex_Object=MibTableColumn
moduleInventoryIndex=_ModuleInventoryIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,1),_ModuleInventoryIndex_Type())
moduleInventoryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:moduleInventoryIndex.setStatus(_A)
_ModuleInventoryExpectedModule_Type=DisplayString
_ModuleInventoryExpectedModule_Object=MibTableColumn
moduleInventoryExpectedModule=_ModuleInventoryExpectedModule_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,2),_ModuleInventoryExpectedModule_Type())
moduleInventoryExpectedModule.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryExpectedModule.setStatus(_A)
_ModuleInventoryModule_Type=DisplayString
_ModuleInventoryModule_Object=MibTableColumn
moduleInventoryModule=_ModuleInventoryModule_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,3),_ModuleInventoryModule_Type())
moduleInventoryModule.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryModule.setStatus(_A)
class _ModuleInventoryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('empty',0),('unknown',1),(_Az,2),('measurement',3),('amplifier',4),('management',5),(_Aq,6),('occupied',7)))
_ModuleInventoryType_Type.__name__=_B
_ModuleInventoryType_Object=MibTableColumn
moduleInventoryType=_ModuleInventoryType_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,4),_ModuleInventoryType_Type())
moduleInventoryType.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryType.setStatus(_A)
class _ModuleInventoryBoardCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ModuleInventoryBoardCode_Type.__name__=_B
_ModuleInventoryBoardCode_Object=MibTableColumn
moduleInventoryBoardCode=_ModuleInventoryBoardCode_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,5),_ModuleInventoryBoardCode_Type())
moduleInventoryBoardCode.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryBoardCode.setStatus(_A)
_ModuleInventoryAdditionalInfo_Type=DisplayString
_ModuleInventoryAdditionalInfo_Object=MibTableColumn
moduleInventoryAdditionalInfo=_ModuleInventoryAdditionalInfo_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,6),_ModuleInventoryAdditionalInfo_Type())
moduleInventoryAdditionalInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryAdditionalInfo.setStatus(_A)
_ModuleInventorySerialNumber_Type=DisplayString
_ModuleInventorySerialNumber_Object=MibTableColumn
moduleInventorySerialNumber=_ModuleInventorySerialNumber_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,7),_ModuleInventorySerialNumber_Type())
moduleInventorySerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventorySerialNumber.setStatus(_A)
_ModuleInventoryOccupiedSlots_Type=Unsigned32
_ModuleInventoryOccupiedSlots_Object=MibTableColumn
moduleInventoryOccupiedSlots=_ModuleInventoryOccupiedSlots_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,8),_ModuleInventoryOccupiedSlots_Type())
moduleInventoryOccupiedSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryOccupiedSlots.setStatus(_A)
_ModuleInventoryProjectNumber_Type=DisplayString
_ModuleInventoryProjectNumber_Object=MibTableColumn
moduleInventoryProjectNumber=_ModuleInventoryProjectNumber_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,9),_ModuleInventoryProjectNumber_Type())
moduleInventoryProjectNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryProjectNumber.setStatus(_A)
_ModuleInventoryBuildVersion_Type=DisplayString
_ModuleInventoryBuildVersion_Object=MibTableColumn
moduleInventoryBuildVersion=_ModuleInventoryBuildVersion_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,10),_ModuleInventoryBuildVersion_Type())
moduleInventoryBuildVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryBuildVersion.setStatus(_A)
_ModuleInventoryProductionDate_Type=DisplayString
_ModuleInventoryProductionDate_Object=MibTableColumn
moduleInventoryProductionDate=_ModuleInventoryProductionDate_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,11),_ModuleInventoryProductionDate_Type())
moduleInventoryProductionDate.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryProductionDate.setStatus(_A)
_ModuleInventoryMfgTestInfo_Type=DisplayString
_ModuleInventoryMfgTestInfo_Object=MibTableColumn
moduleInventoryMfgTestInfo=_ModuleInventoryMfgTestInfo_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,12),_ModuleInventoryMfgTestInfo_Type())
moduleInventoryMfgTestInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryMfgTestInfo.setStatus(_A)
class _ModuleInventoryNumberOfOpticalPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ModuleInventoryNumberOfOpticalPorts_Type.__name__=_B
_ModuleInventoryNumberOfOpticalPorts_Object=MibTableColumn
moduleInventoryNumberOfOpticalPorts=_ModuleInventoryNumberOfOpticalPorts_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,13),_ModuleInventoryNumberOfOpticalPorts_Type())
moduleInventoryNumberOfOpticalPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryNumberOfOpticalPorts.setStatus(_A)
class _ModuleInventoryNumberOfSfpPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ModuleInventoryNumberOfSfpPorts_Type.__name__=_B
_ModuleInventoryNumberOfSfpPorts_Object=MibTableColumn
moduleInventoryNumberOfSfpPorts=_ModuleInventoryNumberOfSfpPorts_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,14),_ModuleInventoryNumberOfSfpPorts_Type())
moduleInventoryNumberOfSfpPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryNumberOfSfpPorts.setStatus(_A)
class _ModuleInventoryNumberOfXfpPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ModuleInventoryNumberOfXfpPorts_Type.__name__=_B
_ModuleInventoryNumberOfXfpPorts_Object=MibTableColumn
moduleInventoryNumberOfXfpPorts=_ModuleInventoryNumberOfXfpPorts_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,15),_ModuleInventoryNumberOfXfpPorts_Type())
moduleInventoryNumberOfXfpPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryNumberOfXfpPorts.setStatus(_A)
_ModuleInventoryCoreFirmwareVersion_Type=DisplayString
_ModuleInventoryCoreFirmwareVersion_Object=MibTableColumn
moduleInventoryCoreFirmwareVersion=_ModuleInventoryCoreFirmwareVersion_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,16),_ModuleInventoryCoreFirmwareVersion_Type())
moduleInventoryCoreFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryCoreFirmwareVersion.setStatus(_A)
_ModuleInventoryCoreFirmwareDate_Type=DisplayString
_ModuleInventoryCoreFirmwareDate_Object=MibTableColumn
moduleInventoryCoreFirmwareDate=_ModuleInventoryCoreFirmwareDate_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,17),_ModuleInventoryCoreFirmwareDate_Type())
moduleInventoryCoreFirmwareDate.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryCoreFirmwareDate.setStatus(_A)
_ModuleInventoryApplFirmwareVersion_Type=DisplayString
_ModuleInventoryApplFirmwareVersion_Object=MibTableColumn
moduleInventoryApplFirmwareVersion=_ModuleInventoryApplFirmwareVersion_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,18),_ModuleInventoryApplFirmwareVersion_Type())
moduleInventoryApplFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryApplFirmwareVersion.setStatus(_A)
_ModuleInventoryApplFirmwareDate_Type=DisplayString
_ModuleInventoryApplFirmwareDate_Object=MibTableColumn
moduleInventoryApplFirmwareDate=_ModuleInventoryApplFirmwareDate_Object((1,3,6,1,4,1,3181,10,6,1,94,101,1,19),_ModuleInventoryApplFirmwareDate_Type())
moduleInventoryApplFirmwareDate.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInventoryApplFirmwareDate.setStatus(_A)
_ModuleStatusTable_Object=MibTable
moduleStatusTable=_ModuleStatusTable_Object((1,3,6,1,4,1,3181,10,6,1,94,102))
if mibBuilder.loadTexts:moduleStatusTable.setStatus(_A)
_ModuleStatusEntry_Object=MibTableRow
moduleStatusEntry=_ModuleStatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1))
moduleStatusEntry.setIndexNames((0,_G,_BJ))
if mibBuilder.loadTexts:moduleStatusEntry.setStatus(_A)
class _ModuleStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_ModuleStatusIndex_Type.__name__=_B
_ModuleStatusIndex_Object=MibTableColumn
moduleStatusIndex=_ModuleStatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,1),_ModuleStatusIndex_Type())
moduleStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:moduleStatusIndex.setStatus(_A)
_ModuleStatusModule_Type=DisplayString
_ModuleStatusModule_Object=MibTableColumn
moduleStatusModule=_ModuleStatusModule_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,2),_ModuleStatusModule_Type())
moduleStatusModule.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusModule.setStatus(_A)
class _ModuleStatusSystemOk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_ModuleStatusSystemOk_Type.__name__=_B
_ModuleStatusSystemOk_Object=MibTableColumn
moduleStatusSystemOk=_ModuleStatusSystemOk_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,3),_ModuleStatusSystemOk_Type())
moduleStatusSystemOk.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusSystemOk.setStatus(_A)
class _ModuleStatusErrorCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_ModuleStatusErrorCondition_Type.__name__=_B
_ModuleStatusErrorCondition_Object=MibTableColumn
moduleStatusErrorCondition=_ModuleStatusErrorCondition_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,4),_ModuleStatusErrorCondition_Type())
moduleStatusErrorCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusErrorCondition.setStatus(_A)
class _ModuleStatusTestMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_ModuleStatusTestMode_Type.__name__=_B
_ModuleStatusTestMode_Object=MibTableColumn
moduleStatusTestMode=_ModuleStatusTestMode_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,5),_ModuleStatusTestMode_Type())
moduleStatusTestMode.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusTestMode.setStatus(_A)
class _ModuleStatusSparePart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_ModuleStatusSparePart_Type.__name__=_B
_ModuleStatusSparePart_Object=MibTableColumn
moduleStatusSparePart=_ModuleStatusSparePart_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,6),_ModuleStatusSparePart_Type())
moduleStatusSparePart.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusSparePart.setStatus(_A)
_ModuleStatusUptime_Type=Counter32
_ModuleStatusUptime_Object=MibTableColumn
moduleStatusUptime=_ModuleStatusUptime_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,7),_ModuleStatusUptime_Type())
moduleStatusUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusUptime.setStatus(_A)
_ModuleStatusTimeSinceCounterReset_Type=Counter32
_ModuleStatusTimeSinceCounterReset_Object=MibTableColumn
moduleStatusTimeSinceCounterReset=_ModuleStatusTimeSinceCounterReset_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,8),_ModuleStatusTimeSinceCounterReset_Type())
moduleStatusTimeSinceCounterReset.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusTimeSinceCounterReset.setStatus(_A)
class _ModuleStatusTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ModuleStatusTemperature_Type.__name__=_B
_ModuleStatusTemperature_Object=MibTableColumn
moduleStatusTemperature=_ModuleStatusTemperature_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,9),_ModuleStatusTemperature_Type())
moduleStatusTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusTemperature.setStatus(_A)
class _ModuleStatusTooHot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_ModuleStatusTooHot_Type.__name__=_B
_ModuleStatusTooHot_Object=MibTableColumn
moduleStatusTooHot=_ModuleStatusTooHot_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,10),_ModuleStatusTooHot_Type())
moduleStatusTooHot.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusTooHot.setStatus(_A)
class _ModuleStatusBackupState_Type(Bits):namedValues=NamedValues(*(('disrupted',0),('backup',1),('awaitSwitchback',2),('manual',3)))
_ModuleStatusBackupState_Type.__name__=_Ak
_ModuleStatusBackupState_Object=MibTableColumn
moduleStatusBackupState=_ModuleStatusBackupState_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,11),_ModuleStatusBackupState_Type())
moduleStatusBackupState.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusBackupState.setStatus(_A)
_ModuleStatusBackupCounter_Type=Unsigned32
_ModuleStatusBackupCounter_Object=MibTableColumn
moduleStatusBackupCounter=_ModuleStatusBackupCounter_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,12),_ModuleStatusBackupCounter_Type())
moduleStatusBackupCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusBackupCounter.setStatus(_A)
_ModuleStatusBackupDuration_Type=Counter32
_ModuleStatusBackupDuration_Object=MibTableColumn
moduleStatusBackupDuration=_ModuleStatusBackupDuration_Object((1,3,6,1,4,1,3181,10,6,1,94,102,1,13),_ModuleStatusBackupDuration_Type())
moduleStatusBackupDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleStatusBackupDuration.setStatus(_A)
_PortStatusTable_Object=MibTable
portStatusTable=_PortStatusTable_Object((1,3,6,1,4,1,3181,10,6,1,94,103))
if mibBuilder.loadTexts:portStatusTable.setStatus(_A)
_PortStatusEntry_Object=MibTableRow
portStatusEntry=_PortStatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1))
portStatusEntry.setIndexNames((0,_G,_BK))
if mibBuilder.loadTexts:portStatusEntry.setStatus(_A)
class _PortStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,47))
_PortStatusPortIndex_Type.__name__=_B
_PortStatusPortIndex_Object=MibTableColumn
portStatusPortIndex=_PortStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,1),_PortStatusPortIndex_Type())
portStatusPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:portStatusPortIndex.setStatus(_A)
_PortStatusModule_Type=DisplayString
_PortStatusModule_Object=MibTableColumn
portStatusModule=_PortStatusModule_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,2),_PortStatusModule_Type())
portStatusModule.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusModule.setStatus(_A)
_PortStatusLocation_Type=DisplayString
_PortStatusLocation_Object=MibTableColumn
portStatusLocation=_PortStatusLocation_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,3),_PortStatusLocation_Type())
portStatusLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusLocation.setStatus(_A)
_PortStatusSnmpPort_Type=Unsigned32
_PortStatusSnmpPort_Object=MibTableColumn
portStatusSnmpPort=_PortStatusSnmpPort_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,4),_PortStatusSnmpPort_Type())
portStatusSnmpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusSnmpPort.setStatus(_A)
_PortStatusAlias_Type=DisplayString
_PortStatusAlias_Object=MibTableColumn
portStatusAlias=_PortStatusAlias_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,5),_PortStatusAlias_Type())
portStatusAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusAlias.setStatus(_A)
class _PortStatusAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Ap,0),('up',1),('down',2),('testing',3)))
_PortStatusAdminStatus_Type.__name__=_B
_PortStatusAdminStatus_Object=MibTableColumn
portStatusAdminStatus=_PortStatusAdminStatus_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,6),_PortStatusAdminStatus_Type())
portStatusAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusAdminStatus.setStatus(_A)
class _PortStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Ap,0),('up',1),('down',2),('testing',3)))
_PortStatusOperStatus_Type.__name__=_B
_PortStatusOperStatus_Object=MibTableColumn
portStatusOperStatus=_PortStatusOperStatus_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,7),_PortStatusOperStatus_Type())
portStatusOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusOperStatus.setStatus(_A)
class _PortStatusDetailedStatus_Type(Bits):namedValues=NamedValues(*((_E,0),('sfpMissing',1),('pllNotLocked',2),(_BE,3),('tooHigh',4),('laserOff',5),('loop',6),('reserved',7),('unknown',8),(_Ap,9)))
_PortStatusDetailedStatus_Type.__name__=_Ak
_PortStatusDetailedStatus_Object=MibTableColumn
portStatusDetailedStatus=_PortStatusDetailedStatus_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,8),_PortStatusDetailedStatus_Type())
portStatusDetailedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusDetailedStatus.setStatus(_A)
class _PortStatusPortDatarate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,10,11,12,13,14,15,20,21,22,23,30,31,32,33,34,35,40,41,42,43,44,45)));namedValues=NamedValues(*((_Ap,0),('txp',1),(_AK,2),(_K,3),(_Aj,4),(_J,10),(_AO,11),(_B0,12),(_Am,13),('ms10xFc',14),('ms16xFc',15),(_AL,20),(_AN,21),(_AP,22),('oc192',23),(_Ai,30),('otu1e',31),('otu1f',32),('otu2',33),('otu2e',34),('otu2f',35),(_Af,40),(_AM,41),(_Ag,42),(_Ah,43),('tdm2',44),('other',45)))
_PortStatusPortDatarate_Type.__name__=_B
_PortStatusPortDatarate_Object=MibTableColumn
portStatusPortDatarate=_PortStatusPortDatarate_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,9),_PortStatusPortDatarate_Type())
portStatusPortDatarate.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusPortDatarate.setStatus(_A)
_PortStatusUpdateTimeStamp_Type=DisplayString
_PortStatusUpdateTimeStamp_Object=MibTableColumn
portStatusUpdateTimeStamp=_PortStatusUpdateTimeStamp_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,10),_PortStatusUpdateTimeStamp_Type())
portStatusUpdateTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusUpdateTimeStamp.setStatus(_A)
_PortStatusTimeSinceValueReset_Type=Counter32
_PortStatusTimeSinceValueReset_Object=MibTableColumn
portStatusTimeSinceValueReset=_PortStatusTimeSinceValueReset_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,11),_PortStatusTimeSinceValueReset_Type())
portStatusTimeSinceValueReset.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusTimeSinceValueReset.setStatus(_A)
_PortStatusTimeSinceLastError_Type=Counter32
_PortStatusTimeSinceLastError_Object=MibTableColumn
portStatusTimeSinceLastError=_PortStatusTimeSinceLastError_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,12),_PortStatusTimeSinceLastError_Type())
portStatusTimeSinceLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusTimeSinceLastError.setStatus(_A)
_PortStatusTimeSignalTooLow_Type=Counter32
_PortStatusTimeSignalTooLow_Object=MibTableColumn
portStatusTimeSignalTooLow=_PortStatusTimeSignalTooLow_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,13),_PortStatusTimeSignalTooLow_Type())
portStatusTimeSignalTooLow.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusTimeSignalTooLow.setStatus(_A)
_PortStatusSignalTooLowCounter_Type=Unsigned32
_PortStatusSignalTooLowCounter_Object=MibTableColumn
portStatusSignalTooLowCounter=_PortStatusSignalTooLowCounter_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,14),_PortStatusSignalTooLowCounter_Type())
portStatusSignalTooLowCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusSignalTooLowCounter.setStatus(_A)
_PortStatusTimeSignalTooHigh_Type=Counter32
_PortStatusTimeSignalTooHigh_Object=MibTableColumn
portStatusTimeSignalTooHigh=_PortStatusTimeSignalTooHigh_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,15),_PortStatusTimeSignalTooHigh_Type())
portStatusTimeSignalTooHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusTimeSignalTooHigh.setStatus(_A)
_PortStatusSignalTooHighCounter_Type=Unsigned32
_PortStatusSignalTooHighCounter_Object=MibTableColumn
portStatusSignalTooHighCounter=_PortStatusSignalTooHighCounter_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,16),_PortStatusSignalTooHighCounter_Type())
portStatusSignalTooHighCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusSignalTooHighCounter.setStatus(_A)
_PortStatusLowThreshold_Type=DisplayString
_PortStatusLowThreshold_Object=MibTableColumn
portStatusLowThreshold=_PortStatusLowThreshold_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,17),_PortStatusLowThreshold_Type())
portStatusLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusLowThreshold.setStatus(_A)
_PortStatusCurrentInputSignal_Type=DisplayString
_PortStatusCurrentInputSignal_Object=MibTableColumn
portStatusCurrentInputSignal=_PortStatusCurrentInputSignal_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,18),_PortStatusCurrentInputSignal_Type())
portStatusCurrentInputSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusCurrentInputSignal.setStatus(_A)
_PortStatusHighThreshold_Type=DisplayString
_PortStatusHighThreshold_Object=MibTableColumn
portStatusHighThreshold=_PortStatusHighThreshold_Object((1,3,6,1,4,1,3181,10,6,1,94,103,1,19),_PortStatusHighThreshold_Type())
portStatusHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusHighThreshold.setStatus(_A)
_EmStatusTable_Object=MibTable
emStatusTable=_EmStatusTable_Object((1,3,6,1,4,1,3181,10,6,1,94,104))
if mibBuilder.loadTexts:emStatusTable.setStatus(_A)
_EmStatusEntry_Object=MibTableRow
emStatusEntry=_EmStatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1))
emStatusEntry.setIndexNames((0,_G,_BL))
if mibBuilder.loadTexts:emStatusEntry.setStatus(_A)
class _EmStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_EmStatusIndex_Type.__name__=_B
_EmStatusIndex_Object=MibTableColumn
emStatusIndex=_EmStatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,1),_EmStatusIndex_Type())
emStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:emStatusIndex.setStatus(_A)
class _EmStatusSystemOk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_EmStatusSystemOk_Type.__name__=_B
_EmStatusSystemOk_Object=MibTableColumn
emStatusSystemOk=_EmStatusSystemOk_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,2),_EmStatusSystemOk_Type())
emStatusSystemOk.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusSystemOk.setStatus(_A)
class _EmStatusErrors_Type(Bits):namedValues=NamedValues(*(('lossOfInput',0),('lossOfOutput',1),('tooHot',2),('eyeSafetyShutdown',3),('backReflection',4),('powerLimit',5),('overCurrent',6),('pumpDown',7)))
_EmStatusErrors_Type.__name__=_Ak
_EmStatusErrors_Object=MibTableColumn
emStatusErrors=_EmStatusErrors_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,3),_EmStatusErrors_Type())
emStatusErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusErrors.setStatus(_A)
_EmStatusHardwareCode_Type=DisplayString
_EmStatusHardwareCode_Object=MibTableColumn
emStatusHardwareCode=_EmStatusHardwareCode_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,4),_EmStatusHardwareCode_Type())
emStatusHardwareCode.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusHardwareCode.setStatus(_A)
_EmStatusTimeSincePowerError_Type=Counter32
_EmStatusTimeSincePowerError_Object=MibTableColumn
emStatusTimeSincePowerError=_EmStatusTimeSincePowerError_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,5),_EmStatusTimeSincePowerError_Type())
emStatusTimeSincePowerError.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusTimeSincePowerError.setStatus(_A)
_EmStatusTimeWithPowerLoss_Type=Counter32
_EmStatusTimeWithPowerLoss_Object=MibTableColumn
emStatusTimeWithPowerLoss=_EmStatusTimeWithPowerLoss_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,6),_EmStatusTimeWithPowerLoss_Type())
emStatusTimeWithPowerLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusTimeWithPowerLoss.setStatus(_A)
_EmStatusInputSignalLowCounter_Type=Unsigned32
_EmStatusInputSignalLowCounter_Object=MibTableColumn
emStatusInputSignalLowCounter=_EmStatusInputSignalLowCounter_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,7),_EmStatusInputSignalLowCounter_Type())
emStatusInputSignalLowCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusInputSignalLowCounter.setStatus(_A)
_EmStatusInputPower_Type=DisplayString
_EmStatusInputPower_Object=MibTableColumn
emStatusInputPower=_EmStatusInputPower_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,8),_EmStatusInputPower_Type())
emStatusInputPower.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusInputPower.setStatus(_A)
_EmStatusSignalGain_Type=DisplayString
_EmStatusSignalGain_Object=MibTableColumn
emStatusSignalGain=_EmStatusSignalGain_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,9),_EmStatusSignalGain_Type())
emStatusSignalGain.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusSignalGain.setStatus(_A)
_EmStatusOptimalFlatGain_Type=DisplayString
_EmStatusOptimalFlatGain_Object=MibTableColumn
emStatusOptimalFlatGain=_EmStatusOptimalFlatGain_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,10),_EmStatusOptimalFlatGain_Type())
emStatusOptimalFlatGain.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusOptimalFlatGain.setStatus(_A)
_EmStatusBackReflection_Type=DisplayString
_EmStatusBackReflection_Object=MibTableColumn
emStatusBackReflection=_EmStatusBackReflection_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,11),_EmStatusBackReflection_Type())
emStatusBackReflection.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusBackReflection.setStatus(_A)
_EmStatusSignalOutputPower_Type=DisplayString
_EmStatusSignalOutputPower_Object=MibTableColumn
emStatusSignalOutputPower=_EmStatusSignalOutputPower_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,12),_EmStatusSignalOutputPower_Type())
emStatusSignalOutputPower.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusSignalOutputPower.setStatus(_A)
_EmStatusTotalOutputPower_Type=DisplayString
_EmStatusTotalOutputPower_Object=MibTableColumn
emStatusTotalOutputPower=_EmStatusTotalOutputPower_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,13),_EmStatusTotalOutputPower_Type())
emStatusTotalOutputPower.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusTotalOutputPower.setStatus(_A)
_EmStatusMinOutputPower_Type=DisplayString
_EmStatusMinOutputPower_Object=MibTableColumn
emStatusMinOutputPower=_EmStatusMinOutputPower_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,14),_EmStatusMinOutputPower_Type())
emStatusMinOutputPower.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusMinOutputPower.setStatus(_A)
_EmStatusMaxOutputPower_Type=DisplayString
_EmStatusMaxOutputPower_Object=MibTableColumn
emStatusMaxOutputPower=_EmStatusMaxOutputPower_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,15),_EmStatusMaxOutputPower_Type())
emStatusMaxOutputPower.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusMaxOutputPower.setStatus(_A)
_EmStatusCfgOutputPower_Type=DisplayString
_EmStatusCfgOutputPower_Object=MibTableColumn
emStatusCfgOutputPower=_EmStatusCfgOutputPower_Object((1,3,6,1,4,1,3181,10,6,1,94,104,1,16),_EmStatusCfgOutputPower_Type())
emStatusCfgOutputPower.setMaxAccess(_D)
if mibBuilder.loadTexts:emStatusCfgOutputPower.setStatus(_A)
_BertStatusTable_Object=MibTable
bertStatusTable=_BertStatusTable_Object((1,3,6,1,4,1,3181,10,6,1,94,105))
if mibBuilder.loadTexts:bertStatusTable.setStatus(_A)
_BertStatusEntry_Object=MibTableRow
bertStatusEntry=_BertStatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1))
bertStatusEntry.setIndexNames((0,_G,_BM))
if mibBuilder.loadTexts:bertStatusEntry.setStatus(_A)
class _BertStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_BertStatusIndex_Type.__name__=_B
_BertStatusIndex_Object=MibTableColumn
bertStatusIndex=_BertStatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,1),_BertStatusIndex_Type())
bertStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:bertStatusIndex.setStatus(_A)
_BertStatusLocation_Type=DisplayString
_BertStatusLocation_Object=MibTableColumn
bertStatusLocation=_BertStatusLocation_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,2),_BertStatusLocation_Type())
bertStatusLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusLocation.setStatus(_A)
class _BertStatusBertOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unused',0),('inSync',1),('wasOutOfSync',2),('outOfSync',3)))
_BertStatusBertOperation_Type.__name__=_B
_BertStatusBertOperation_Object=MibTableColumn
bertStatusBertOperation=_BertStatusBertOperation_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,3),_BertStatusBertOperation_Type())
bertStatusBertOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusBertOperation.setStatus(_A)
_BertStatusTotalErrors_Type=Unsigned32
_BertStatusTotalErrors_Object=MibTableColumn
bertStatusTotalErrors=_BertStatusTotalErrors_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,4),_BertStatusTotalErrors_Type())
bertStatusTotalErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusTotalErrors.setStatus(_A)
_BertStatusTimeSinceLastError_Type=Counter32
_BertStatusTimeSinceLastError_Object=MibTableColumn
bertStatusTimeSinceLastError=_BertStatusTimeSinceLastError_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,5),_BertStatusTimeSinceLastError_Type())
bertStatusTimeSinceLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusTimeSinceLastError.setStatus(_A)
_BertStatusTotalTestTime_Type=Counter32
_BertStatusTotalTestTime_Object=MibTableColumn
bertStatusTotalTestTime=_BertStatusTotalTestTime_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,6),_BertStatusTotalTestTime_Type())
bertStatusTotalTestTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusTotalTestTime.setStatus(_A)
_BertStatusErroredTime_Type=Counter32
_BertStatusErroredTime_Object=MibTableColumn
bertStatusErroredTime=_BertStatusErroredTime_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,7),_BertStatusErroredTime_Type())
bertStatusErroredTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusErroredTime.setStatus(_A)
_BertStatusBitErrorRate_Type=DisplayString
_BertStatusBitErrorRate_Object=MibTableColumn
bertStatusBitErrorRate=_BertStatusBitErrorRate_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,8),_BertStatusBitErrorRate_Type())
bertStatusBitErrorRate.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusBitErrorRate.setStatus(_A)
_BertStatusBerSinceLastError_Type=DisplayString
_BertStatusBerSinceLastError_Object=MibTableColumn
bertStatusBerSinceLastError=_BertStatusBerSinceLastError_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,9),_BertStatusBerSinceLastError_Type())
bertStatusBerSinceLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusBerSinceLastError.setStatus(_A)
_BertStatusTheoreticalBer_Type=DisplayString
_BertStatusTheoreticalBer_Object=MibTableColumn
bertStatusTheoreticalBer=_BertStatusTheoreticalBer_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,10),_BertStatusTheoreticalBer_Type())
bertStatusTheoreticalBer.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusTheoreticalBer.setStatus(_A)
_BertStatusAvailability_Type=DisplayString
_BertStatusAvailability_Object=MibTableColumn
bertStatusAvailability=_BertStatusAvailability_Object((1,3,6,1,4,1,3181,10,6,1,94,105,1,11),_BertStatusAvailability_Type())
bertStatusAvailability.setMaxAccess(_D)
if mibBuilder.loadTexts:bertStatusAvailability.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'device':device,'msp1000':msp1000,'systemConfigTable':systemConfigTable,'systemConfigEntry':systemConfigEntry,_B1:systemConfigIndex,'systemConfigNmsOperationMode':systemConfigNmsOperationMode,'systemConfigCoreMode':systemConfigCoreMode,'systemConfigNodeId':systemConfigNodeId,'systemConfigDisableLegacyAccess':systemConfigDisableLegacyAccess,'slotConfigTable':slotConfigTable,'slotConfigEntry':slotConfigEntry,_B2:slotConfigIndex,'slotConfigModule':slotConfigModule,'slotConfigSparepartMode':slotConfigSparepartMode,'slotConfigPort1Alias':slotConfigPort1Alias,'slotConfigPort2Alias':slotConfigPort2Alias,'slotConfigPort3Alias':slotConfigPort3Alias,'slotConfigPort4Alias':slotConfigPort4Alias,'x2gConfigTable':x2gConfigTable,'x2gConfigEntry':x2gConfigEntry,_B3:x2gConfigIndex,'x2gConfigPort1Datarate':x2gConfigPort1Datarate,'x2gConfigPort2Datarate':x2gConfigPort2Datarate,'x2gConfigPort3Datarate':x2gConfigPort3Datarate,'x2gConfigPort4Datarate':x2gConfigPort4Datarate,'x2gConfigCrossConnect':x2gConfigCrossConnect,'x2gConfigDeactivatePort1':x2gConfigDeactivatePort1,'x2gConfigDeactivatePort2':x2gConfigDeactivatePort2,'x2gConfigDeactivatePort3':x2gConfigDeactivatePort3,'x2gConfigDeactivatePort4':x2gConfigDeactivatePort4,'x2gConfigFrontPanelMode':x2gConfigFrontPanelMode,'x2gConfigLossOfSignalHandling':x2gConfigLossOfSignalHandling,'x2gConfigOptimizedFor8b10b':x2gConfigOptimizedFor8b10b,'x2gConfigBertPattern':x2gConfigBertPattern,'x2gConfigSfpDeltaInterval':x2gConfigSfpDeltaInterval,'x2gConfigSfpDeltaThreshold':x2gConfigSfpDeltaThreshold,'x2gConfigBackupTrigger':x2gConfigBackupTrigger,'x2gConfigStayWithLastLink':x2gConfigStayWithLastLink,'x2gConfigBackupEnd':x2gConfigBackupEnd,'x2gConfigPermitLinkOverride':x2gConfigPermitLinkOverride,'txgConfigTable':txgConfigTable,'txgConfigEntry':txgConfigEntry,_B6:txgConfigIndex,'txgConfigTxgDatarate':txgConfigTxgDatarate,'txgConfigTxgOperationMode':txgConfigTxgOperationMode,'txgConfigPort1ItuChannel':txgConfigPort1ItuChannel,'txgConfigPort2ItuChannel':txgConfigPort2ItuChannel,'txgConfigDeactivatePort1':txgConfigDeactivatePort1,'txgConfigDeactivatePort2':txgConfigDeactivatePort2,'txgConfigFrontPanelMode':txgConfigFrontPanelMode,'txgConfigLossOfSignalHandling':txgConfigLossOfSignalHandling,'txgConfigBertPattern':txgConfigBertPattern,'txgConfigSfpDeltaInterval':txgConfigSfpDeltaInterval,'txgConfigSfpDeltaThreshold':txgConfigSfpDeltaThreshold,'cxgPlusConfigTable':cxgPlusConfigTable,'cxgPlusConfigEntry':cxgPlusConfigEntry,_B7:cxgPlusConfigIndex,'cxgPlusConfigCxgPort12Datarate':cxgPlusConfigCxgPort12Datarate,'cxgPlusConfigCxgPort34Datarate':cxgPlusConfigCxgPort34Datarate,'cxgPlusConfigPort1ItuChannel':cxgPlusConfigPort1ItuChannel,'cxgPlusConfigPort2ItuChannel':cxgPlusConfigPort2ItuChannel,'cxgPlusConfigPort3ItuChannel':cxgPlusConfigPort3ItuChannel,'cxgPlusConfigPort4ItuChannel':cxgPlusConfigPort4ItuChannel,'cxgPlusConfigDeactivatePort1':cxgPlusConfigDeactivatePort1,'cxgPlusConfigDeactivatePort2':cxgPlusConfigDeactivatePort2,'cxgPlusConfigDeactivatePort3':cxgPlusConfigDeactivatePort3,'cxgPlusConfigDeactivatePort4':cxgPlusConfigDeactivatePort4,'cxgPlusConfigFrontPanelMode':cxgPlusConfigFrontPanelMode,'cxgPlusConfigLossOfSignalHandling':cxgPlusConfigLossOfSignalHandling,'cxgPlusConfigSfpDeltaInterval':cxgPlusConfigSfpDeltaInterval,'cxgPlusConfigSfpDeltaThreshold':cxgPlusConfigSfpDeltaThreshold,'cxgConfigTable':cxgConfigTable,'cxgConfigEntry':cxgConfigEntry,_B8:cxgConfigIndex,'cxgConfigCxgPort12Datarate':cxgConfigCxgPort12Datarate,'cxgConfigPort1ItuChannel':cxgConfigPort1ItuChannel,'cxgConfigPort2ItuChannel':cxgConfigPort2ItuChannel,'cxgConfigDeactivatePort1':cxgConfigDeactivatePort1,'cxgConfigDeactivatePort2':cxgConfigDeactivatePort2,'cxgConfigFrontPanelMode':cxgConfigFrontPanelMode,'cxgConfigLossOfSignalHandling':cxgConfigLossOfSignalHandling,'cxgConfigSfpDeltaInterval':cxgConfigSfpDeltaInterval,'cxgConfigSfpDeltaThreshold':cxgConfigSfpDeltaThreshold,'t4gConfigTable':t4gConfigTable,'t4gConfigEntry':t4gConfigEntry,_B9:t4gConfigIndex,'t4gConfigT4gPort12Datarate':t4gConfigT4gPort12Datarate,'t4gConfigT4gPort34Datarate':t4gConfigT4gPort34Datarate,'t4gConfigT4gOperationMode':t4gConfigT4gOperationMode,'t4gConfigDeactivatePort1':t4gConfigDeactivatePort1,'t4gConfigDeactivatePort2':t4gConfigDeactivatePort2,'t4gConfigDeactivatePort3':t4gConfigDeactivatePort3,'t4gConfigDeactivatePort4':t4gConfigDeactivatePort4,'t4gConfigFrontPanelMode':t4gConfigFrontPanelMode,'t4gConfigLossOfSignalHandling':t4gConfigLossOfSignalHandling,'t4gConfigBertPattern':t4gConfigBertPattern,'t4gConfigSfpDeltaInterval':t4gConfigSfpDeltaInterval,'t4gConfigSfpDeltaThreshold':t4gConfigSfpDeltaThreshold,'m2gConfigTable':m2gConfigTable,'m2gConfigEntry':m2gConfigEntry,_BB:m2gConfigIndex,'m2gConfigChannel1Datarate':m2gConfigChannel1Datarate,'m2gConfigChannel2Datarate':m2gConfigChannel2Datarate,'m2gConfigPort1CopperSfp':m2gConfigPort1CopperSfp,'m2gConfigPort2CopperSfp':m2gConfigPort2CopperSfp,'m2gConfigSfpDeltaInterval':m2gConfigSfpDeltaInterval,'m2gConfigSfpDeltaThreshold':m2gConfigSfpDeltaThreshold,'m2gConfigLinkBackupTrigger':m2gConfigLinkBackupTrigger,'m2gConfigStayWithLastLink':m2gConfigStayWithLastLink,'m2gConfigBackupEnd':m2gConfigBackupEnd,'m2gConfigPermitLinkOverride':m2gConfigPermitLinkOverride,'om1ConfigTable':om1ConfigTable,'om1ConfigEntry':om1ConfigEntry,_BC:om1ConfigIndex,'om1ConfigWavelengthPortA':om1ConfigWavelengthPortA,'om1ConfigLowThresholdPortA':om1ConfigLowThresholdPortA,'om1ConfigHighThresholdPortA':om1ConfigHighThresholdPortA,'om1ConfigWavelengthPortB':om1ConfigWavelengthPortB,'om1ConfigLowThresholdPortB':om1ConfigLowThresholdPortB,'om1ConfigHighThresholdPortB':om1ConfigHighThresholdPortB,'om1ConfigFrontPanelMode':om1ConfigFrontPanelMode,'lp1ConfigTable':lp1ConfigTable,'lp1ConfigEntry':lp1ConfigEntry,_BD:lp1ConfigIndex,'lp1ConfigWavelengthPortA':lp1ConfigWavelengthPortA,'lp1ConfigLowThresholdPortA':lp1ConfigLowThresholdPortA,'lp1ConfigHighThresholdPortA':lp1ConfigHighThresholdPortA,'lp1ConfigWavelengthPortB':lp1ConfigWavelengthPortB,'lp1ConfigLowThresholdPortB':lp1ConfigLowThresholdPortB,'lp1ConfigHighThresholdPortB':lp1ConfigHighThresholdPortB,'lp1ConfigBackupCriteria':lp1ConfigBackupCriteria,'lp1ConfigStayWithLastLink':lp1ConfigStayWithLastLink,'lp1ConfigBackupEnd':lp1ConfigBackupEnd,'lp1ConfigFrontPanelMode':lp1ConfigFrontPanelMode,'emConfigTable':emConfigTable,'emConfigEntry':emConfigEntry,_BF:emConfigIndex,'emConfigEdfaOperationMode':emConfigEdfaOperationMode,'emConfigLossOfSignalHandling':emConfigLossOfSignalHandling,'emConfigSignalGain':emConfigSignalGain,'emConfigMaxOutputPower':emConfigMaxOutputPower,'emConfigLowThresholdEdfaIn':emConfigLowThresholdEdfaIn,'emConfigHighThresholdEdfaIn':emConfigHighThresholdEdfaIn,'emConfigLowThresholdPortB':emConfigLowThresholdPortB,'emConfigHighThresholdPortB':emConfigHighThresholdPortB,'emConfigFrontPanelMode':emConfigFrontPanelMode,'moduleControlTable':moduleControlTable,'moduleControlEntry':moduleControlEntry,_BG:moduleControlIndex,'moduleControlEnterPassword':moduleControlEnterPassword,'moduleControlRebootModule':moduleControlRebootModule,'moduleControlWarmStart':moduleControlWarmStart,'moduleControlClearCounter':moduleControlClearCounter,'moduleControlSwitchOffBackup':moduleControlSwitchOffBackup,'moduleControlSwitchToBackup':moduleControlSwitchToBackup,'moduleControlAutomaticBackup':moduleControlAutomaticBackup,'moduleControlWriteDisplay':moduleControlWriteDisplay,'moduleControlLedTest':moduleControlLedTest,'moduleControlLoopOff':moduleControlLoopOff,'moduleControlLoopPort1':moduleControlLoopPort1,'moduleControlLoopPort2':moduleControlLoopPort2,'moduleControlLoopPort3':moduleControlLoopPort3,'moduleControlLoopPort4':moduleControlLoopPort4,'moduleControlBertRestart':moduleControlBertRestart,'moduleControlBertInsertError':moduleControlBertInsertError,'moduleControlBertClearCounter':moduleControlBertClearCounter,'systemStatusTable':systemStatusTable,'systemStatusEntry':systemStatusEntry,_BH:systemStatusIndex,'systemStatusAnyErrorCondition':systemStatusAnyErrorCondition,'systemStatusAnyTestMode':systemStatusAnyTestMode,'systemStatusAnySparePart':systemStatusAnySparePart,'systemStatusUsedNodeId':systemStatusUsedNodeId,'systemStatusLocalRack':systemStatusLocalRack,'systemStatusLocalSlot':systemStatusLocalSlot,'moduleInventoryTable':moduleInventoryTable,'moduleInventoryEntry':moduleInventoryEntry,_BI:moduleInventoryIndex,'moduleInventoryExpectedModule':moduleInventoryExpectedModule,'moduleInventoryModule':moduleInventoryModule,'moduleInventoryType':moduleInventoryType,'moduleInventoryBoardCode':moduleInventoryBoardCode,'moduleInventoryAdditionalInfo':moduleInventoryAdditionalInfo,'moduleInventorySerialNumber':moduleInventorySerialNumber,'moduleInventoryOccupiedSlots':moduleInventoryOccupiedSlots,'moduleInventoryProjectNumber':moduleInventoryProjectNumber,'moduleInventoryBuildVersion':moduleInventoryBuildVersion,'moduleInventoryProductionDate':moduleInventoryProductionDate,'moduleInventoryMfgTestInfo':moduleInventoryMfgTestInfo,'moduleInventoryNumberOfOpticalPorts':moduleInventoryNumberOfOpticalPorts,'moduleInventoryNumberOfSfpPorts':moduleInventoryNumberOfSfpPorts,'moduleInventoryNumberOfXfpPorts':moduleInventoryNumberOfXfpPorts,'moduleInventoryCoreFirmwareVersion':moduleInventoryCoreFirmwareVersion,'moduleInventoryCoreFirmwareDate':moduleInventoryCoreFirmwareDate,'moduleInventoryApplFirmwareVersion':moduleInventoryApplFirmwareVersion,'moduleInventoryApplFirmwareDate':moduleInventoryApplFirmwareDate,'moduleStatusTable':moduleStatusTable,'moduleStatusEntry':moduleStatusEntry,_BJ:moduleStatusIndex,'moduleStatusModule':moduleStatusModule,'moduleStatusSystemOk':moduleStatusSystemOk,'moduleStatusErrorCondition':moduleStatusErrorCondition,'moduleStatusTestMode':moduleStatusTestMode,'moduleStatusSparePart':moduleStatusSparePart,'moduleStatusUptime':moduleStatusUptime,'moduleStatusTimeSinceCounterReset':moduleStatusTimeSinceCounterReset,'moduleStatusTemperature':moduleStatusTemperature,'moduleStatusTooHot':moduleStatusTooHot,'moduleStatusBackupState':moduleStatusBackupState,'moduleStatusBackupCounter':moduleStatusBackupCounter,'moduleStatusBackupDuration':moduleStatusBackupDuration,'portStatusTable':portStatusTable,'portStatusEntry':portStatusEntry,_BK:portStatusPortIndex,'portStatusModule':portStatusModule,'portStatusLocation':portStatusLocation,'portStatusSnmpPort':portStatusSnmpPort,'portStatusAlias':portStatusAlias,'portStatusAdminStatus':portStatusAdminStatus,'portStatusOperStatus':portStatusOperStatus,'portStatusDetailedStatus':portStatusDetailedStatus,'portStatusPortDatarate':portStatusPortDatarate,'portStatusUpdateTimeStamp':portStatusUpdateTimeStamp,'portStatusTimeSinceValueReset':portStatusTimeSinceValueReset,'portStatusTimeSinceLastError':portStatusTimeSinceLastError,'portStatusTimeSignalTooLow':portStatusTimeSignalTooLow,'portStatusSignalTooLowCounter':portStatusSignalTooLowCounter,'portStatusTimeSignalTooHigh':portStatusTimeSignalTooHigh,'portStatusSignalTooHighCounter':portStatusSignalTooHighCounter,'portStatusLowThreshold':portStatusLowThreshold,'portStatusCurrentInputSignal':portStatusCurrentInputSignal,'portStatusHighThreshold':portStatusHighThreshold,'emStatusTable':emStatusTable,'emStatusEntry':emStatusEntry,_BL:emStatusIndex,'emStatusSystemOk':emStatusSystemOk,'emStatusErrors':emStatusErrors,'emStatusHardwareCode':emStatusHardwareCode,'emStatusTimeSincePowerError':emStatusTimeSincePowerError,'emStatusTimeWithPowerLoss':emStatusTimeWithPowerLoss,'emStatusInputSignalLowCounter':emStatusInputSignalLowCounter,'emStatusInputPower':emStatusInputPower,'emStatusSignalGain':emStatusSignalGain,'emStatusOptimalFlatGain':emStatusOptimalFlatGain,'emStatusBackReflection':emStatusBackReflection,'emStatusSignalOutputPower':emStatusSignalOutputPower,'emStatusTotalOutputPower':emStatusTotalOutputPower,'emStatusMinOutputPower':emStatusMinOutputPower,'emStatusMaxOutputPower':emStatusMaxOutputPower,'emStatusCfgOutputPower':emStatusCfgOutputPower,'bertStatusTable':bertStatusTable,'bertStatusEntry':bertStatusEntry,_BM:bertStatusIndex,'bertStatusLocation':bertStatusLocation,'bertStatusBertOperation':bertStatusBertOperation,'bertStatusTotalErrors':bertStatusTotalErrors,'bertStatusTimeSinceLastError':bertStatusTimeSinceLastError,'bertStatusTotalTestTime':bertStatusTotalTestTime,'bertStatusErroredTime':bertStatusErroredTime,'bertStatusBitErrorRate':bertStatusBitErrorRate,'bertStatusBerSinceLastError':bertStatusBerSinceLastError,'bertStatusTheoreticalBer':bertStatusTheoreticalBer,'bertStatusAvailability':bertStatusAvailability})