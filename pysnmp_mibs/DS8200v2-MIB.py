_An='netAPSHist30Index'
_Am='netAPSHist30ifIndex'
_Al='netAPSHist30FarIndex'
_Ak='netAPSHist30NearIndex'
_Aj='statSummary'
_Ai='netAPSHist24Index'
_Ah='netAPSHist24ifIndex'
_Ag='netAPSHist24FarIndex'
_Af='netAPSHist24NearIndex'
_Ae='triggered'
_Ad='netAPSConfigifIndex'
_Ac='netAPSConfigFarIndex'
_Ab='netAPSConfigNearIndex'
_Aa='labelTableIndex'
_AZ='unitUtilitiesFarIndex'
_AY='unitUtilitiesNearIndex'
_AX='traplogIndex'
_AW='iTableIndex'
_AV='iTableFarIndex'
_AU='iTableNearIndex'
_AT='performance30Index'
_AS='performance30InterfaceIndex'
_AR='performance30FarIndex'
_AQ='performance30NearIndex'
_AP='performance24Index'
_AO='performance24InterfaceIndex'
_AN='performance24FarIndex'
_AM='performance24NearIndex'
_AL='testTableIndex'
_AK='testFarIndex'
_AJ='testNearIndex'
_AI='bertInterfaceIndex'
_AH='bertChipIndex'
_AG='bertInterfaceFarIndex'
_AF='bertInterfaceNearIndex'
_AE='bertIndex'
_AD='bertFarIndex'
_AC='bertNearIndex'
_AB='connectionChannelIndex'
_AA='connectionChannelLineIndex'
_A9='connectionChannelFarIndex'
_A8='connectionChannelNearIndex'
_A7='connectionTableIndex'
_A6='connectionFarIndex'
_A5='connectionNearIndex'
_A4='analogDteIndex'
_A3='analogDteFarIndex'
_A2='analogDteNearIndex'
_A1='serialDteDTRAlarmOther'
_A0='serialDteAlarmIndex'
_z='serialDteAlarmFarIndex'
_y='serialDteAlarmNearIndex'
_x='serialDteConfigIndex'
_w='serialDteConfigFarIndex'
_v='serialDteConfigNearIndex'
_u='ddsNetAlarmIndex'
_t='ddsNetAlarmFarIndex'
_s='ddsNetAlarmNearIndex'
_r='ddsNetConfigIndex'
_q='ddsNetConfigFarIndex'
_p='ddsNetConfigNearIndex'
_o='t1e1AlarmIndex'
_n='t1e1AlarmFarIndex'
_m='t1e1AlarmNearIndex'
_l='t1e1ConfigIndex'
_k='t1e1ConfigFarIndex'
_j='t1e1ConfigNearIndex'
_i='dbuStartStopDayOfWeek'
_h='dbuStartStopConfigEntryIndex'
_g='dbuStartStopFarIndex'
_f='dbuStartStopNearIndex'
_e='dbuResetStringsIndex'
_d='dbuResetConfigEntryIndex'
_c='dbuResetFarIndex'
_b='dbuResetNearIndex'
_a='dbuActivatorBPV'
_Z='dbuActivatorAIS'
_Y='dbuActivatorRAS'
_X='dbuActivatorLOF'
_W='dbuActivatorUAS'
_V='dbuActivatorSES'
_U='dbuActivatorES'
_T='dbuActivatorAny'
_S='dbuActivatorOOF'
_R='dbuActivatorOOS'
_Q='dbuActivatorLOS'
_P='dbuActivatorOther'
_O='dbuConfigTableIndex'
_N='dbuFarIndex'
_M='dbuNearIndex'
_L='mgmtPortsTableIndex'
_K='t1e1StatusOther'
_J='enabled'
_I='OctetString'
_H='disabled'
_G='other'
_F='DisplayString'
_E='DS8200v2-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hbu,verilink=mibBuilder.importSymbols('DS8200v2-TC-MIB','hbu','verilink')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
tinterfaces=ModuleIdentity((1,3,6,1,4,1,321,100,2))
_MgmtPorts_ObjectIdentity=ObjectIdentity
mgmtPorts=_MgmtPorts_ObjectIdentity((1,3,6,1,4,1,321,100,2,1))
_MgmtPortsTable_Object=MibTable
mgmtPortsTable=_MgmtPortsTable_Object((1,3,6,1,4,1,321,100,2,1,1))
if mibBuilder.loadTexts:mgmtPortsTable.setStatus(_A)
_MgmtPortsTableEntry_Object=MibTableRow
mgmtPortsTableEntry=_MgmtPortsTableEntry_Object((1,3,6,1,4,1,321,100,2,1,1,1))
mgmtPortsTableEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:mgmtPortsTableEntry.setStatus(_A)
_MgmtPortsTableIndex_Type=Integer32
_MgmtPortsTableIndex_Object=MibTableColumn
mgmtPortsTableIndex=_MgmtPortsTableIndex_Object((1,3,6,1,4,1,321,100,2,1,1,1,1),_MgmtPortsTableIndex_Type())
mgmtPortsTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtPortsTableIndex.setStatus(_A)
class _MgmtPortsDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_MgmtPortsDescription_Type.__name__=_F
_MgmtPortsDescription_Object=MibTableColumn
mgmtPortsDescription=_MgmtPortsDescription_Object((1,3,6,1,4,1,321,100,2,1,1,1,2),_MgmtPortsDescription_Type())
mgmtPortsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtPortsDescription.setStatus(_A)
class _MgmtPortsElementID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,27))
_MgmtPortsElementID_Type.__name__=_F
_MgmtPortsElementID_Object=MibTableColumn
mgmtPortsElementID=_MgmtPortsElementID_Object((1,3,6,1,4,1,321,100,2,1,1,1,3),_MgmtPortsElementID_Type())
mgmtPortsElementID.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmtPortsElementID.setStatus(_A)
class _MgmtPortsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),(_H,2),('coadial',3),('coadirect',4),('extAlarmOnOpen',5),('extAlarmOnClosed',6),('slipdial',7),('slipdirect',8)))
_MgmtPortsMode_Type.__name__=_C
_MgmtPortsMode_Object=MibTableColumn
mgmtPortsMode=_MgmtPortsMode_Object((1,3,6,1,4,1,321,100,2,1,1,1,4),_MgmtPortsMode_Type())
mgmtPortsMode.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmtPortsMode.setStatus(_A)
class _MgmtPortsDialPrefix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_MgmtPortsDialPrefix_Type.__name__=_F
_MgmtPortsDialPrefix_Object=MibTableColumn
mgmtPortsDialPrefix=_MgmtPortsDialPrefix_Object((1,3,6,1,4,1,321,100,2,1,1,1,5),_MgmtPortsDialPrefix_Type())
mgmtPortsDialPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmtPortsDialPrefix.setStatus(_A)
class _MgmtPortsPrimaryDialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_MgmtPortsPrimaryDialString_Type.__name__=_F
_MgmtPortsPrimaryDialString_Object=MibTableColumn
mgmtPortsPrimaryDialString=_MgmtPortsPrimaryDialString_Object((1,3,6,1,4,1,321,100,2,1,1,1,6),_MgmtPortsPrimaryDialString_Type())
mgmtPortsPrimaryDialString.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmtPortsPrimaryDialString.setStatus(_A)
class _MgmtPortsSecondaryDialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_MgmtPortsSecondaryDialString_Type.__name__=_F
_MgmtPortsSecondaryDialString_Object=MibTableColumn
mgmtPortsSecondaryDialString=_MgmtPortsSecondaryDialString_Object((1,3,6,1,4,1,321,100,2,1,1,1,7),_MgmtPortsSecondaryDialString_Type())
mgmtPortsSecondaryDialString.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmtPortsSecondaryDialString.setStatus(_A)
class _MgmtPortsExtInitString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_MgmtPortsExtInitString_Type.__name__=_F
_MgmtPortsExtInitString_Object=MibTableColumn
mgmtPortsExtInitString=_MgmtPortsExtInitString_Object((1,3,6,1,4,1,321,100,2,1,1,1,8),_MgmtPortsExtInitString_Type())
mgmtPortsExtInitString.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmtPortsExtInitString.setStatus(_A)
class _MgmtPortsCompressedSlip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_J,2),(_H,3),('auto',4)))
_MgmtPortsCompressedSlip_Type.__name__=_C
_MgmtPortsCompressedSlip_Object=MibTableColumn
mgmtPortsCompressedSlip=_MgmtPortsCompressedSlip_Object((1,3,6,1,4,1,321,100,2,1,1,1,9),_MgmtPortsCompressedSlip_Type())
mgmtPortsCompressedSlip.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmtPortsCompressedSlip.setStatus(_A)
class _MgmtPortsInternalModem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('notPresent',2),(_J,3),(_H,4)))
_MgmtPortsInternalModem_Type.__name__=_C
_MgmtPortsInternalModem_Object=MibTableColumn
mgmtPortsInternalModem=_MgmtPortsInternalModem_Object((1,3,6,1,4,1,321,100,2,1,1,1,10),_MgmtPortsInternalModem_Type())
mgmtPortsInternalModem.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmtPortsInternalModem.setStatus(_A)
_Dbu_ObjectIdentity=ObjectIdentity
dbu=_Dbu_ObjectIdentity((1,3,6,1,4,1,321,100,2,2))
_DbuConfigTable_Object=MibTable
dbuConfigTable=_DbuConfigTable_Object((1,3,6,1,4,1,321,100,2,2,1))
if mibBuilder.loadTexts:dbuConfigTable.setStatus(_A)
_DbuConfigTableEntry_Object=MibTableRow
dbuConfigTableEntry=_DbuConfigTableEntry_Object((1,3,6,1,4,1,321,100,2,2,1,1))
dbuConfigTableEntry.setIndexNames((0,_E,_M),(0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:dbuConfigTableEntry.setStatus(_A)
_DbuNearIndex_Type=Integer32
_DbuNearIndex_Object=MibTableColumn
dbuNearIndex=_DbuNearIndex_Object((1,3,6,1,4,1,321,100,2,2,1,1,1),_DbuNearIndex_Type())
dbuNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuNearIndex.setStatus(_A)
_DbuFarIndex_Type=Integer32
_DbuFarIndex_Object=MibTableColumn
dbuFarIndex=_DbuFarIndex_Object((1,3,6,1,4,1,321,100,2,2,1,1,2),_DbuFarIndex_Type())
dbuFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuFarIndex.setStatus(_A)
_DbuConfigTableIndex_Type=Integer32
_DbuConfigTableIndex_Object=MibTableColumn
dbuConfigTableIndex=_DbuConfigTableIndex_Object((1,3,6,1,4,1,321,100,2,2,1,1,3),_DbuConfigTableIndex_Type())
dbuConfigTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuConfigTableIndex.setStatus(_A)
class _DbuDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DbuDescription_Type.__name__=_F
_DbuDescription_Object=MibTableColumn
dbuDescription=_DbuDescription_Object((1,3,6,1,4,1,321,100,2,2,1,1,4),_DbuDescription_Type())
dbuDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuDescription.setStatus(_A)
class _DbuRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('dbuRateOther',1),('dbuRate2400',2),('dbuRate4800',3),('dbuRate9600',4),('dbuRate19200',5),('dbuRate38400',6),('dbuRate56000',7),('dbuRate57600',8),('dbuRate64000',9)))
_DbuRate_Type.__name__=_C
_DbuRate_Object=MibTableColumn
dbuRate=_DbuRate_Object((1,3,6,1,4,1,321,100,2,2,1,1,5),_DbuRate_Type())
dbuRate.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuRate.setStatus(_A)
class _DbuMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('dbuModeOther',1),('dbuModeOrig',2),('dbuModeAnsw',3),('dbuModeNotAvail',4),('dbuModeCallbackOrig',5),('dbuModeCallbackAnsw',6),('dbuModeMaster',7),('dbuModeSlave',8)))
_DbuMode_Type.__name__=_C
_DbuMode_Object=MibTableColumn
dbuMode=_DbuMode_Object((1,3,6,1,4,1,321,100,2,2,1,1,6),_DbuMode_Type())
dbuMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuMode.setStatus(_A)
class _DbuFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dbuFormatOther',1),('dbuFormatSync',2),('dbuFormatAsync',3),('dbuFormatNotAvail',4)))
_DbuFormat_Type.__name__=_C
_DbuFormat_Object=MibTableColumn
dbuFormat=_DbuFormat_Object((1,3,6,1,4,1,321,100,2,2,1,1,7),_DbuFormat_Type())
dbuFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuFormat.setStatus(_A)
class _DbuNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_DbuNumber_Type.__name__=_F
_DbuNumber_Object=MibTableColumn
dbuNumber=_DbuNumber_Object((1,3,6,1,4,1,321,100,2,2,1,1,8),_DbuNumber_Type())
dbuNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuNumber.setStatus(_A)
class _DbuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('dbuStatusOther',1),('dbuStatusDisabled',2),('dbuStatusEnabled',3),('dbuStatusActive',4),('dbuStatusLocked',5),('dbuStatusConnecting',6),('dbuStatusDisallowed',7),('dbuStatusAwaitingCall',8),('dbuStatusDialing',9),('dbuStatusDisconnecting',10),('dbuStatusTesting',11),('dbuStatusTestPassed',12),('dbuStatusTestFailed',13)))
_DbuStatus_Type.__name__=_C
_DbuStatus_Object=MibTableColumn
dbuStatus=_DbuStatus_Object((1,3,6,1,4,1,321,100,2,2,1,1,9),_DbuStatus_Type())
dbuStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuStatus.setStatus(_A)
class _DbuCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('dbuCommandOther',1),('dbuCommandDisable',2),('dbuCommandEnable',3),('dbuCommandActivate',4),('dbuCommandLock',5),('dbuCommandEnableDaily',6),('dbuCommandTest',7)))
_DbuCommand_Type.__name__=_C
_DbuCommand_Object=MibTableColumn
dbuCommand=_DbuCommand_Object((1,3,6,1,4,1,321,100,2,2,1,1,10),_DbuCommand_Type())
dbuCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuCommand.setStatus(_A)
class _DbuActivator1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12)))
_DbuActivator1_Type.__name__=_C
_DbuActivator1_Object=MibTableColumn
dbuActivator1=_DbuActivator1_Object((1,3,6,1,4,1,321,100,2,2,1,1,11),_DbuActivator1_Type())
dbuActivator1.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuActivator1.setStatus(_A)
class _DbuActivator2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12)))
_DbuActivator2_Type.__name__=_C
_DbuActivator2_Object=MibTableColumn
dbuActivator2=_DbuActivator2_Object((1,3,6,1,4,1,321,100,2,2,1,1,12),_DbuActivator2_Type())
dbuActivator2.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuActivator2.setStatus(_A)
class _DbuDialStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_DbuDialStr_Type.__name__=_F
_DbuDialStr_Object=MibTableColumn
dbuDialStr=_DbuDialStr_Object((1,3,6,1,4,1,321,100,2,2,1,1,13),_DbuDialStr_Type())
dbuDialStr.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuDialStr.setStatus(_A)
class _DbuInitStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_DbuInitStr_Type.__name__=_F
_DbuInitStr_Object=MibTableColumn
dbuInitStr=_DbuInitStr_Object((1,3,6,1,4,1,321,100,2,2,1,1,14),_DbuInitStr_Type())
dbuInitStr.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuInitStr.setStatus(_A)
class _DbuHangupStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_DbuHangupStr_Type.__name__=_F
_DbuHangupStr_Object=MibTableColumn
dbuHangupStr=_DbuHangupStr_Object((1,3,6,1,4,1,321,100,2,2,1,1,15),_DbuHangupStr_Type())
dbuHangupStr.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuHangupStr.setStatus(_A)
class _DbuPasswordStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DbuPasswordStr_Type.__name__=_F
_DbuPasswordStr_Object=MibTableColumn
dbuPasswordStr=_DbuPasswordStr_Object((1,3,6,1,4,1,321,100,2,2,1,1,16),_DbuPasswordStr_Type())
dbuPasswordStr.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuPasswordStr.setStatus(_A)
class _DbuSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dbuSecurityOther',1),('dbuSecurityDisable',2),('dbuSecurityEnable',3)))
_DbuSecurity_Type.__name__=_C
_DbuSecurity_Object=MibTableColumn
dbuSecurity=_DbuSecurity_Object((1,3,6,1,4,1,321,100,2,2,1,1,17),_DbuSecurity_Type())
dbuSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuSecurity.setStatus(_A)
class _DbuDtrDial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dbuDtrDialOther',1),('dbuDtrDialDisable',2),('dbuDtrDialEnable',3)))
_DbuDtrDial_Type.__name__=_C
_DbuDtrDial_Object=MibTableColumn
dbuDtrDial=_DbuDtrDial_Object((1,3,6,1,4,1,321,100,2,2,1,1,18),_DbuDtrDial_Type())
dbuDtrDial.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuDtrDial.setStatus(_A)
_DbuISDNSwitchType_Type=Integer32
_DbuISDNSwitchType_Object=MibTableColumn
dbuISDNSwitchType=_DbuISDNSwitchType_Object((1,3,6,1,4,1,321,100,2,2,1,1,19),_DbuISDNSwitchType_Type())
dbuISDNSwitchType.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuISDNSwitchType.setStatus(_A)
class _DbuISDNSwitchVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dbuISDNSwitchVersionOther',1),('dbuISDNSwitchVersionNational1',2),('dbuISDNSwitchVersionATTP2P',3),('dbuISDNSwitchVersionATTMP',4),('dbuISDNSwitchVersionDMS100PVCIC0',5),('dbuISDNSwitchVersionDMS100PVCIC1',6)))
_DbuISDNSwitchVersion_Type.__name__=_C
_DbuISDNSwitchVersion_Object=MibTableColumn
dbuISDNSwitchVersion=_DbuISDNSwitchVersion_Object((1,3,6,1,4,1,321,100,2,2,1,1,20),_DbuISDNSwitchVersion_Type())
dbuISDNSwitchVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuISDNSwitchVersion.setStatus(_A)
class _DbuISDNTEI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67)));namedValues=NamedValues(*(('dbuISDNTEIOther',1),('dbuISDNTEIDisable',2),('dbuISDNTEIAuto',3),('dbuISDNTEI0',4),('dbuISDNTEI1',5),('dbuISDNTEI2',6),('dbuISDNTEI3',7),('dbuISDNTEI4',8),('dbuISDNTEI5',9),('dbuISDNTEI6',10),('dbuISDNTEI7',11),('dbuISDNTEI8',12),('dbuISDNTEI9',13),('dbuISDNTEI10',14),('dbuISDNTEI11',15),('dbuISDNTEI12',16),('dbuISDNTEI13',17),('dbuISDNTEI14',18),('dbuISDNTEI15',19),('dbuISDNTEI16',20),('dbuISDNTEI17',21),('dbuISDNTEI18',22),('dbuISDNTEI19',23),('dbuISDNTEI20',24),('dbuISDNTEI21',25),('dbuISDNTEI22',26),('dbuISDNTEI23',27),('dbuISDNTEI24',28),('dbuISDNTEI25',29),('dbuISDNTEI26',30),('dbuISDNTEI27',31),('dbuISDNTEI28',32),('dbuISDNTEI29',33),('dbuISDNTEI30',34),('dbuISDNTEI31',35),('dbuISDNTEI32',36),('dbuISDNTEI33',37),('dbuISDNTEI34',38),('dbuISDNTEI35',39),('dbuISDNTEI36',40),('dbuISDNTEI37',41),('dbuISDNTEI38',42),('dbuISDNTEI39',43),('dbuISDNTEI40',44),('dbuISDNTEI41',45),('dbuISDNTEI42',46),('dbuISDNTEI43',47),('dbuISDNTEI44',48),('dbuISDNTEI45',49),('dbuISDNTEI46',50),('dbuISDNTEI47',51),('dbuISDNTEI48',52),('dbuISDNTEI49',53),('dbuISDNTEI50',54),('dbuISDNTEI51',55),('dbuISDNTEI52',56),('dbuISDNTEI53',57),('dbuISDNTEI54',58),('dbuISDNTEI55',59),('dbuISDNTEI56',60),('dbuISDNTEI57',61),('dbuISDNTEI58',62),('dbuISDNTEI59',63),('dbuISDNTEI60',64),('dbuISDNTEI61',65),('dbuISDNTEI62',66),('dbuISDNTEI63',67)))
_DbuISDNTEI_Type.__name__=_C
_DbuISDNTEI_Object=MibTableColumn
dbuISDNTEI=_DbuISDNTEI_Object((1,3,6,1,4,1,321,100,2,2,1,1,21),_DbuISDNTEI_Type())
dbuISDNTEI.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuISDNTEI.setStatus(_A)
class _DbuISDNSPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DbuISDNSPID_Type.__name__=_F
_DbuISDNSPID_Object=MibTableColumn
dbuISDNSPID=_DbuISDNSPID_Object((1,3,6,1,4,1,321,100,2,2,1,1,22),_DbuISDNSPID_Type())
dbuISDNSPID.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuISDNSPID.setStatus(_A)
class _DbuISDNDDNUM_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DbuISDNDDNUM_Type.__name__=_F
_DbuISDNDDNUM_Object=MibTableColumn
dbuISDNDDNUM=_DbuISDNDDNUM_Object((1,3,6,1,4,1,321,100,2,2,1,1,23),_DbuISDNDDNUM_Type())
dbuISDNDDNUM.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuISDNDDNUM.setStatus(_A)
_DbuResetStringsTable_Object=MibTable
dbuResetStringsTable=_DbuResetStringsTable_Object((1,3,6,1,4,1,321,100,2,2,2))
if mibBuilder.loadTexts:dbuResetStringsTable.setStatus(_A)
_DbuResetStringsEntry_Object=MibTableRow
dbuResetStringsEntry=_DbuResetStringsEntry_Object((1,3,6,1,4,1,321,100,2,2,2,1))
dbuResetStringsEntry.setIndexNames((0,_E,_b),(0,_E,_c),(0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:dbuResetStringsEntry.setStatus(_A)
_DbuResetNearIndex_Type=Integer32
_DbuResetNearIndex_Object=MibTableColumn
dbuResetNearIndex=_DbuResetNearIndex_Object((1,3,6,1,4,1,321,100,2,2,2,1,1),_DbuResetNearIndex_Type())
dbuResetNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuResetNearIndex.setStatus(_A)
_DbuResetFarIndex_Type=Integer32
_DbuResetFarIndex_Object=MibTableColumn
dbuResetFarIndex=_DbuResetFarIndex_Object((1,3,6,1,4,1,321,100,2,2,2,1,2),_DbuResetFarIndex_Type())
dbuResetFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuResetFarIndex.setStatus(_A)
_DbuResetConfigEntryIndex_Type=Integer32
_DbuResetConfigEntryIndex_Object=MibTableColumn
dbuResetConfigEntryIndex=_DbuResetConfigEntryIndex_Object((1,3,6,1,4,1,321,100,2,2,2,1,3),_DbuResetConfigEntryIndex_Type())
dbuResetConfigEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuResetConfigEntryIndex.setStatus(_A)
_DbuResetStringsIndex_Type=Integer32
_DbuResetStringsIndex_Object=MibTableColumn
dbuResetStringsIndex=_DbuResetStringsIndex_Object((1,3,6,1,4,1,321,100,2,2,2,1,4),_DbuResetStringsIndex_Type())
dbuResetStringsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuResetStringsIndex.setStatus(_A)
class _DbuResetString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_DbuResetString_Type.__name__=_F
_DbuResetString_Object=MibTableColumn
dbuResetString=_DbuResetString_Object((1,3,6,1,4,1,321,100,2,2,2,1,5),_DbuResetString_Type())
dbuResetString.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuResetString.setStatus(_A)
_DbuStartStopTable_Object=MibTable
dbuStartStopTable=_DbuStartStopTable_Object((1,3,6,1,4,1,321,100,2,2,3))
if mibBuilder.loadTexts:dbuStartStopTable.setStatus(_A)
_DbuStartStopTableEntry_Object=MibTableRow
dbuStartStopTableEntry=_DbuStartStopTableEntry_Object((1,3,6,1,4,1,321,100,2,2,3,1))
dbuStartStopTableEntry.setIndexNames((0,_E,_f),(0,_E,_g),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:dbuStartStopTableEntry.setStatus(_A)
_DbuStartStopNearIndex_Type=Integer32
_DbuStartStopNearIndex_Object=MibTableColumn
dbuStartStopNearIndex=_DbuStartStopNearIndex_Object((1,3,6,1,4,1,321,100,2,2,3,1,1),_DbuStartStopNearIndex_Type())
dbuStartStopNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuStartStopNearIndex.setStatus(_A)
_DbuStartStopFarIndex_Type=Integer32
_DbuStartStopFarIndex_Object=MibTableColumn
dbuStartStopFarIndex=_DbuStartStopFarIndex_Object((1,3,6,1,4,1,321,100,2,2,3,1,2),_DbuStartStopFarIndex_Type())
dbuStartStopFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuStartStopFarIndex.setStatus(_A)
_DbuStartStopConfigEntryIndex_Type=Integer32
_DbuStartStopConfigEntryIndex_Object=MibTableColumn
dbuStartStopConfigEntryIndex=_DbuStartStopConfigEntryIndex_Object((1,3,6,1,4,1,321,100,2,2,3,1,3),_DbuStartStopConfigEntryIndex_Type())
dbuStartStopConfigEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuStartStopConfigEntryIndex.setStatus(_A)
class _DbuStartStopDayOfWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('dbuStartStopSunday',1),('dbuStartStopMonday',2),('dbuStartStopTuesday',3),('dbuStartStopWednesday',4),('dbuStartStopThursday',5),('dbuStartStopFriday',6),('dbuStartStopSaturday',7)))
_DbuStartStopDayOfWeek_Type.__name__=_C
_DbuStartStopDayOfWeek_Object=MibTableColumn
dbuStartStopDayOfWeek=_DbuStartStopDayOfWeek_Object((1,3,6,1,4,1,321,100,2,2,3,1,4),_DbuStartStopDayOfWeek_Type())
dbuStartStopDayOfWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:dbuStartStopDayOfWeek.setStatus(_A)
class _DbuStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('dbuStartHour00',1),('dbuStartHour01',2),('dbuStartHour02',3),('dbuStartHour03',4),('dbuStartHour04',5),('dbuStartHour05',6),('dbuStartHour06',7),('dbuStartHour07',8),('dbuStartHour08',9),('dbuStartHour09',10),('dbuStartHour10',11),('dbuStartHour11',12),('dbuStartHour12',13),('dbuStartHour13',14),('dbuStartHour14',15),('dbuStartHour15',16),('dbuStartHour16',17),('dbuStartHour17',18),('dbuStartHour18',19),('dbuStartHour19',20),('dbuStartHour20',21),('dbuStartHour21',22),('dbuStartHour22',23),('dbuStartHour23',24)))
_DbuStart_Type.__name__=_C
_DbuStart_Object=MibTableColumn
dbuStart=_DbuStart_Object((1,3,6,1,4,1,321,100,2,2,3,1,5),_DbuStart_Type())
dbuStart.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuStart.setStatus(_A)
class _DbuStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('dbuStopHour00',1),('dbuStopHour01',2),('dbuStopHour02',3),('dbuStopHour03',4),('dbuStopHour04',5),('dbuStopHour05',6),('dbuStopHour06',7),('dbuStopHour07',8),('dbuStopHour08',9),('dbuStopHour09',10),('dbuStopHour10',11),('dbuStopHour11',12),('dbuStopHour12',13),('dbuStopHour13',14),('dbuStopHour14',15),('dbuStopHour15',16),('dbuStopHour16',17),('dbuStopHour17',18),('dbuStopHour18',19),('dbuStopHour19',20),('dbuStopHour20',21),('dbuStopHour21',22),('dbuStopHour22',23),('dbuStopHour23',24)))
_DbuStop_Type.__name__=_C
_DbuStop_Object=MibTableColumn
dbuStop=_DbuStop_Object((1,3,6,1,4,1,321,100,2,2,3,1,6),_DbuStop_Type())
dbuStop.setMaxAccess(_D)
if mibBuilder.loadTexts:dbuStop.setStatus(_A)
_T1e1_ObjectIdentity=ObjectIdentity
t1e1=_T1e1_ObjectIdentity((1,3,6,1,4,1,321,100,2,3))
_T1e1ConfigTable_Object=MibTable
t1e1ConfigTable=_T1e1ConfigTable_Object((1,3,6,1,4,1,321,100,2,3,1))
if mibBuilder.loadTexts:t1e1ConfigTable.setStatus(_A)
_T1e1ConfigTableEntry_Object=MibTableRow
t1e1ConfigTableEntry=_T1e1ConfigTableEntry_Object((1,3,6,1,4,1,321,100,2,3,1,1))
t1e1ConfigTableEntry.setIndexNames((0,_E,_j),(0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:t1e1ConfigTableEntry.setStatus(_A)
_T1e1ConfigNearIndex_Type=Integer32
_T1e1ConfigNearIndex_Object=MibTableColumn
t1e1ConfigNearIndex=_T1e1ConfigNearIndex_Object((1,3,6,1,4,1,321,100,2,3,1,1,1),_T1e1ConfigNearIndex_Type())
t1e1ConfigNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1ConfigNearIndex.setStatus(_A)
_T1e1ConfigFarIndex_Type=Integer32
_T1e1ConfigFarIndex_Object=MibTableColumn
t1e1ConfigFarIndex=_T1e1ConfigFarIndex_Object((1,3,6,1,4,1,321,100,2,3,1,1,2),_T1e1ConfigFarIndex_Type())
t1e1ConfigFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1ConfigFarIndex.setStatus(_A)
_T1e1ConfigIndex_Type=Integer32
_T1e1ConfigIndex_Object=MibTableColumn
t1e1ConfigIndex=_T1e1ConfigIndex_Object((1,3,6,1,4,1,321,100,2,3,1,1,3),_T1e1ConfigIndex_Type())
t1e1ConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1ConfigIndex.setStatus(_A)
class _T1e1Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_T1e1Description_Type.__name__=_F
_T1e1Description_Object=MibTableColumn
t1e1Description=_T1e1Description_Object((1,3,6,1,4,1,321,100,2,3,1,1,4),_T1e1Description_Type())
t1e1Description.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1Description.setStatus(_A)
class _T1e1Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1ModeOther',1),('t1e1ModeDTE',2),('t1e1ModeNetwork',3)))
_T1e1Mode_Type.__name__=_C
_T1e1Mode_Object=MibTableColumn
t1e1Mode=_T1e1Mode_Object((1,3,6,1,4,1,321,100,2,3,1,1,5),_T1e1Mode_Type())
t1e1Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1Mode.setStatus(_A)
class _T1e1FrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('t1e1FrameTypeOther',1),('t1e1FrameTypeESF',2),('t1e1FrameTypeD4',3),('t1e1FrameTypeCCSCRC',4),('t1e1FrameTypeCCS',5),('t1e1FrameTypeCAS',6),('t1e1FrameTypeCASCRC',7),('t1e1FrameTypeUnframed',8),('t1e1FrameTypeV3',9),('t1e1FrameTypeT1Unframed',10)))
_T1e1FrameType_Type.__name__=_C
_T1e1FrameType_Object=MibTableColumn
t1e1FrameType=_T1e1FrameType_Object((1,3,6,1,4,1,321,100,2,3,1,1,6),_T1e1FrameType_Type())
t1e1FrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1FrameType.setStatus(_A)
class _T1e1LineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('t1e1LineCodeOther',1),('t1e1LineCodeAMI',2),('t1e1LineCodeB8ZS',3),('t1e1LineCodeHDB3',4)))
_T1e1LineCode_Type.__name__=_C
_T1e1LineCode_Object=MibTableColumn
t1e1LineCode=_T1e1LineCode_Object((1,3,6,1,4,1,321,100,2,3,1,1,7),_T1e1LineCode_Type())
t1e1LineCode.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1LineCode.setStatus(_A)
class _T1e1LineBuildOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('t1e1LineBuildOutOther',1),('t1e1LineBuildOut0db',2),('t1e1LineBuildOut75db',3),('t1e1LineBuildOut15db',4),('t1e1LineBuildOut225db',5)))
_T1e1LineBuildOut_Type.__name__=_C
_T1e1LineBuildOut_Object=MibTableColumn
t1e1LineBuildOut=_T1e1LineBuildOut_Object((1,3,6,1,4,1,321,100,2,3,1,1,8),_T1e1LineBuildOut_Type())
t1e1LineBuildOut.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1LineBuildOut.setStatus(_A)
class _T1e1Timing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108)));namedValues=NamedValues(*(('t1e1TimingOther',1),('t1e1TimingInternal',2),('t1e1TimingNetwork',3),('t1e1TimingT1DTE',4),('t1e1TimingStation',5),('t1e1TimingStaClock',6),('t1e1TimingPort1',7),('t1e1TimingPort2',8),('t1e1TimingPort3',9),('t1e1TimingPort4',10),('t1e1TimingPort5',11),('t1e1TimingPort6',12),('t1e1TimingPort7',13),('t1e1TimingPort8',14),('t1e1TimingPort9',15),('t1e1TimingPort10',16),('t1e1TimingPort11',17),('t1e1TimingPort12',18),('t1e1TimingPort13',19),('t1e1TimingPort14',20),('t1e1TimingPort15',21),('t1e1TimingPort16',22),('t1e1TimingPort17',23),('t1e1TimingPort18',24),('t1e1TimingPort19',25),('t1e1TimingPort20',26),('t1e1TimingPort21',27),('t1e1TimingPort22',28),('t1e1TimingPort23',29),('t1e1TimingPort24',30),('t1e1TimingPort25',31),('t1e1TimingPort26',32),('t1e1TimingPort27',33),('t1e1TimingPort28',34),('t1e1TimingPort29',35),('t1e1TimingPort30',36),('t1e1TimingPort31',37),('t1e1TimingPort32',38),('t1e1TimingSlot2PortA',39),('t1e1TimingSlot2PortB',40),('t1e1TimingSlot3PortA',41),('t1e1TimingSlot3PortB',42),('t1e1TimingSlot4PortA',43),('t1e1TimingSlot4PortB',44),('t1e1TimingSlot5PortA',45),('t1e1TimingSlot5PortB',46),('t1e1TimingSlot6PortA',47),('t1e1TimingSlot6PortB',48),('t1e1TimingSlot2Dsu1PortA',49),('t1e1TimingSlot2Dsu1PortB',50),('t1e1TimingSlot2Dsu2PortA',51),('t1e1TimingSlot2Dsu2PortB',52),('t1e1TimingSlot2Dsu3PortA',53),('t1e1TimingSlot2Dsu3PortB',54),('t1e1TimingSlot2Dsu4PortA',55),('t1e1TimingSlot2Dsu4PortB',56),('t1e1TimingSlot2Dsu5PortA',57),('t1e1TimingSlot2Dsu5PortB',58),('t1e1TimingSlot2Dsu6PortA',59),('t1e1TimingSlot2Dsu6PortB',60),('t1e1TimingSlot3Dsu1PortA',61),('t1e1TimingSlot3Dsu1PortB',62),('t1e1TimingSlot3Dsu2PortA',63),('t1e1TimingSlot3Dsu2PortB',64),('t1e1TimingSlot3Dsu3PortA',65),('t1e1TimingSlot3Dsu3PortB',66),('t1e1TimingSlot3Dsu4PortA',67),('t1e1TimingSlot3Dsu4PortB',68),('t1e1TimingSlot3Dsu5PortA',69),('t1e1TimingSlot3Dsu5PortB',70),('t1e1TimingSlot3Dsu6PortA',71),('t1e1TimingSlot3Dsu6PortB',72),('t1e1TimingSlot4Dsu1PortA',73),('t1e1TimingSlot4Dsu1PortB',74),('t1e1TimingSlot4Dsu2PortA',75),('t1e1TimingSlot4Dsu2PortB',76),('t1e1TimingSlot4Dsu3PortA',77),('t1e1TimingSlot4Dsu3PortB',78),('t1e1TimingSlot4Dsu4PortA',79),('t1e1TimingSlot4Dsu4PortB',80),('t1e1TimingSlot4Dsu5PortA',81),('t1e1TimingSlot4Dsu5PortB',82),('t1e1TimingSlot4Dsu6PortA',83),('t1e1TimingSlot4Dsu6PortB',84),('t1e1TimingSlot5Dsu1PortA',85),('t1e1TimingSlot5Dsu1PortB',86),('t1e1TimingSlot5Dsu2PortA',87),('t1e1TimingSlot5Dsu2PortB',88),('t1e1TimingSlot5Dsu3PortA',89),('t1e1TimingSlot5Dsu3PortB',90),('t1e1TimingSlot5Dsu4PortA',91),('t1e1TimingSlot5Dsu4PortB',92),('t1e1TimingSlot5Dsu5PortA',93),('t1e1TimingSlot5Dsu5PortB',94),('t1e1TimingSlot5Dsu6PortA',95),('t1e1TimingSlot5Dsu6PortB',96),('t1e1TimingSlot6Dsu1PortA',97),('t1e1TimingSlot6Dsu1PortB',98),('t1e1TimingSlot6Dsu2PortA',99),('t1e1TimingSlot6Dsu2PortB',100),('t1e1TimingSlot6Dsu3PortA',101),('t1e1TimingSlot6Dsu3PortB',102),('t1e1TimingSlot6Dsu4PortA',103),('t1e1TimingSlot6Dsu4PortB',104),('t1e1TimingSlot6Dsu5PortA',105),('t1e1TimingSlot6Dsu5PortB',106),('t1e1TimingSlot6Dsu6PortA',107),('t1e1TimingSlot6Dsu6PortB',108)))
_T1e1Timing_Type.__name__=_C
_T1e1Timing_Object=MibTableColumn
t1e1Timing=_T1e1Timing_Object((1,3,6,1,4,1,321,100,2,3,1,1,9),_T1e1Timing_Type())
t1e1Timing.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1Timing.setStatus(_A)
class _T1e1StationInTiming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('t1e1StationInTimingOther',1),('t1e1StationInTimingNX56',2),('t1e1StationInTimingNX64',3),('t1e1StationInTiming1544',4),('t1e1StationInTiming2048',5)))
_T1e1StationInTiming_Type.__name__=_C
_T1e1StationInTiming_Object=MibTableColumn
t1e1StationInTiming=_T1e1StationInTiming_Object((1,3,6,1,4,1,321,100,2,3,1,1,10),_T1e1StationInTiming_Type())
t1e1StationInTiming.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1StationInTiming.setStatus(_A)
_T1e1StationTiming_Type=Integer32
_T1e1StationTiming_Object=MibTableColumn
t1e1StationTiming=_T1e1StationTiming_Object((1,3,6,1,4,1,321,100,2,3,1,1,11),_T1e1StationTiming_Type())
t1e1StationTiming.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1StationTiming.setStatus(_A)
class _T1e1PRM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1PRMOther',1),('t1e1PRMDisable',2),('t1e1PRMEnable',3)))
_T1e1PRM_Type.__name__=_C
_T1e1PRM_Object=MibTableColumn
t1e1PRM=_T1e1PRM_Object((1,3,6,1,4,1,321,100,2,3,1,1,12),_T1e1PRM_Type())
t1e1PRM.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1PRM.setStatus(_A)
class _T1e1ZeroSuppress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1ZeroOther',1),('t1e1ZeroDisable',2),('t1e1ZeroEnable',3)))
_T1e1ZeroSuppress_Type.__name__=_C
_T1e1ZeroSuppress_Object=MibTableColumn
t1e1ZeroSuppress=_T1e1ZeroSuppress_Object((1,3,6,1,4,1,321,100,2,3,1,1,13),_T1e1ZeroSuppress_Type())
t1e1ZeroSuppress.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1ZeroSuppress.setStatus(_A)
class _T1e1NationalBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('t1e1NationalOther',1),('t1e1NationalNone',2),('t1e1NationalSA4',3),('t1e1NationalSA5',4),('t1e1NationalSA6',5),('t1e1NationalSA7',6),('t1e1NationalSA8',7)))
_T1e1NationalBit_Type.__name__=_C
_T1e1NationalBit_Object=MibTableColumn
t1e1NationalBit=_T1e1NationalBit_Object((1,3,6,1,4,1,321,100,2,3,1,1,14),_T1e1NationalBit_Type())
t1e1NationalBit.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1NationalBit.setStatus(_A)
class _T1e1KeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('t1e1KeepAliveOther',1),('t1e1KeepAliveUnframedOnes',2),('t1e1KeepAliveFramedOnes',3),('t1e1KeepAliveLoop',4)))
_T1e1KeepAlive_Type.__name__=_C
_T1e1KeepAlive_Object=MibTableColumn
t1e1KeepAlive=_T1e1KeepAlive_Object((1,3,6,1,4,1,321,100,2,3,1,1,15),_T1e1KeepAlive_Type())
t1e1KeepAlive.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1KeepAlive.setStatus(_A)
class _T1e1CRC4Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1CRC4Other',1),('t1e1CRC4Disabled',2),('t1e1CRC4Enabled',3)))
_T1e1CRC4Mode_Type.__name__=_C
_T1e1CRC4Mode_Object=MibTableColumn
t1e1CRC4Mode=_T1e1CRC4Mode_Object((1,3,6,1,4,1,321,100,2,3,1,1,16),_T1e1CRC4Mode_Type())
t1e1CRC4Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1CRC4Mode.setStatus(_A)
class _T1e1DSXLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('t1e1DSXOther',1),('t1e1DSX0110',2),('t1e1DSX111220',3),('t1e1DSX221330',4),('t1e1DSX331440',5),('t1e1DSX441550',6),('t1e1DSX551660',7),('t1e1DSX661up',8)))
_T1e1DSXLevel_Type.__name__=_C
_T1e1DSXLevel_Object=MibTableColumn
t1e1DSXLevel=_T1e1DSXLevel_Object((1,3,6,1,4,1,321,100,2,3,1,1,17),_T1e1DSXLevel_Type())
t1e1DSXLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1DSXLevel.setStatus(_A)
class _T1e1CRC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1CRCOther',1),('t1e1CRCPass',2),('t1e1CRCRegenerate',3)))
_T1e1CRC_Type.__name__=_C
_T1e1CRC_Object=MibTableColumn
t1e1CRC=_T1e1CRC_Object((1,3,6,1,4,1,321,100,2,3,1,1,18),_T1e1CRC_Type())
t1e1CRC.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1CRC.setStatus(_A)
class _T1e1FDLPassThrough_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1FDLPassThroughOther',1),('t1e1FDLPassThroughPass',2),('t1e1FDLPassThroughTerminate',3)))
_T1e1FDLPassThrough_Type.__name__=_C
_T1e1FDLPassThrough_Object=MibTableColumn
t1e1FDLPassThrough=_T1e1FDLPassThrough_Object((1,3,6,1,4,1,321,100,2,3,1,1,19),_T1e1FDLPassThrough_Type())
t1e1FDLPassThrough.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1FDLPassThrough.setStatus(_A)
class _T1e1AudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1AudibleAlarmOther',1),('t1e1AudibleAlarmDisabled',2),('t1e1AudibleAlarmEnabled',3)))
_T1e1AudibleAlarm_Type.__name__=_C
_T1e1AudibleAlarm_Object=MibTableColumn
t1e1AudibleAlarm=_T1e1AudibleAlarm_Object((1,3,6,1,4,1,321,100,2,3,1,1,20),_T1e1AudibleAlarm_Type())
t1e1AudibleAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1AudibleAlarm.setStatus(_A)
class _T1e1Function_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('t1e1FunctionOther',1),('t1e1FunctionNetwork',2),('t1e1FunctionSlaved',3),('t1e1FunctionBackup',4)))
_T1e1Function_Type.__name__=_C
_T1e1Function_Object=MibTableColumn
t1e1Function=_T1e1Function_Object((1,3,6,1,4,1,321,100,2,3,1,1,21),_T1e1Function_Type())
t1e1Function.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1Function.setStatus(_A)
class _T1e1EBitGeneration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_J,3)))
_T1e1EBitGeneration_Type.__name__=_C
_T1e1EBitGeneration_Object=MibTableColumn
t1e1EBitGeneration=_T1e1EBitGeneration_Object((1,3,6,1,4,1,321,100,2,3,1,1,22),_T1e1EBitGeneration_Type())
t1e1EBitGeneration.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1EBitGeneration.setStatus(_A)
class _T1e1RAIGeneration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_J,3)))
_T1e1RAIGeneration_Type.__name__=_C
_T1e1RAIGeneration_Object=MibTableColumn
t1e1RAIGeneration=_T1e1RAIGeneration_Object((1,3,6,1,4,1,321,100,2,3,1,1,23),_T1e1RAIGeneration_Type())
t1e1RAIGeneration.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1RAIGeneration.setStatus(_A)
class _T1e1SpareBitInsertion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_J,3)))
_T1e1SpareBitInsertion_Type.__name__=_C
_T1e1SpareBitInsertion_Object=MibTableColumn
t1e1SpareBitInsertion=_T1e1SpareBitInsertion_Object((1,3,6,1,4,1,321,100,2,3,1,1,24),_T1e1SpareBitInsertion_Type())
t1e1SpareBitInsertion.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1SpareBitInsertion.setStatus(_A)
class _T1e1Sa4In_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa4In_Type.__name__=_I
_T1e1Sa4In_Object=MibTableColumn
t1e1Sa4In=_T1e1Sa4In_Object((1,3,6,1,4,1,321,100,2,3,1,1,25),_T1e1Sa4In_Type())
t1e1Sa4In.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1Sa4In.setStatus(_A)
class _T1e1Sa5In_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa5In_Type.__name__=_I
_T1e1Sa5In_Object=MibTableColumn
t1e1Sa5In=_T1e1Sa5In_Object((1,3,6,1,4,1,321,100,2,3,1,1,26),_T1e1Sa5In_Type())
t1e1Sa5In.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1Sa5In.setStatus(_A)
class _T1e1Sa6In_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa6In_Type.__name__=_I
_T1e1Sa6In_Object=MibTableColumn
t1e1Sa6In=_T1e1Sa6In_Object((1,3,6,1,4,1,321,100,2,3,1,1,27),_T1e1Sa6In_Type())
t1e1Sa6In.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1Sa6In.setStatus(_A)
class _T1e1Sa7In_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa7In_Type.__name__=_I
_T1e1Sa7In_Object=MibTableColumn
t1e1Sa7In=_T1e1Sa7In_Object((1,3,6,1,4,1,321,100,2,3,1,1,28),_T1e1Sa7In_Type())
t1e1Sa7In.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1Sa7In.setStatus(_A)
class _T1e1Sa8In_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa8In_Type.__name__=_I
_T1e1Sa8In_Object=MibTableColumn
t1e1Sa8In=_T1e1Sa8In_Object((1,3,6,1,4,1,321,100,2,3,1,1,29),_T1e1Sa8In_Type())
t1e1Sa8In.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1Sa8In.setStatus(_A)
class _T1e1Sa4Out_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa4Out_Type.__name__=_I
_T1e1Sa4Out_Object=MibTableColumn
t1e1Sa4Out=_T1e1Sa4Out_Object((1,3,6,1,4,1,321,100,2,3,1,1,30),_T1e1Sa4Out_Type())
t1e1Sa4Out.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1Sa4Out.setStatus(_A)
class _T1e1Sa5Out_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa5Out_Type.__name__=_I
_T1e1Sa5Out_Object=MibTableColumn
t1e1Sa5Out=_T1e1Sa5Out_Object((1,3,6,1,4,1,321,100,2,3,1,1,31),_T1e1Sa5Out_Type())
t1e1Sa5Out.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1Sa5Out.setStatus(_A)
class _T1e1Sa6Out_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa6Out_Type.__name__=_I
_T1e1Sa6Out_Object=MibTableColumn
t1e1Sa6Out=_T1e1Sa6Out_Object((1,3,6,1,4,1,321,100,2,3,1,1,32),_T1e1Sa6Out_Type())
t1e1Sa6Out.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1Sa6Out.setStatus(_A)
class _T1e1Sa7Out_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa7Out_Type.__name__=_I
_T1e1Sa7Out_Object=MibTableColumn
t1e1Sa7Out=_T1e1Sa7Out_Object((1,3,6,1,4,1,321,100,2,3,1,1,33),_T1e1Sa7Out_Type())
t1e1Sa7Out.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1Sa7Out.setStatus(_A)
class _T1e1Sa8Out_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_T1e1Sa8Out_Type.__name__=_I
_T1e1Sa8Out_Object=MibTableColumn
t1e1Sa8Out=_T1e1Sa8Out_Object((1,3,6,1,4,1,321,100,2,3,1,1,34),_T1e1Sa8Out_Type())
t1e1Sa8Out.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1Sa8Out.setStatus(_A)
_T1e1AlarmTable_Object=MibTable
t1e1AlarmTable=_T1e1AlarmTable_Object((1,3,6,1,4,1,321,100,2,3,2))
if mibBuilder.loadTexts:t1e1AlarmTable.setStatus(_A)
_T1e1AlarmTableEntry_Object=MibTableRow
t1e1AlarmTableEntry=_T1e1AlarmTableEntry_Object((1,3,6,1,4,1,321,100,2,3,2,1))
t1e1AlarmTableEntry.setIndexNames((0,_E,_m),(0,_E,_n),(0,_E,_o))
if mibBuilder.loadTexts:t1e1AlarmTableEntry.setStatus(_A)
_T1e1AlarmNearIndex_Type=Integer32
_T1e1AlarmNearIndex_Object=MibTableColumn
t1e1AlarmNearIndex=_T1e1AlarmNearIndex_Object((1,3,6,1,4,1,321,100,2,3,2,1,1),_T1e1AlarmNearIndex_Type())
t1e1AlarmNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1AlarmNearIndex.setStatus(_A)
_T1e1AlarmFarIndex_Type=Integer32
_T1e1AlarmFarIndex_Object=MibTableColumn
t1e1AlarmFarIndex=_T1e1AlarmFarIndex_Object((1,3,6,1,4,1,321,100,2,3,2,1,2),_T1e1AlarmFarIndex_Type())
t1e1AlarmFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1AlarmFarIndex.setStatus(_A)
_T1e1AlarmIndex_Type=Integer32
_T1e1AlarmIndex_Object=MibTableColumn
t1e1AlarmIndex=_T1e1AlarmIndex_Object((1,3,6,1,4,1,321,100,2,3,2,1,3),_T1e1AlarmIndex_Type())
t1e1AlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1AlarmIndex.setStatus(_A)
class _T1e1StatusSummary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_T1e1StatusSummary_Type.__name__=_F
_T1e1StatusSummary_Object=MibTableColumn
t1e1StatusSummary=_T1e1StatusSummary_Object((1,3,6,1,4,1,321,100,2,3,2,1,4),_T1e1StatusSummary_Type())
t1e1StatusSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1StatusSummary.setStatus(_A)
class _T1e1AlarmSummary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_T1e1AlarmSummary_Type.__name__=_F
_T1e1AlarmSummary_Object=MibTableColumn
t1e1AlarmSummary=_T1e1AlarmSummary_Object((1,3,6,1,4,1,321,100,2,3,2,1,5),_T1e1AlarmSummary_Type())
t1e1AlarmSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1AlarmSummary.setStatus(_A)
class _T1e1ESStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('t1e1StatusNoES',2),('t1e1StatusES',3)))
_T1e1ESStatus_Type.__name__=_C
_T1e1ESStatus_Object=MibTableColumn
t1e1ESStatus=_T1e1ESStatus_Object((1,3,6,1,4,1,321,100,2,3,2,1,6),_T1e1ESStatus_Type())
t1e1ESStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1ESStatus.setStatus(_A)
_T1e1ESCount_Type=Integer32
_T1e1ESCount_Object=MibTableColumn
t1e1ESCount=_T1e1ESCount_Object((1,3,6,1,4,1,321,100,2,3,2,1,7),_T1e1ESCount_Type())
t1e1ESCount.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1ESCount.setStatus(_A)
_T1e1ESThreshold_Type=Integer32
_T1e1ESThreshold_Object=MibTableColumn
t1e1ESThreshold=_T1e1ESThreshold_Object((1,3,6,1,4,1,321,100,2,3,2,1,8),_T1e1ESThreshold_Type())
t1e1ESThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1ESThreshold.setStatus(_A)
class _T1e1ESAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1ESAlarmOther',1),('t1e1ESAlarmNone',2),('t1e1ESAlarmThresholdExceeded',3)))
_T1e1ESAlarm_Type.__name__=_C
_T1e1ESAlarm_Object=MibTableColumn
t1e1ESAlarm=_T1e1ESAlarm_Object((1,3,6,1,4,1,321,100,2,3,2,1,9),_T1e1ESAlarm_Type())
t1e1ESAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1ESAlarm.setStatus(_A)
class _T1e1SESStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('t1e1StatusNoSES',2),('t1e1StatusSES',3)))
_T1e1SESStatus_Type.__name__=_C
_T1e1SESStatus_Object=MibTableColumn
t1e1SESStatus=_T1e1SESStatus_Object((1,3,6,1,4,1,321,100,2,3,2,1,10),_T1e1SESStatus_Type())
t1e1SESStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1SESStatus.setStatus(_A)
_T1e1SESCount_Type=Integer32
_T1e1SESCount_Object=MibTableColumn
t1e1SESCount=_T1e1SESCount_Object((1,3,6,1,4,1,321,100,2,3,2,1,11),_T1e1SESCount_Type())
t1e1SESCount.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1SESCount.setStatus(_A)
_T1e1SESThreshold_Type=Integer32
_T1e1SESThreshold_Object=MibTableColumn
t1e1SESThreshold=_T1e1SESThreshold_Object((1,3,6,1,4,1,321,100,2,3,2,1,12),_T1e1SESThreshold_Type())
t1e1SESThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1SESThreshold.setStatus(_A)
class _T1e1SESAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1SESAlarmOther',1),('t1e1SESAlarmNone',2),('t1e1SESAlarmThresholdExceeded',3)))
_T1e1SESAlarm_Type.__name__=_C
_T1e1SESAlarm_Object=MibTableColumn
t1e1SESAlarm=_T1e1SESAlarm_Object((1,3,6,1,4,1,321,100,2,3,2,1,13),_T1e1SESAlarm_Type())
t1e1SESAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1SESAlarm.setStatus(_A)
class _T1e1LOSSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('t1e1StatusNoLOSS',2),('t1e1StatusLOSS',3)))
_T1e1LOSSStatus_Type.__name__=_C
_T1e1LOSSStatus_Object=MibTableColumn
t1e1LOSSStatus=_T1e1LOSSStatus_Object((1,3,6,1,4,1,321,100,2,3,2,1,14),_T1e1LOSSStatus_Type())
t1e1LOSSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1LOSSStatus.setStatus(_A)
_T1e1LOSSCount_Type=Integer32
_T1e1LOSSCount_Object=MibTableColumn
t1e1LOSSCount=_T1e1LOSSCount_Object((1,3,6,1,4,1,321,100,2,3,2,1,15),_T1e1LOSSCount_Type())
t1e1LOSSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1LOSSCount.setStatus(_A)
_T1e1LOSSThreshold_Type=Integer32
_T1e1LOSSThreshold_Object=MibTableColumn
t1e1LOSSThreshold=_T1e1LOSSThreshold_Object((1,3,6,1,4,1,321,100,2,3,2,1,16),_T1e1LOSSThreshold_Type())
t1e1LOSSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1LOSSThreshold.setStatus(_A)
class _T1e1LOSSAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1LOSSAlarmOther',1),('t1e1LOSSAlarmNone',2),('t1e1LOSSAlarmThresholdExceeded',3)))
_T1e1LOSSAlarm_Type.__name__=_C
_T1e1LOSSAlarm_Object=MibTableColumn
t1e1LOSSAlarm=_T1e1LOSSAlarm_Object((1,3,6,1,4,1,321,100,2,3,2,1,17),_T1e1LOSSAlarm_Type())
t1e1LOSSAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1LOSSAlarm.setStatus(_A)
class _T1e1UASStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('t1e1StatusNoUAS',2),('t1e1StatusUAS',3)))
_T1e1UASStatus_Type.__name__=_C
_T1e1UASStatus_Object=MibTableColumn
t1e1UASStatus=_T1e1UASStatus_Object((1,3,6,1,4,1,321,100,2,3,2,1,18),_T1e1UASStatus_Type())
t1e1UASStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1UASStatus.setStatus(_A)
_T1e1UASCount_Type=Integer32
_T1e1UASCount_Object=MibTableColumn
t1e1UASCount=_T1e1UASCount_Object((1,3,6,1,4,1,321,100,2,3,2,1,19),_T1e1UASCount_Type())
t1e1UASCount.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1UASCount.setStatus(_A)
_T1e1UASThreshold_Type=Integer32
_T1e1UASThreshold_Object=MibTableColumn
t1e1UASThreshold=_T1e1UASThreshold_Object((1,3,6,1,4,1,321,100,2,3,2,1,20),_T1e1UASThreshold_Type())
t1e1UASThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1UASThreshold.setStatus(_A)
class _T1e1UASAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1UASAlarmOther',1),('t1e1UASAlarmNone',2),('t1e1UASAlarmThresholdExceeded',3)))
_T1e1UASAlarm_Type.__name__=_C
_T1e1UASAlarm_Object=MibTableColumn
t1e1UASAlarm=_T1e1UASAlarm_Object((1,3,6,1,4,1,321,100,2,3,2,1,21),_T1e1UASAlarm_Type())
t1e1UASAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1UASAlarm.setStatus(_A)
class _T1e1CSSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('t1e1StatusNoCSS',2),('t1e1StatusCSS',3)))
_T1e1CSSStatus_Type.__name__=_C
_T1e1CSSStatus_Object=MibTableColumn
t1e1CSSStatus=_T1e1CSSStatus_Object((1,3,6,1,4,1,321,100,2,3,2,1,22),_T1e1CSSStatus_Type())
t1e1CSSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1CSSStatus.setStatus(_A)
_T1e1CSSCount_Type=Integer32
_T1e1CSSCount_Object=MibTableColumn
t1e1CSSCount=_T1e1CSSCount_Object((1,3,6,1,4,1,321,100,2,3,2,1,23),_T1e1CSSCount_Type())
t1e1CSSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1CSSCount.setStatus(_A)
_T1e1CSSThreshold_Type=Integer32
_T1e1CSSThreshold_Object=MibTableColumn
t1e1CSSThreshold=_T1e1CSSThreshold_Object((1,3,6,1,4,1,321,100,2,3,2,1,24),_T1e1CSSThreshold_Type())
t1e1CSSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1CSSThreshold.setStatus(_A)
class _T1e1CSSAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1CSSAlarmOther',1),('t1e1CSSAlarmNone',2),('t1e1CSSAlarmThresholdExceeded',3)))
_T1e1CSSAlarm_Type.__name__=_C
_T1e1CSSAlarm_Object=MibTableColumn
t1e1CSSAlarm=_T1e1CSSAlarm_Object((1,3,6,1,4,1,321,100,2,3,2,1,25),_T1e1CSSAlarm_Type())
t1e1CSSAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1CSSAlarm.setStatus(_A)
class _T1e1BPVSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('t1e1StatusNoBPVS',2),('t1e1StatusBPVS',3)))
_T1e1BPVSStatus_Type.__name__=_C
_T1e1BPVSStatus_Object=MibTableColumn
t1e1BPVSStatus=_T1e1BPVSStatus_Object((1,3,6,1,4,1,321,100,2,3,2,1,26),_T1e1BPVSStatus_Type())
t1e1BPVSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1BPVSStatus.setStatus(_A)
_T1e1BPVSCount_Type=Integer32
_T1e1BPVSCount_Object=MibTableColumn
t1e1BPVSCount=_T1e1BPVSCount_Object((1,3,6,1,4,1,321,100,2,3,2,1,27),_T1e1BPVSCount_Type())
t1e1BPVSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1BPVSCount.setStatus(_A)
_T1e1BPVSThreshold_Type=Integer32
_T1e1BPVSThreshold_Object=MibTableColumn
t1e1BPVSThreshold=_T1e1BPVSThreshold_Object((1,3,6,1,4,1,321,100,2,3,2,1,28),_T1e1BPVSThreshold_Type())
t1e1BPVSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1BPVSThreshold.setStatus(_A)
class _T1e1BPVSAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1BPVSAlarmOther',1),('t1e1BPVSAlarmNone',2),('t1e1BPVSAlarmThresholdExceeded',3)))
_T1e1BPVSAlarm_Type.__name__=_C
_T1e1BPVSAlarm_Object=MibTableColumn
t1e1BPVSAlarm=_T1e1BPVSAlarm_Object((1,3,6,1,4,1,321,100,2,3,2,1,29),_T1e1BPVSAlarm_Type())
t1e1BPVSAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1BPVSAlarm.setStatus(_A)
class _T1e1OOFSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('t1e1StatusNoOOF',2),('t1e1StatusOOF',3)))
_T1e1OOFSStatus_Type.__name__=_C
_T1e1OOFSStatus_Object=MibTableColumn
t1e1OOFSStatus=_T1e1OOFSStatus_Object((1,3,6,1,4,1,321,100,2,3,2,1,30),_T1e1OOFSStatus_Type())
t1e1OOFSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1OOFSStatus.setStatus(_A)
_T1e1OOFSCount_Type=Integer32
_T1e1OOFSCount_Object=MibTableColumn
t1e1OOFSCount=_T1e1OOFSCount_Object((1,3,6,1,4,1,321,100,2,3,2,1,31),_T1e1OOFSCount_Type())
t1e1OOFSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1OOFSCount.setStatus(_A)
_T1e1OOFSThreshold_Type=Integer32
_T1e1OOFSThreshold_Object=MibTableColumn
t1e1OOFSThreshold=_T1e1OOFSThreshold_Object((1,3,6,1,4,1,321,100,2,3,2,1,32),_T1e1OOFSThreshold_Type())
t1e1OOFSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1OOFSThreshold.setStatus(_A)
class _T1e1OOFSAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1OOFSAlarmOther',1),('t1e1OOFSAlarmNone',2),('t1e1OOFSAlarmExists',3)))
_T1e1OOFSAlarm_Type.__name__=_C
_T1e1OOFSAlarm_Object=MibTableColumn
t1e1OOFSAlarm=_T1e1OOFSAlarm_Object((1,3,6,1,4,1,321,100,2,3,2,1,33),_T1e1OOFSAlarm_Type())
t1e1OOFSAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1OOFSAlarm.setStatus(_A)
class _T1e1AISStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('t1e1StatusNoAIS',2),('t1e1StatusAIS',3)))
_T1e1AISStatus_Type.__name__=_C
_T1e1AISStatus_Object=MibTableColumn
t1e1AISStatus=_T1e1AISStatus_Object((1,3,6,1,4,1,321,100,2,3,2,1,34),_T1e1AISStatus_Type())
t1e1AISStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1AISStatus.setStatus(_A)
_T1e1AISCount_Type=Integer32
_T1e1AISCount_Object=MibTableColumn
t1e1AISCount=_T1e1AISCount_Object((1,3,6,1,4,1,321,100,2,3,2,1,35),_T1e1AISCount_Type())
t1e1AISCount.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1AISCount.setStatus(_A)
_T1e1AISThreshold_Type=Integer32
_T1e1AISThreshold_Object=MibTableColumn
t1e1AISThreshold=_T1e1AISThreshold_Object((1,3,6,1,4,1,321,100,2,3,2,1,36),_T1e1AISThreshold_Type())
t1e1AISThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1AISThreshold.setStatus(_A)
class _T1e1AISAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1AISAlarmOther',1),('t1e1AISAlarmNone',2),('t1e1AISAlarmExists',3)))
_T1e1AISAlarm_Type.__name__=_C
_T1e1AISAlarm_Object=MibTableColumn
t1e1AISAlarm=_T1e1AISAlarm_Object((1,3,6,1,4,1,321,100,2,3,2,1,37),_T1e1AISAlarm_Type())
t1e1AISAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1AISAlarm.setStatus(_A)
class _T1e1RASStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1RASStatusOther',1),('t1e1RASStatusNoRAS',2),('t1e1RASStatusRAS',3)))
_T1e1RASStatus_Type.__name__=_C
_T1e1RASStatus_Object=MibTableColumn
t1e1RASStatus=_T1e1RASStatus_Object((1,3,6,1,4,1,321,100,2,3,2,1,38),_T1e1RASStatus_Type())
t1e1RASStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1RASStatus.setStatus(_A)
_T1e1RASCount_Type=Integer32
_T1e1RASCount_Object=MibTableColumn
t1e1RASCount=_T1e1RASCount_Object((1,3,6,1,4,1,321,100,2,3,2,1,39),_T1e1RASCount_Type())
t1e1RASCount.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1RASCount.setStatus(_A)
_T1e1RASThreshold_Type=Integer32
_T1e1RASThreshold_Object=MibTableColumn
t1e1RASThreshold=_T1e1RASThreshold_Object((1,3,6,1,4,1,321,100,2,3,2,1,40),_T1e1RASThreshold_Type())
t1e1RASThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1RASThreshold.setStatus(_A)
class _T1e1RASAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t1e1RASAlarmOther',1),('t1e1RASAlarmNone',2),('t1e1RASAlarmExists',3)))
_T1e1RASAlarm_Type.__name__=_C
_T1e1RASAlarm_Object=MibTableColumn
t1e1RASAlarm=_T1e1RASAlarm_Object((1,3,6,1,4,1,321,100,2,3,2,1,41),_T1e1RASAlarm_Type())
t1e1RASAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:t1e1RASAlarm.setStatus(_A)
_T1e1AlarmResetTimer_Type=Integer32
_T1e1AlarmResetTimer_Object=MibTableColumn
t1e1AlarmResetTimer=_T1e1AlarmResetTimer_Object((1,3,6,1,4,1,321,100,2,3,2,1,42),_T1e1AlarmResetTimer_Type())
t1e1AlarmResetTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1AlarmResetTimer.setStatus(_A)
class _T1e1AlarmReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('t1e1AlarmResetOther',1),('t1e1AlarmResetClearAlarms',2)))
_T1e1AlarmReset_Type.__name__=_C
_T1e1AlarmReset_Object=MibTableColumn
t1e1AlarmReset=_T1e1AlarmReset_Object((1,3,6,1,4,1,321,100,2,3,2,1,43),_T1e1AlarmReset_Type())
t1e1AlarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:t1e1AlarmReset.setStatus(_A)
_DdsNet_ObjectIdentity=ObjectIdentity
ddsNet=_DdsNet_ObjectIdentity((1,3,6,1,4,1,321,100,2,4))
_DdsNetConfigTable_Object=MibTable
ddsNetConfigTable=_DdsNetConfigTable_Object((1,3,6,1,4,1,321,100,2,4,1))
if mibBuilder.loadTexts:ddsNetConfigTable.setStatus(_A)
_DdsNetConfigTableEntry_Object=MibTableRow
ddsNetConfigTableEntry=_DdsNetConfigTableEntry_Object((1,3,6,1,4,1,321,100,2,4,1,1))
ddsNetConfigTableEntry.setIndexNames((0,_E,_p),(0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:ddsNetConfigTableEntry.setStatus(_A)
_DdsNetConfigNearIndex_Type=Integer32
_DdsNetConfigNearIndex_Object=MibTableColumn
ddsNetConfigNearIndex=_DdsNetConfigNearIndex_Object((1,3,6,1,4,1,321,100,2,4,1,1,1),_DdsNetConfigNearIndex_Type())
ddsNetConfigNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetConfigNearIndex.setStatus(_A)
_DdsNetConfigFarIndex_Type=Integer32
_DdsNetConfigFarIndex_Object=MibTableColumn
ddsNetConfigFarIndex=_DdsNetConfigFarIndex_Object((1,3,6,1,4,1,321,100,2,4,1,1,2),_DdsNetConfigFarIndex_Type())
ddsNetConfigFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetConfigFarIndex.setStatus(_A)
_DdsNetConfigIndex_Type=Integer32
_DdsNetConfigIndex_Object=MibTableColumn
ddsNetConfigIndex=_DdsNetConfigIndex_Object((1,3,6,1,4,1,321,100,2,4,1,1,3),_DdsNetConfigIndex_Type())
ddsNetConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetConfigIndex.setStatus(_A)
class _DdsNetDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DdsNetDescription_Type.__name__=_F
_DdsNetDescription_Object=MibTableColumn
ddsNetDescription=_DdsNetDescription_Object((1,3,6,1,4,1,321,100,2,4,1,1,4),_DdsNetDescription_Type())
ddsNetDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetDescription.setStatus(_A)
class _DdsNetRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ddsNetRate2400',1),('ddsNetRate4800',2),('ddsNetRate9600',3),('ddsNetRate19200',4),('ddsNetRate38400',5),('ddsNetRate56000',6),('ddsNetRate64000',7)))
_DdsNetRate_Type.__name__=_C
_DdsNetRate_Object=MibTableColumn
ddsNetRate=_DdsNetRate_Object((1,3,6,1,4,1,321,100,2,4,1,1,5),_DdsNetRate_Type())
ddsNetRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetRate.setStatus(_A)
class _DdsNetMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ddsNetModeNormal',1),('ddsNetModeProprietaryTXPI',2),('ddsNetMode64KClearChannel',3),('ddsNetMode64KCCProprietaryTXPII',4)))
_DdsNetMode_Type.__name__=_C
_DdsNetMode_Object=MibTableColumn
ddsNetMode=_DdsNetMode_Object((1,3,6,1,4,1,321,100,2,4,1,1,6),_DdsNetMode_Type())
ddsNetMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetMode.setStatus(_A)
class _DdsNetTimingSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ddsNetTimingNet',1),('ddsNetTimingInt',2),('ddsNetTimingDTE',3),('ddsNetTimingPort1',4),('ddsNetTimingPort2',5)))
_DdsNetTimingSource_Type.__name__=_C
_DdsNetTimingSource_Object=MibTableColumn
ddsNetTimingSource=_DdsNetTimingSource_Object((1,3,6,1,4,1,321,100,2,4,1,1,7),_DdsNetTimingSource_Type())
ddsNetTimingSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetTimingSource.setStatus(_A)
class _DdsNetRemComm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetRemCommEnabled',1),('ddsNetRemCommDisabled',2),('ddsNetRemCommNotAvailable',3)))
_DdsNetRemComm_Type.__name__=_C
_DdsNetRemComm_Object=MibTableColumn
ddsNetRemComm=_DdsNetRemComm_Object((1,3,6,1,4,1,321,100,2,4,1,1,8),_DdsNetRemComm_Type())
ddsNetRemComm.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetRemComm.setStatus(_A)
class _DdsNetCircuitAssur_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetCircuitAssurEnabled',1),('ddsNetCircuitAssurDisabled',2),('ddsNetCircuitAssurNotAvailable',3)))
_DdsNetCircuitAssur_Type.__name__=_C
_DdsNetCircuitAssur_Object=MibTableColumn
ddsNetCircuitAssur=_DdsNetCircuitAssur_Object((1,3,6,1,4,1,321,100,2,4,1,1,9),_DdsNetCircuitAssur_Type())
ddsNetCircuitAssur.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetCircuitAssur.setStatus(_A)
class _DdsNetAntiStrTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ddsNetAntiStrTimerOff',1),('ddsNetAntiStrTimer10',2),('ddsNetAntiStrTimer30',3),('ddsNetAntiStrTimer60',4)))
_DdsNetAntiStrTimer_Type.__name__=_C
_DdsNetAntiStrTimer_Object=MibTableColumn
ddsNetAntiStrTimer=_DdsNetAntiStrTimer_Object((1,3,6,1,4,1,321,100,2,4,1,1,10),_DdsNetAntiStrTimer_Type())
ddsNetAntiStrTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetAntiStrTimer.setStatus(_A)
_DdsNetAlarmTable_Object=MibTable
ddsNetAlarmTable=_DdsNetAlarmTable_Object((1,3,6,1,4,1,321,100,2,4,2))
if mibBuilder.loadTexts:ddsNetAlarmTable.setStatus(_A)
_DdsNetAlarmTableEntry_Object=MibTableRow
ddsNetAlarmTableEntry=_DdsNetAlarmTableEntry_Object((1,3,6,1,4,1,321,100,2,4,2,1))
ddsNetAlarmTableEntry.setIndexNames((0,_E,_s),(0,_E,_t),(0,_E,_u))
if mibBuilder.loadTexts:ddsNetAlarmTableEntry.setStatus(_A)
_DdsNetAlarmNearIndex_Type=Integer32
_DdsNetAlarmNearIndex_Object=MibTableColumn
ddsNetAlarmNearIndex=_DdsNetAlarmNearIndex_Object((1,3,6,1,4,1,321,100,2,4,2,1,1),_DdsNetAlarmNearIndex_Type())
ddsNetAlarmNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetAlarmNearIndex.setStatus(_A)
_DdsNetAlarmFarIndex_Type=Integer32
_DdsNetAlarmFarIndex_Object=MibTableColumn
ddsNetAlarmFarIndex=_DdsNetAlarmFarIndex_Object((1,3,6,1,4,1,321,100,2,4,2,1,2),_DdsNetAlarmFarIndex_Type())
ddsNetAlarmFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetAlarmFarIndex.setStatus(_A)
_DdsNetAlarmIndex_Type=Integer32
_DdsNetAlarmIndex_Object=MibTableColumn
ddsNetAlarmIndex=_DdsNetAlarmIndex_Object((1,3,6,1,4,1,321,100,2,4,2,1,3),_DdsNetAlarmIndex_Type())
ddsNetAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetAlarmIndex.setStatus(_A)
class _DdsNetStatusSummary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_DdsNetStatusSummary_Type.__name__=_F
_DdsNetStatusSummary_Object=MibTableColumn
ddsNetStatusSummary=_DdsNetStatusSummary_Object((1,3,6,1,4,1,321,100,2,4,2,1,4),_DdsNetStatusSummary_Type())
ddsNetStatusSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetStatusSummary.setStatus(_A)
class _DdsNetAlarmSummary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_DdsNetAlarmSummary_Type.__name__=_F
_DdsNetAlarmSummary_Object=MibTableColumn
ddsNetAlarmSummary=_DdsNetAlarmSummary_Object((1,3,6,1,4,1,321,100,2,4,2,1,5),_DdsNetAlarmSummary_Type())
ddsNetAlarmSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetAlarmSummary.setStatus(_A)
class _DdsNetLOSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetStatusLOSOther',1),('ddsNetStatusNoLOS',2),('ddsNetStatusLOS',3)))
_DdsNetLOSStatus_Type.__name__=_C
_DdsNetLOSStatus_Object=MibTableColumn
ddsNetLOSStatus=_DdsNetLOSStatus_Object((1,3,6,1,4,1,321,100,2,4,2,1,6),_DdsNetLOSStatus_Type())
ddsNetLOSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetLOSStatus.setStatus(_A)
_DdsNetLOSCount_Type=Integer32
_DdsNetLOSCount_Object=MibTableColumn
ddsNetLOSCount=_DdsNetLOSCount_Object((1,3,6,1,4,1,321,100,2,4,2,1,7),_DdsNetLOSCount_Type())
ddsNetLOSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetLOSCount.setStatus(_A)
class _DdsNetLOSThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('ddsNetLOSThresholdOther',1),('ddsNetLOSThresholdNone',2),('ddsNetLOSThreshold1',3),('ddsNetLOSThreshold2',4),('ddsNetLOSThreshold3',5),('ddsNetLOSThreshold4',6),('ddsNetLOSThreshold5',7),('ddsNetLOSThreshold10',8),('ddsNetLOSThreshold20',9),('ddsNetLOSThreshold30',10)))
_DdsNetLOSThreshold_Type.__name__=_C
_DdsNetLOSThreshold_Object=MibTableColumn
ddsNetLOSThreshold=_DdsNetLOSThreshold_Object((1,3,6,1,4,1,321,100,2,4,2,1,8),_DdsNetLOSThreshold_Type())
ddsNetLOSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetLOSThreshold.setStatus(_A)
class _DdsNetLOSAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetLOSAlarmOther',1),('ddsNetLOSAlarmNone',2),('ddsNetLOSAlarmThresholdExceeded',3)))
_DdsNetLOSAlarm_Type.__name__=_C
_DdsNetLOSAlarm_Object=MibTableColumn
ddsNetLOSAlarm=_DdsNetLOSAlarm_Object((1,3,6,1,4,1,321,100,2,4,2,1,9),_DdsNetLOSAlarm_Type())
ddsNetLOSAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetLOSAlarm.setStatus(_A)
class _DdsNetOOFStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetStatusOOFOther',1),('ddsNetStatusNoOOF',2),('ddsNetStatusOOF',3)))
_DdsNetOOFStatus_Type.__name__=_C
_DdsNetOOFStatus_Object=MibTableColumn
ddsNetOOFStatus=_DdsNetOOFStatus_Object((1,3,6,1,4,1,321,100,2,4,2,1,10),_DdsNetOOFStatus_Type())
ddsNetOOFStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetOOFStatus.setStatus(_A)
_DdsNetOOFCount_Type=Integer32
_DdsNetOOFCount_Object=MibTableColumn
ddsNetOOFCount=_DdsNetOOFCount_Object((1,3,6,1,4,1,321,100,2,4,2,1,11),_DdsNetOOFCount_Type())
ddsNetOOFCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetOOFCount.setStatus(_A)
class _DdsNetOOFThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('ddsNetOOFThresholdOther',1),('ddsNetOOFThresholdNone',2),('ddsNetOOFThreshold1',3),('ddsNetOOFThreshold2',4),('ddsNetOOFThreshold3',5),('ddsNetOOFThreshold4',6),('ddsNetOOFThreshold5',7),('ddsNetOOFThreshold10',8),('ddsNetOOFThreshold20',9),('ddsNetOOFThreshold30',10)))
_DdsNetOOFThreshold_Type.__name__=_C
_DdsNetOOFThreshold_Object=MibTableColumn
ddsNetOOFThreshold=_DdsNetOOFThreshold_Object((1,3,6,1,4,1,321,100,2,4,2,1,12),_DdsNetOOFThreshold_Type())
ddsNetOOFThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetOOFThreshold.setStatus(_A)
class _DdsNetOOFAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetOOFSAlarmOther',1),('ddsNetOOFSAlarmNone',2),('ddsNetOOFSAlarmThresholdExceeded',3)))
_DdsNetOOFAlarm_Type.__name__=_C
_DdsNetOOFAlarm_Object=MibTableColumn
ddsNetOOFAlarm=_DdsNetOOFAlarm_Object((1,3,6,1,4,1,321,100,2,4,2,1,13),_DdsNetOOFAlarm_Type())
ddsNetOOFAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetOOFAlarm.setStatus(_A)
class _DdsNetOOSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetStatusOOSOther',1),('ddsNetStatusNoOOS',2),('ddsNetStatusOOS',3)))
_DdsNetOOSStatus_Type.__name__=_C
_DdsNetOOSStatus_Object=MibTableColumn
ddsNetOOSStatus=_DdsNetOOSStatus_Object((1,3,6,1,4,1,321,100,2,4,2,1,14),_DdsNetOOSStatus_Type())
ddsNetOOSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetOOSStatus.setStatus(_A)
_DdsNetOOSCount_Type=Integer32
_DdsNetOOSCount_Object=MibTableColumn
ddsNetOOSCount=_DdsNetOOSCount_Object((1,3,6,1,4,1,321,100,2,4,2,1,15),_DdsNetOOSCount_Type())
ddsNetOOSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetOOSCount.setStatus(_A)
class _DdsNetOOSThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('ddsNetOOSThresholdOther',1),('ddsNetOOSThresholdNone',2),('ddsNetOOSThreshold1',3),('ddsNetOOSThreshold2',4),('ddsNetOOSThreshold3',5),('ddsNetOOSThreshold4',6),('ddsNetOOSThreshold5',7),('ddsNetOOSThreshold10',8),('ddsNetOOSThreshold20',9),('ddsNetOOSThreshold30',10)))
_DdsNetOOSThreshold_Type.__name__=_C
_DdsNetOOSThreshold_Object=MibTableColumn
ddsNetOOSThreshold=_DdsNetOOSThreshold_Object((1,3,6,1,4,1,321,100,2,4,2,1,16),_DdsNetOOSThreshold_Type())
ddsNetOOSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetOOSThreshold.setStatus(_A)
class _DdsNetOOSAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetOOSAlarmOther',1),('ddsNetOOSAlarmNone',2),('ddsNetOOSAlarmThresholdExceeded',3)))
_DdsNetOOSAlarm_Type.__name__=_C
_DdsNetOOSAlarm_Object=MibTableColumn
ddsNetOOSAlarm=_DdsNetOOSAlarm_Object((1,3,6,1,4,1,321,100,2,4,2,1,17),_DdsNetOOSAlarm_Type())
ddsNetOOSAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetOOSAlarm.setStatus(_A)
class _DdsNetFDLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetStatusFDLOther',1),('ddsNetStatusNoFDL',2),('ddsNetStatusFDL',3)))
_DdsNetFDLStatus_Type.__name__=_C
_DdsNetFDLStatus_Object=MibTableColumn
ddsNetFDLStatus=_DdsNetFDLStatus_Object((1,3,6,1,4,1,321,100,2,4,2,1,18),_DdsNetFDLStatus_Type())
ddsNetFDLStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetFDLStatus.setStatus(_A)
_DdsNetFDLCount_Type=Integer32
_DdsNetFDLCount_Object=MibTableColumn
ddsNetFDLCount=_DdsNetFDLCount_Object((1,3,6,1,4,1,321,100,2,4,2,1,19),_DdsNetFDLCount_Type())
ddsNetFDLCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetFDLCount.setStatus(_A)
class _DdsNetFDLThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('ddsNetFDLThresholdOther',1),('ddsNetFDLThresholdNone',2),('ddsNetFDLThreshold1',3),('ddsNetFDLThreshold2',4),('ddsNetFDLThreshold3',5),('ddsNetFDLThreshold4',6),('ddsNetFDLThreshold5',7),('ddsNetFDLThreshold10',8),('ddsNetFDLThreshold20',9),('ddsNetFDLThreshold30',10)))
_DdsNetFDLThreshold_Type.__name__=_C
_DdsNetFDLThreshold_Object=MibTableColumn
ddsNetFDLThreshold=_DdsNetFDLThreshold_Object((1,3,6,1,4,1,321,100,2,4,2,1,20),_DdsNetFDLThreshold_Type())
ddsNetFDLThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetFDLThreshold.setStatus(_A)
class _DdsNetFDLAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetFDLAlarmOther',1),('ddsNetFDLAlarmNone',2),('ddsNetFDLAlarmThresholdExceeded',3)))
_DdsNetFDLAlarm_Type.__name__=_C
_DdsNetFDLAlarm_Object=MibTableColumn
ddsNetFDLAlarm=_DdsNetFDLAlarm_Object((1,3,6,1,4,1,321,100,2,4,2,1,21),_DdsNetFDLAlarm_Type())
ddsNetFDLAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetFDLAlarm.setStatus(_A)
_DdsNetAlarmResetTimer_Type=Integer32
_DdsNetAlarmResetTimer_Object=MibTableColumn
ddsNetAlarmResetTimer=_DdsNetAlarmResetTimer_Object((1,3,6,1,4,1,321,100,2,4,2,1,22),_DdsNetAlarmResetTimer_Type())
ddsNetAlarmResetTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetAlarmResetTimer.setStatus(_A)
class _DdsNetAlarmReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ddsNetAlarmResetOther',1),('ddsNetAlarmResetClearAlarms',2)))
_DdsNetAlarmReset_Type.__name__=_C
_DdsNetAlarmReset_Object=MibTableColumn
ddsNetAlarmReset=_DdsNetAlarmReset_Object((1,3,6,1,4,1,321,100,2,4,2,1,23),_DdsNetAlarmReset_Type())
ddsNetAlarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetAlarmReset.setStatus(_A)
class _DdsNetBPVStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetStatusBPVOther',1),('ddsNetStatusNoBPV',2),('ddsNetStatusBPV',3)))
_DdsNetBPVStatus_Type.__name__=_C
_DdsNetBPVStatus_Object=MibTableColumn
ddsNetBPVStatus=_DdsNetBPVStatus_Object((1,3,6,1,4,1,321,100,2,4,2,1,24),_DdsNetBPVStatus_Type())
ddsNetBPVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetBPVStatus.setStatus(_A)
_DdsNetBPVCount_Type=Integer32
_DdsNetBPVCount_Object=MibTableColumn
ddsNetBPVCount=_DdsNetBPVCount_Object((1,3,6,1,4,1,321,100,2,4,2,1,25),_DdsNetBPVCount_Type())
ddsNetBPVCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetBPVCount.setStatus(_A)
class _DdsNetBPVThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('ddsNetBPVThresholdOther',1),('ddsNetBPVThresholdNone',2),('ddsNetBPVThreshold1',3),('ddsNetBPVThreshold2',4),('ddsNetBPVThreshold3',5),('ddsNetBPVThreshold4',6),('ddsNetBPVThreshold5',7),('ddsNetBPVThreshold10',8),('ddsNetBPVThreshold20',9),('ddsNetBPVThreshold30',10)))
_DdsNetBPVThreshold_Type.__name__=_C
_DdsNetBPVThreshold_Object=MibTableColumn
ddsNetBPVThreshold=_DdsNetBPVThreshold_Object((1,3,6,1,4,1,321,100,2,4,2,1,26),_DdsNetBPVThreshold_Type())
ddsNetBPVThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsNetBPVThreshold.setStatus(_A)
class _DdsNetBPVAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNetBPVAlarmOther',1),('ddsNetBPVAlarmNone',2),('ddsNetBPVAlarmThresholdExceeded',3)))
_DdsNetBPVAlarm_Type.__name__=_C
_DdsNetBPVAlarm_Object=MibTableColumn
ddsNetBPVAlarm=_DdsNetBPVAlarm_Object((1,3,6,1,4,1,321,100,2,4,2,1,27),_DdsNetBPVAlarm_Type())
ddsNetBPVAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsNetBPVAlarm.setStatus(_A)
_SerialDte_ObjectIdentity=ObjectIdentity
serialDte=_SerialDte_ObjectIdentity((1,3,6,1,4,1,321,100,2,5))
_SerialDteConfigTable_Object=MibTable
serialDteConfigTable=_SerialDteConfigTable_Object((1,3,6,1,4,1,321,100,2,5,1))
if mibBuilder.loadTexts:serialDteConfigTable.setStatus(_A)
_SerialDteConfigTableEntry_Object=MibTableRow
serialDteConfigTableEntry=_SerialDteConfigTableEntry_Object((1,3,6,1,4,1,321,100,2,5,1,1))
serialDteConfigTableEntry.setIndexNames((0,_E,_v),(0,_E,_w),(0,_E,_x))
if mibBuilder.loadTexts:serialDteConfigTableEntry.setStatus(_A)
_SerialDteConfigNearIndex_Type=Integer32
_SerialDteConfigNearIndex_Object=MibTableColumn
serialDteConfigNearIndex=_SerialDteConfigNearIndex_Object((1,3,6,1,4,1,321,100,2,5,1,1,1),_SerialDteConfigNearIndex_Type())
serialDteConfigNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteConfigNearIndex.setStatus(_A)
_SerialDteConfigFarIndex_Type=Integer32
_SerialDteConfigFarIndex_Object=MibTableColumn
serialDteConfigFarIndex=_SerialDteConfigFarIndex_Object((1,3,6,1,4,1,321,100,2,5,1,1,2),_SerialDteConfigFarIndex_Type())
serialDteConfigFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteConfigFarIndex.setStatus(_A)
_SerialDteConfigIndex_Type=Integer32
_SerialDteConfigIndex_Object=MibTableColumn
serialDteConfigIndex=_SerialDteConfigIndex_Object((1,3,6,1,4,1,321,100,2,5,1,1,3),_SerialDteConfigIndex_Type())
serialDteConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteConfigIndex.setStatus(_A)
class _SerialDteDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SerialDteDescription_Type.__name__=_F
_SerialDteDescription_Object=MibTableColumn
serialDteDescription=_SerialDteDescription_Object((1,3,6,1,4,1,321,100,2,5,1,1,4),_SerialDteDescription_Type())
serialDteDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteDescription.setStatus(_A)
class _SerialDteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('serialDteTypeOther',1),('serialDteTypeV35',2),('serialDteTypeRS232',3),('serialDteTypeEIA530',4),('serialDteTypeX21',5),('serialDteTypeV36',6),('serialDteTypeEIA530A',7)))
_SerialDteType_Type.__name__=_C
_SerialDteType_Object=MibTableColumn
serialDteType=_SerialDteType_Object((1,3,6,1,4,1,321,100,2,5,1,1,5),_SerialDteType_Type())
serialDteType.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteType.setStatus(_A)
class _SerialDteRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83)));namedValues=NamedValues(*(('serialDteRateOther',1),('serialDteRate2400',2),('serialDteRate4800',3),('serialDteRate9600',4),('serialDteRate19200',5),('serialDteRate38400',6),('serialDteRate52000',7),('serialDteRate56000',8),('serialDteRate57600',9),('serialDteRate60000',10),('serialDteRate64000',11),('serialDteRate112000',12),('serialDteRate128000',13),('serialDteRate168000',14),('serialDteRate192000',15),('serialDteRate224000',16),('serialDteRate256000',17),('serialDteRate280000',18),('serialDteRate320000',19),('serialDteRate336000',20),('serialDteRate384000',21),('serialDteRate392000',22),('serialDteRate448000',23),('serialDteRate504000',24),('serialDteRate512000',25),('serialDteRate560000',26),('serialDteRate576000',27),('serialDteRate616000',28),('serialDteRate640000',29),('serialDteRate672000',30),('serialDteRate704000',31),('serialDteRate728000',32),('serialDteRate768000',33),('serialDteRate784000',34),('serialDteRate832000',35),('serialDteRate840000',36),('serialDteRate896000',37),('serialDteRate952000',38),('serialDteRate960000',39),('serialDteRate1008000',40),('serialDteRate1024000',41),('serialDteRate1064000',42),('serialDteRate1088000',43),('serialDteRate1120000',44),('serialDteRate1152000',45),('serialDteRate1176000',46),('serialDteRate1216000',47),('serialDteRate1232000',48),('serialDteRate1280000',49),('serialDteRate1288000',50),('serialDteRate1344000',51),('serialDteRate1400000',52),('serialDteRate1408000',53),('serialDteRate1456000',54),('serialDteRate1472000',55),('serialDteRate1512000',56),('serialDteRate1536000',57),('serialDteRate1568000',58),('serialDteRate1600000',59),('serialDteRate1624000',60),('serialDteRate1664000',61),('serialDteRate1680000',62),('serialDteRate1728000',63),('serialDteRate1736000',64),('serialDteRate1792000',65),('serialDteRate1856000',66),('serialDteRate1920000',67),('serialDteRate1984000',68),('serialDteRate2048000',69),('serialDteRate1200',70),('serialDteRate14400',71),('serialDteRate28800',72),('serialDteRate48000',73),('serialDteRate31200',74),('serialDteRate115200',75),('serialDteRate2112000',76),('serialDteRate2176000',77),('serialDteRate2240000',78),('serialDteRate2304000',79),('serialDteRate300',80),('serialDteRate600',81),('serialDteRate3072000',82),('serialDteRate4096000',83)))
_SerialDteRate_Type.__name__=_C
_SerialDteRate_Object=MibTableColumn
serialDteRate=_SerialDteRate_Object((1,3,6,1,4,1,321,100,2,5,1,1,6),_SerialDteRate_Type())
serialDteRate.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteRate.setStatus(_A)
class _SerialDteInvertData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteInvertDataOther',1),('serialDteInvertDataDisabled',2),('serialDteInvertDataEnabled',3)))
_SerialDteInvertData_Type.__name__=_C
_SerialDteInvertData_Object=MibTableColumn
serialDteInvertData=_SerialDteInvertData_Object((1,3,6,1,4,1,321,100,2,5,1,1,7),_SerialDteInvertData_Type())
serialDteInvertData.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteInvertData.setStatus(_A)
class _SerialDteFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('serialDteFormatOther',1),('serialDteFormatSync',2),('serialDteFormatAsync',3),('serialDteFormatNotAvail',4)))
_SerialDteFormat_Type.__name__=_C
_SerialDteFormat_Object=MibTableColumn
serialDteFormat=_SerialDteFormat_Object((1,3,6,1,4,1,321,100,2,5,1,1,8),_SerialDteFormat_Type())
serialDteFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteFormat.setStatus(_A)
class _SerialDteParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('serialDteParityOther',1),('serialDteParityNone',2),('serialDteParityOdd',3),('serialDteParityEven',4),('serialDteParityMark',5),('serialDteParitySpace',6),('serialDteParityNotAvail',7)))
_SerialDteParity_Type.__name__=_C
_SerialDteParity_Object=MibTableColumn
serialDteParity=_SerialDteParity_Object((1,3,6,1,4,1,321,100,2,5,1,1,9),_SerialDteParity_Type())
serialDteParity.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteParity.setStatus(_A)
class _SerialDteStopBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('serialDteStopBitOther',1),('serialDteStopBit1',2),('serialDteStopBit2',3),('serialDteStopBitNotAvail',4)))
_SerialDteStopBit_Type.__name__=_C
_SerialDteStopBit_Object=MibTableColumn
serialDteStopBit=_SerialDteStopBit_Object((1,3,6,1,4,1,321,100,2,5,1,1,10),_SerialDteStopBit_Type())
serialDteStopBit.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteStopBit.setStatus(_A)
class _SerialDteMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('serialDteModeOther',1),('serialDteModeDDSI',2),('serialDteModeDDSII',3),('serialDteModeTxpINormal',4),('serialDteModeTxpITDM',5),('serialDteModeTxpIINormal',6),('serialDteModeTxpIITDM',7)))
_SerialDteMode_Type.__name__=_C
_SerialDteMode_Object=MibTableColumn
serialDteMode=_SerialDteMode_Object((1,3,6,1,4,1,321,100,2,5,1,1,11),_SerialDteMode_Type())
serialDteMode.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteMode.setStatus(_A)
class _SerialDteDSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('serialDteDSROther',1),('serialDteDSRTestOff',2),('serialDteDSRForcedOn',3),('serialDteDSRForcedOff',4),('serialDteDSRInternal',5)))
_SerialDteDSR_Type.__name__=_C
_SerialDteDSR_Object=MibTableColumn
serialDteDSR=_SerialDteDSR_Object((1,3,6,1,4,1,321,100,2,5,1,1,12),_SerialDteDSR_Type())
serialDteDSR.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteDSR.setStatus(_A)
class _SerialDteDCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('serialDteDCDOther',1),('serialDteDCDIdleOff',2),('serialDteDCDForcedOn',3),('serialDteDCDForcedOff',4),('serialDteDCDInternal',5),('serialDteDCDFarRTS',6)))
_SerialDteDCD_Type.__name__=_C
_SerialDteDCD_Object=MibTableColumn
serialDteDCD=_SerialDteDCD_Object((1,3,6,1,4,1,321,100,2,5,1,1,13),_SerialDteDCD_Type())
serialDteDCD.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteDCD.setStatus(_A)
class _SerialDteRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('serialDteRTSOther',1),('serialDteRTSNormal',2),('serialDteRTSForcedOn',3),('serialDteRTSExternal',4)))
_SerialDteRTS_Type.__name__=_C
_SerialDteRTS_Object=MibTableColumn
serialDteRTS=_SerialDteRTS_Object((1,3,6,1,4,1,321,100,2,5,1,1,14),_SerialDteRTS_Type())
serialDteRTS.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteRTS.setStatus(_A)
class _SerialDteRTSDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteRTSDelayOther',1),('serialDteRTSDelayNormal',2),('serialDteRTSDelayLong',3)))
_SerialDteRTSDelay_Type.__name__=_C
_SerialDteRTSDelay_Object=MibTableColumn
serialDteRTSDelay=_SerialDteRTSDelay_Object((1,3,6,1,4,1,321,100,2,5,1,1,15),_SerialDteRTSDelay_Type())
serialDteRTSDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteRTSDelay.setStatus(_A)
class _SerialDteDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteDTROther',1),('serialDteDTRFalse',2),('serialDteDTRTrue',3)))
_SerialDteDTR_Type.__name__=_C
_SerialDteDTR_Object=MibTableColumn
serialDteDTR=_SerialDteDTR_Object((1,3,6,1,4,1,321,100,2,5,1,1,16),_SerialDteDTR_Type())
serialDteDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteDTR.setStatus(_A)
class _SerialDteCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('serialDteCTSOther',1),('serialDteCTSForceTrue',2),('serialDteCTSForceFalse',3),('serialDteCTSInternal',4)))
_SerialDteCTS_Type.__name__=_C
_SerialDteCTS_Object=MibTableColumn
serialDteCTS=_SerialDteCTS_Object((1,3,6,1,4,1,321,100,2,5,1,1,17),_SerialDteCTS_Type())
serialDteCTS.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteCTS.setStatus(_A)
class _SerialDteV54_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteV54Other',1),('serialDteV54Disable',2),('serialDteV54Enable',3)))
_SerialDteV54_Type.__name__=_C
_SerialDteV54_Object=MibTableColumn
serialDteV54=_SerialDteV54_Object((1,3,6,1,4,1,321,100,2,5,1,1,18),_SerialDteV54_Type())
serialDteV54.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteV54.setStatus(_A)
class _SerialDteLL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteLLOther',1),('serialDteLLDisable',2),('serialDteLLEnable',3)))
_SerialDteLL_Type.__name__=_C
_SerialDteLL_Object=MibTableColumn
serialDteLL=_SerialDteLL_Object((1,3,6,1,4,1,321,100,2,5,1,1,19),_SerialDteLL_Type())
serialDteLL.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteLL.setStatus(_A)
class _SerialDteRL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteRLOther',1),('serialDteRLDisable',2),('serialDteRLEnable',3)))
_SerialDteRL_Type.__name__=_C
_SerialDteRL_Object=MibTableColumn
serialDteRL=_SerialDteRL_Object((1,3,6,1,4,1,321,100,2,5,1,1,20),_SerialDteRL_Type())
serialDteRL.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteRL.setStatus(_A)
_SerialDteStartChannel_Type=Integer32
_SerialDteStartChannel_Object=MibTableColumn
serialDteStartChannel=_SerialDteStartChannel_Object((1,3,6,1,4,1,321,100,2,5,1,1,21),_SerialDteStartChannel_Type())
serialDteStartChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteStartChannel.setStatus(_A)
_SerialDteNumberOfChannels_Type=Integer32
_SerialDteNumberOfChannels_Object=MibTableColumn
serialDteNumberOfChannels=_SerialDteNumberOfChannels_Object((1,3,6,1,4,1,321,100,2,5,1,1,22),_SerialDteNumberOfChannels_Type())
serialDteNumberOfChannels.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteNumberOfChannels.setStatus(_A)
class _SerialDteTxClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('serialDteTxClockOther',1),('serialDteTxClockInternal',2),('serialDteTxClockExternal',3),('serialDteTxClockOversample',4)))
_SerialDteTxClock_Type.__name__=_C
_SerialDteTxClock_Object=MibTableColumn
serialDteTxClock=_SerialDteTxClock_Object((1,3,6,1,4,1,321,100,2,5,1,1,23),_SerialDteTxClock_Type())
serialDteTxClock.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteTxClock.setStatus(_A)
class _SerialDteBundle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('contiguous',2),('alternate',3)))
_SerialDteBundle_Type.__name__=_C
_SerialDteBundle_Object=MibTableColumn
serialDteBundle=_SerialDteBundle_Object((1,3,6,1,4,1,321,100,2,5,1,1,24),_SerialDteBundle_Type())
serialDteBundle.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteBundle.setStatus(_A)
class _SerialDteChannelRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('nx56k',2),('nx64k',3)))
_SerialDteChannelRate_Type.__name__=_C
_SerialDteChannelRate_Object=MibTableColumn
serialDteChannelRate=_SerialDteChannelRate_Object((1,3,6,1,4,1,321,100,2,5,1,1,25),_SerialDteChannelRate_Type())
serialDteChannelRate.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteChannelRate.setStatus(_A)
class _SerialDteInvertClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_J,3)))
_SerialDteInvertClock_Type.__name__=_C
_SerialDteInvertClock_Object=MibTableColumn
serialDteInvertClock=_SerialDteInvertClock_Object((1,3,6,1,4,1,321,100,2,5,1,1,26),_SerialDteInvertClock_Type())
serialDteInvertClock.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteInvertClock.setStatus(_A)
class _SerialDteCharSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('five',2),('six',3),('seven',4),('eight',5)))
_SerialDteCharSize_Type.__name__=_C
_SerialDteCharSize_Object=MibTableColumn
serialDteCharSize=_SerialDteCharSize_Object((1,3,6,1,4,1,321,100,2,5,1,1,27),_SerialDteCharSize_Type())
serialDteCharSize.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteCharSize.setStatus(_A)
class _SerialDteFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('none',2),('xonXoff',3),('rtsCts',4)))
_SerialDteFlowControl_Type.__name__=_C
_SerialDteFlowControl_Object=MibTableColumn
serialDteFlowControl=_SerialDteFlowControl_Object((1,3,6,1,4,1,321,100,2,5,1,1,28),_SerialDteFlowControl_Type())
serialDteFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteFlowControl.setStatus(_A)
class _SerialDtePinStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SerialDtePinStatus_Type.__name__=_F
_SerialDtePinStatus_Object=MibTableColumn
serialDtePinStatus=_SerialDtePinStatus_Object((1,3,6,1,4,1,321,100,2,5,1,1,29),_SerialDtePinStatus_Type())
serialDtePinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDtePinStatus.setStatus(_A)
class _SerialDteInInvertClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_J,3)))
_SerialDteInInvertClock_Type.__name__=_C
_SerialDteInInvertClock_Object=MibTableColumn
serialDteInInvertClock=_SerialDteInInvertClock_Object((1,3,6,1,4,1,321,100,2,5,1,1,30),_SerialDteInInvertClock_Type())
serialDteInInvertClock.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteInInvertClock.setStatus(_A)
_SerialDteAlarmTable_Object=MibTable
serialDteAlarmTable=_SerialDteAlarmTable_Object((1,3,6,1,4,1,321,100,2,5,2))
if mibBuilder.loadTexts:serialDteAlarmTable.setStatus(_A)
_SerialDteAlarmTableEntry_Object=MibTableRow
serialDteAlarmTableEntry=_SerialDteAlarmTableEntry_Object((1,3,6,1,4,1,321,100,2,5,2,1))
serialDteAlarmTableEntry.setIndexNames((0,_E,_y),(0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:serialDteAlarmTableEntry.setStatus(_A)
_SerialDteAlarmNearIndex_Type=Integer32
_SerialDteAlarmNearIndex_Object=MibTableColumn
serialDteAlarmNearIndex=_SerialDteAlarmNearIndex_Object((1,3,6,1,4,1,321,100,2,5,2,1,1),_SerialDteAlarmNearIndex_Type())
serialDteAlarmNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteAlarmNearIndex.setStatus(_A)
_SerialDteAlarmFarIndex_Type=Integer32
_SerialDteAlarmFarIndex_Object=MibTableColumn
serialDteAlarmFarIndex=_SerialDteAlarmFarIndex_Object((1,3,6,1,4,1,321,100,2,5,2,1,2),_SerialDteAlarmFarIndex_Type())
serialDteAlarmFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteAlarmFarIndex.setStatus(_A)
_SerialDteAlarmIndex_Type=Integer32
_SerialDteAlarmIndex_Object=MibTableColumn
serialDteAlarmIndex=_SerialDteAlarmIndex_Object((1,3,6,1,4,1,321,100,2,5,2,1,3),_SerialDteAlarmIndex_Type())
serialDteAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteAlarmIndex.setStatus(_A)
class _SerialDteDTRAlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A1,1),('serialDteDTRAlarmDisable',2),('serialDteDTRAlarmEnable',3)))
_SerialDteDTRAlarmControl_Type.__name__=_C
_SerialDteDTRAlarmControl_Object=MibTableColumn
serialDteDTRAlarmControl=_SerialDteDTRAlarmControl_Object((1,3,6,1,4,1,321,100,2,5,2,1,4),_SerialDteDTRAlarmControl_Type())
serialDteDTRAlarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteDTRAlarmControl.setStatus(_A)
class _SerialDteDTRAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A1,1),('serialDteDTRAlarmNone',2),('serialDteDTRAlarmActive',3)))
_SerialDteDTRAlarmStatus_Type.__name__=_C
_SerialDteDTRAlarmStatus_Object=MibTableColumn
serialDteDTRAlarmStatus=_SerialDteDTRAlarmStatus_Object((1,3,6,1,4,1,321,100,2,5,2,1,5),_SerialDteDTRAlarmStatus_Type())
serialDteDTRAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteDTRAlarmStatus.setStatus(_A)
class _SerialDteStatusSummary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SerialDteStatusSummary_Type.__name__=_F
_SerialDteStatusSummary_Object=MibTableColumn
serialDteStatusSummary=_SerialDteStatusSummary_Object((1,3,6,1,4,1,321,100,2,5,2,1,6),_SerialDteStatusSummary_Type())
serialDteStatusSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteStatusSummary.setStatus(_A)
class _SerialDteAlarmSummary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SerialDteAlarmSummary_Type.__name__=_F
_SerialDteAlarmSummary_Object=MibTableColumn
serialDteAlarmSummary=_SerialDteAlarmSummary_Object((1,3,6,1,4,1,321,100,2,5,2,1,7),_SerialDteAlarmSummary_Type())
serialDteAlarmSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteAlarmSummary.setStatus(_A)
class _SerialDteASCStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteStatusASCOther',1),('serialDteStatusNoASC',2),('serialDteStatusASC',3)))
_SerialDteASCStatus_Type.__name__=_C
_SerialDteASCStatus_Object=MibTableColumn
serialDteASCStatus=_SerialDteASCStatus_Object((1,3,6,1,4,1,321,100,2,5,2,1,8),_SerialDteASCStatus_Type())
serialDteASCStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteASCStatus.setStatus(_A)
_SerialDteASCCount_Type=Integer32
_SerialDteASCCount_Object=MibTableColumn
serialDteASCCount=_SerialDteASCCount_Object((1,3,6,1,4,1,321,100,2,5,2,1,9),_SerialDteASCCount_Type())
serialDteASCCount.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteASCCount.setStatus(_A)
_SerialDteASCThreshold_Type=Integer32
_SerialDteASCThreshold_Object=MibTableColumn
serialDteASCThreshold=_SerialDteASCThreshold_Object((1,3,6,1,4,1,321,100,2,5,2,1,10),_SerialDteASCThreshold_Type())
serialDteASCThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteASCThreshold.setStatus(_A)
class _SerialDteASCAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteASCAlarmOther',1),('serialDteASCAlarmNone',2),('serialDteASCAlarmThresholdExceeded',3)))
_SerialDteASCAlarm_Type.__name__=_C
_SerialDteASCAlarm_Object=MibTableColumn
serialDteASCAlarm=_SerialDteASCAlarm_Object((1,3,6,1,4,1,321,100,2,5,2,1,11),_SerialDteASCAlarm_Type())
serialDteASCAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteASCAlarm.setStatus(_A)
class _SerialDteFDLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteStatusFDLOther',1),('serialDteStatusNoFDL',2),('serialDteStatusFDL',3)))
_SerialDteFDLStatus_Type.__name__=_C
_SerialDteFDLStatus_Object=MibTableColumn
serialDteFDLStatus=_SerialDteFDLStatus_Object((1,3,6,1,4,1,321,100,2,5,2,1,12),_SerialDteFDLStatus_Type())
serialDteFDLStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteFDLStatus.setStatus(_A)
_SerialDteFDLCount_Type=Integer32
_SerialDteFDLCount_Object=MibTableColumn
serialDteFDLCount=_SerialDteFDLCount_Object((1,3,6,1,4,1,321,100,2,5,2,1,13),_SerialDteFDLCount_Type())
serialDteFDLCount.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteFDLCount.setStatus(_A)
_SerialDteFDLThreshold_Type=Integer32
_SerialDteFDLThreshold_Object=MibTableColumn
serialDteFDLThreshold=_SerialDteFDLThreshold_Object((1,3,6,1,4,1,321,100,2,5,2,1,14),_SerialDteFDLThreshold_Type())
serialDteFDLThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteFDLThreshold.setStatus(_A)
class _SerialDteFDLAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteFDLAlarmOther',1),('serialDteFDLAlarmNone',2),('serialDteFDLAlarmThresholdExceeded',3)))
_SerialDteFDLAlarm_Type.__name__=_C
_SerialDteFDLAlarm_Object=MibTableColumn
serialDteFDLAlarm=_SerialDteFDLAlarm_Object((1,3,6,1,4,1,321,100,2,5,2,1,15),_SerialDteFDLAlarm_Type())
serialDteFDLAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteFDLAlarm.setStatus(_A)
class _SerialDteLOSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteStatusLOSOther',1),('serialDteStatusNoLOS',2),('serialDteStatusLOS',3)))
_SerialDteLOSStatus_Type.__name__=_C
_SerialDteLOSStatus_Object=MibTableColumn
serialDteLOSStatus=_SerialDteLOSStatus_Object((1,3,6,1,4,1,321,100,2,5,2,1,16),_SerialDteLOSStatus_Type())
serialDteLOSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteLOSStatus.setStatus(_A)
_SerialDteLOSCount_Type=Integer32
_SerialDteLOSCount_Object=MibTableColumn
serialDteLOSCount=_SerialDteLOSCount_Object((1,3,6,1,4,1,321,100,2,5,2,1,17),_SerialDteLOSCount_Type())
serialDteLOSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteLOSCount.setStatus(_A)
_SerialDteLOSThreshold_Type=Integer32
_SerialDteLOSThreshold_Object=MibTableColumn
serialDteLOSThreshold=_SerialDteLOSThreshold_Object((1,3,6,1,4,1,321,100,2,5,2,1,18),_SerialDteLOSThreshold_Type())
serialDteLOSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:serialDteLOSThreshold.setStatus(_A)
class _SerialDteLOSAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialDteLOSAlarmOther',1),('serialDteLOSAlarmNone',2),('serialDteLOSAlarmThresholdExceeded',3)))
_SerialDteLOSAlarm_Type.__name__=_C
_SerialDteLOSAlarm_Object=MibTableColumn
serialDteLOSAlarm=_SerialDteLOSAlarm_Object((1,3,6,1,4,1,321,100,2,5,2,1,19),_SerialDteLOSAlarm_Type())
serialDteLOSAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:serialDteLOSAlarm.setStatus(_A)
_AnalogDte_ObjectIdentity=ObjectIdentity
analogDte=_AnalogDte_ObjectIdentity((1,3,6,1,4,1,321,100,2,6))
_AnalogDteTable_Object=MibTable
analogDteTable=_AnalogDteTable_Object((1,3,6,1,4,1,321,100,2,6,1))
if mibBuilder.loadTexts:analogDteTable.setStatus(_A)
_AnalogDteTableEntry_Object=MibTableRow
analogDteTableEntry=_AnalogDteTableEntry_Object((1,3,6,1,4,1,321,100,2,6,1,1))
analogDteTableEntry.setIndexNames((0,_E,_A2),(0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:analogDteTableEntry.setStatus(_A)
_AnalogDteNearIndex_Type=Integer32
_AnalogDteNearIndex_Object=MibTableColumn
analogDteNearIndex=_AnalogDteNearIndex_Object((1,3,6,1,4,1,321,100,2,6,1,1,1),_AnalogDteNearIndex_Type())
analogDteNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:analogDteNearIndex.setStatus(_A)
_AnalogDteFarIndex_Type=Integer32
_AnalogDteFarIndex_Object=MibTableColumn
analogDteFarIndex=_AnalogDteFarIndex_Object((1,3,6,1,4,1,321,100,2,6,1,1,2),_AnalogDteFarIndex_Type())
analogDteFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:analogDteFarIndex.setStatus(_A)
_AnalogDteIndex_Type=Integer32
_AnalogDteIndex_Object=MibTableColumn
analogDteIndex=_AnalogDteIndex_Object((1,3,6,1,4,1,321,100,2,6,1,1,3),_AnalogDteIndex_Type())
analogDteIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:analogDteIndex.setStatus(_A)
class _AnalogDteDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AnalogDteDescription_Type.__name__=_F
_AnalogDteDescription_Object=MibTableColumn
analogDteDescription=_AnalogDteDescription_Object((1,3,6,1,4,1,321,100,2,6,1,1,4),_AnalogDteDescription_Type())
analogDteDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:analogDteDescription.setStatus(_A)
class _AnalogDteCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('analogDteCardTypeOther',1),('analogDteCardTypeFXS',2),('analogDteCardTypeFXO',3),('analogDteCardType4WEM',4)))
_AnalogDteCardType_Type.__name__=_C
_AnalogDteCardType_Object=MibTableColumn
analogDteCardType=_AnalogDteCardType_Object((1,3,6,1,4,1,321,100,2,6,1,1,5),_AnalogDteCardType_Type())
analogDteCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:analogDteCardType.setStatus(_A)
class _AnalogDteMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('analogDteModeOther',1),('analogDteModeSpare',2),('analogDteModeActive',3)))
_AnalogDteMode_Type.__name__=_C
_AnalogDteMode_Object=MibTableColumn
analogDteMode=_AnalogDteMode_Object((1,3,6,1,4,1,321,100,2,6,1,1,6),_AnalogDteMode_Type())
analogDteMode.setMaxAccess(_D)
if mibBuilder.loadTexts:analogDteMode.setStatus(_A)
class _AnalogDteState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('analogDteStateOther',1),('analogDteStateIdle',2),('analogDteStateBusy',3)))
_AnalogDteState_Type.__name__=_C
_AnalogDteState_Object=MibTableColumn
analogDteState=_AnalogDteState_Object((1,3,6,1,4,1,321,100,2,6,1,1,7),_AnalogDteState_Type())
analogDteState.setMaxAccess(_B)
if mibBuilder.loadTexts:analogDteState.setStatus(_A)
class _AnalogDteElementID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AnalogDteElementID_Type.__name__=_F
_AnalogDteElementID_Object=MibTableColumn
analogDteElementID=_AnalogDteElementID_Object((1,3,6,1,4,1,321,100,2,6,1,1,8),_AnalogDteElementID_Type())
analogDteElementID.setMaxAccess(_D)
if mibBuilder.loadTexts:analogDteElementID.setStatus(_A)
class _AnalogDteSignalling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)));namedValues=NamedValues(*(('analogDteSignallingOther',1),('analogDteSignallingFXSLS',2),('analogDteSignallingFXSGS',3),('analogDteSignallingUVG',4),('analogDteSignallingMEGLS',5),('analogDteSignallingMEGGS',6),('analogDteSignallingMEGRLS',7),('analogDteSignallingMEGRGS',8),('analogDteSignallingPLAR',9),('analogDteSignallingSLC96',10),('analogDteSignallingDIDDNIS',11),('analogDteSignallingDNISWLS',12),('analogDteSignallingDNISDLS',13),('analogDteSignallingDNISWRLS',14),('analogDteSignallingDNISDRLS',15),('analogDteSignallingDNISWGS',16),('analogDteSignallingDNISDGS',17),('analogDteSignallingDNISWRGS',18),('analogDteSignallingDNISDRGS',19),('analogDteSignallingFXOLS',20),('analogDteSignallingFXOGS',21),('analogDteSignallingFXOUVG',22),('analogDteSignallingFXOUVGR',23),('analogDteSignalling4WEMTYPE1',24),('analogDteSignalling4WEMTYPE2',25),('analogDteSignalling4WEMTYPE3',26),('analogDteSignalling4WEMTYPE4',27),('analogDteSignalling4WEMTYPE5',28),('analogDteSignalling4WEMTO',29)))
_AnalogDteSignalling_Type.__name__=_C
_AnalogDteSignalling_Object=MibTableColumn
analogDteSignalling=_AnalogDteSignalling_Object((1,3,6,1,4,1,321,100,2,6,1,1,9),_AnalogDteSignalling_Type())
analogDteSignalling.setMaxAccess(_D)
if mibBuilder.loadTexts:analogDteSignalling.setStatus(_A)
class _AnalogDteDNISDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('analogDteDNISDelayOther',1),('analogDteDNISDelay1Second',2),('analogDteDNISDelay2Seconds',3),('analogDteDNISDelay3Seconds',4),('analogDteDNISDelay4Seconds',5),('analogDteDNISDelay5Seconds',6)))
_AnalogDteDNISDelay_Type.__name__=_C
_AnalogDteDNISDelay_Object=MibTableColumn
analogDteDNISDelay=_AnalogDteDNISDelay_Object((1,3,6,1,4,1,321,100,2,6,1,1,10),_AnalogDteDNISDelay_Type())
analogDteDNISDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:analogDteDNISDelay.setStatus(_A)
class _AnalogDteTxGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('analogDteTxGainOther',1),('analogDteTxGain3DB',2),('analogDteTxGain2DB',3),('analogDteTxGain1DB',4),('analogDteTxGain0DB',5),('analogDteTxGainm1DB',6),('analogDteTxGainm2DB',7),('analogDteTxGainm3DB',8),('analogDteTxGainm4DB',9),('analogDteTxGainm5DB',10),('analogDteTxGainm6DB',11),('analogDteTxGainm7DB',12),('analogDteTxGainm8DB',13),('analogDteTxGainm9DB',14),('analogDteTxGainm10DB',15)))
_AnalogDteTxGain_Type.__name__=_C
_AnalogDteTxGain_Object=MibTableColumn
analogDteTxGain=_AnalogDteTxGain_Object((1,3,6,1,4,1,321,100,2,6,1,1,11),_AnalogDteTxGain_Type())
analogDteTxGain.setMaxAccess(_D)
if mibBuilder.loadTexts:analogDteTxGain.setStatus(_A)
class _AnalogDteRxGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('analogDteRxGainOther',1),('analogDteRxGain2DB',2),('analogDteRxGain1DB',3),('analogDteRxGain0DB',4),('analogDteRxGainm1DB',5),('analogDteRxGainm2DB',6),('analogDteRxGainm3DB',7),('analogDteRxGainm4DB',8),('analogDteRxGainm5DB',9),('analogDteRxGainm6DB',10),('analogDteRxGainm7DB',11),('analogDteRxGainm8DB',12),('analogDteRxGainm9DB',13),('analogDteRxGainm10DB',14),('analogDteRxGainm11DB',15),('analogDteRxGainm12DB',16),('analogDteRxGainm13DB',17),('analogDteRxGainm14DB',18),('analogDteRxGainm15DB',19),('analogDteRxGainm16DB',20)))
_AnalogDteRxGain_Type.__name__=_C
_AnalogDteRxGain_Object=MibTableColumn
analogDteRxGain=_AnalogDteRxGain_Object((1,3,6,1,4,1,321,100,2,6,1,1,12),_AnalogDteRxGain_Type())
analogDteRxGain.setMaxAccess(_D)
if mibBuilder.loadTexts:analogDteRxGain.setStatus(_A)
_Connection_ObjectIdentity=ObjectIdentity
connection=_Connection_ObjectIdentity((1,3,6,1,4,1,321,100,2,7))
_ConnectionTable_Object=MibTable
connectionTable=_ConnectionTable_Object((1,3,6,1,4,1,321,100,2,7,1))
if mibBuilder.loadTexts:connectionTable.setStatus(_A)
_ConnectionTableEntry_Object=MibTableRow
connectionTableEntry=_ConnectionTableEntry_Object((1,3,6,1,4,1,321,100,2,7,1,1))
connectionTableEntry.setIndexNames((0,_E,_A5),(0,_E,_A6),(0,_E,_A7))
if mibBuilder.loadTexts:connectionTableEntry.setStatus(_A)
_ConnectionNearIndex_Type=Integer32
_ConnectionNearIndex_Object=MibTableColumn
connectionNearIndex=_ConnectionNearIndex_Object((1,3,6,1,4,1,321,100,2,7,1,1,1),_ConnectionNearIndex_Type())
connectionNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionNearIndex.setStatus(_A)
_ConnectionFarIndex_Type=Integer32
_ConnectionFarIndex_Object=MibTableColumn
connectionFarIndex=_ConnectionFarIndex_Object((1,3,6,1,4,1,321,100,2,7,1,1,2),_ConnectionFarIndex_Type())
connectionFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionFarIndex.setStatus(_A)
_ConnectionTableIndex_Type=Integer32
_ConnectionTableIndex_Object=MibTableColumn
connectionTableIndex=_ConnectionTableIndex_Object((1,3,6,1,4,1,321,100,2,7,1,1,3),_ConnectionTableIndex_Type())
connectionTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionTableIndex.setStatus(_A)
class _ConnectionTableDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_ConnectionTableDescription_Type.__name__=_F
_ConnectionTableDescription_Object=MibTableColumn
connectionTableDescription=_ConnectionTableDescription_Object((1,3,6,1,4,1,321,100,2,7,1,1,4),_ConnectionTableDescription_Type())
connectionTableDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionTableDescription.setStatus(_A)
_ConnectionChannelTable_Object=MibTable
connectionChannelTable=_ConnectionChannelTable_Object((1,3,6,1,4,1,321,100,2,7,2))
if mibBuilder.loadTexts:connectionChannelTable.setStatus(_A)
_ConnectionChannelEntry_Object=MibTableRow
connectionChannelEntry=_ConnectionChannelEntry_Object((1,3,6,1,4,1,321,100,2,7,2,1))
connectionChannelEntry.setIndexNames((0,_E,_A8),(0,_E,_A9),(0,_E,_AA),(0,_E,_AB))
if mibBuilder.loadTexts:connectionChannelEntry.setStatus(_A)
_ConnectionChannelNearIndex_Type=Integer32
_ConnectionChannelNearIndex_Object=MibTableColumn
connectionChannelNearIndex=_ConnectionChannelNearIndex_Object((1,3,6,1,4,1,321,100,2,7,2,1,1),_ConnectionChannelNearIndex_Type())
connectionChannelNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionChannelNearIndex.setStatus(_A)
_ConnectionChannelFarIndex_Type=Integer32
_ConnectionChannelFarIndex_Object=MibTableColumn
connectionChannelFarIndex=_ConnectionChannelFarIndex_Object((1,3,6,1,4,1,321,100,2,7,2,1,2),_ConnectionChannelFarIndex_Type())
connectionChannelFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionChannelFarIndex.setStatus(_A)
_ConnectionChannelLineIndex_Type=Integer32
_ConnectionChannelLineIndex_Object=MibTableColumn
connectionChannelLineIndex=_ConnectionChannelLineIndex_Object((1,3,6,1,4,1,321,100,2,7,2,1,3),_ConnectionChannelLineIndex_Type())
connectionChannelLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionChannelLineIndex.setStatus(_A)
_ConnectionChannelIndex_Type=Integer32
_ConnectionChannelIndex_Object=MibTableColumn
connectionChannelIndex=_ConnectionChannelIndex_Object((1,3,6,1,4,1,321,100,2,7,2,1,4),_ConnectionChannelIndex_Type())
connectionChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionChannelIndex.setStatus(_A)
class _ChannelInterfaceAssignment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106)));namedValues=NamedValues(*((_G,1),('unassigned',2),('dTE',3),('remComm',4),('port1',5),('port2',6),('port3',7),('port4',8),('port5',9),('port6',10),('port7',11),('port8',12),('port9',13),('port10',14),('port11',15),('port12',16),('port13',17),('port14',18),('port15',19),('port16',20),('port17',21),('port18',22),('port19',23),('port20',24),('port21',25),('port22',26),('port23',27),('port24',28),('port25',29),('port26',30),('port27',31),('port28',32),('port29',33),('port30',34),('port31',35),('port32',36),('slot2PortA',37),('slot2PortB',38),('slot3PortA',39),('slot3PortB',40),('slot4PortA',41),('slot4PortB',42),('slot5PortA',43),('slot5PortB',44),('slot6PortA',45),('slot6PortB',46),('slot2Dsu1PortA',47),('slot2Dsu1PortB',48),('slot2Dsu2PortA',49),('slot2Dsu2PortB',50),('slot2Dsu3PortA',51),('slot2Dsu3PortB',52),('slot2Dsu4PortA',53),('slot2Dsu4PortB',54),('slot2Dsu5PortA',55),('slot2Dsu5PortB',56),('slot2Dsu6PortA',57),('slot2Dsu6PortB',58),('slot3Dsu1PortA',59),('slot3Dsu1PortB',60),('slot3Dsu2PortA',61),('slot3Dsu2PortB',62),('slot3Dsu3PortA',63),('slot3Dsu3PortB',64),('slot3Dsu4PortA',65),('slot3Dsu4PortB',66),('slot3Dsu5PortA',67),('slot3Dsu5PortB',68),('slot3Dsu6PortA',69),('slot3Dsu6PortB',70),('slot4Dsu1PortA',71),('slot4Dsu1PortB',72),('slot4Dsu2PortA',73),('slot4Dsu2PortB',74),('slot4Dsu3PortA',75),('slot4Dsu3PortB',76),('slot4Dsu4PortA',77),('slot4Dsu4PortB',78),('slot4Dsu5PortA',79),('slot4Dsu5PortB',80),('slot4Dsu6PortA',81),('slot4Dsu6PortB',82),('slot5Dsu1PortA',83),('slot5Dsu1PortB',84),('slot5Dsu2PortA',85),('slot5Dsu2PortB',86),('slot5Dsu3PortA',87),('slot5Dsu3PortB',88),('slot5Dsu4PortA',89),('slot5Dsu4PortB',90),('slot5Dsu5PortA',91),('slot5Dsu5PortB',92),('slot5Dsu6PortA',93),('slot5Dsu6PortB',94),('slot6Dsu1PortA',95),('slot6Dsu1PortB',96),('slot6Dsu2PortA',97),('slot6Dsu2PortB',98),('slot6Dsu3PortA',99),('slot6Dsu3PortB',100),('slot6Dsu4PortA',101),('slot6Dsu4PortB',102),('slot6Dsu5PortA',103),('slot6Dsu5PortB',104),('slot6Dsu6PortA',105),('slot6Dsu6PortB',106)))
_ChannelInterfaceAssignment_Type.__name__=_C
_ChannelInterfaceAssignment_Object=MibTableColumn
channelInterfaceAssignment=_ChannelInterfaceAssignment_Object((1,3,6,1,4,1,321,100,2,7,2,1,5),_ChannelInterfaceAssignment_Type())
channelInterfaceAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:channelInterfaceAssignment.setStatus(_A)
class _ChannelInterfaceDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ChannelInterfaceDescription_Type.__name__=_F
_ChannelInterfaceDescription_Object=MibTableColumn
channelInterfaceDescription=_ChannelInterfaceDescription_Object((1,3,6,1,4,1,321,100,2,7,2,1,6),_ChannelInterfaceDescription_Type())
channelInterfaceDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInterfaceDescription.setStatus(_A)
_ChannelInterfaceChannel_Type=Integer32
_ChannelInterfaceChannel_Object=MibTableColumn
channelInterfaceChannel=_ChannelInterfaceChannel_Object((1,3,6,1,4,1,321,100,2,7,2,1,7),_ChannelInterfaceChannel_Type())
channelInterfaceChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:channelInterfaceChannel.setStatus(_A)
class _ChannelSignalling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('clearChannel',2),('robbedBit',3)))
_ChannelSignalling_Type.__name__=_C
_ChannelSignalling_Object=MibTableColumn
channelSignalling=_ChannelSignalling_Object((1,3,6,1,4,1,321,100,2,7,2,1,8),_ChannelSignalling_Type())
channelSignalling.setMaxAccess(_D)
if mibBuilder.loadTexts:channelSignalling.setStatus(_A)
_Maintenance_ObjectIdentity=ObjectIdentity
maintenance=_Maintenance_ObjectIdentity((1,3,6,1,4,1,321,100,2,8))
_BertTable_Object=MibTable
bertTable=_BertTable_Object((1,3,6,1,4,1,321,100,2,8,1))
if mibBuilder.loadTexts:bertTable.setStatus(_A)
_BertTableEntry_Object=MibTableRow
bertTableEntry=_BertTableEntry_Object((1,3,6,1,4,1,321,100,2,8,1,1))
bertTableEntry.setIndexNames((0,_E,_AC),(0,_E,_AD),(0,_E,_AE))
if mibBuilder.loadTexts:bertTableEntry.setStatus(_A)
_BertNearIndex_Type=Integer32
_BertNearIndex_Object=MibTableColumn
bertNearIndex=_BertNearIndex_Object((1,3,6,1,4,1,321,100,2,8,1,1,1),_BertNearIndex_Type())
bertNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bertNearIndex.setStatus(_A)
_BertFarIndex_Type=Integer32
_BertFarIndex_Object=MibTableColumn
bertFarIndex=_BertFarIndex_Object((1,3,6,1,4,1,321,100,2,8,1,1,2),_BertFarIndex_Type())
bertFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bertFarIndex.setStatus(_A)
_BertIndex_Type=Integer32
_BertIndex_Object=MibTableColumn
bertIndex=_BertIndex_Object((1,3,6,1,4,1,321,100,2,8,1,1,3),_BertIndex_Type())
bertIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bertIndex.setStatus(_A)
class _BertPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('bertPatternOther',1),('bertPatternQRSS',2),('bertPattern63',3),('bertPattern511',4),('bertPattern2047',5),('bertPattern215',6),('bertPattern220',7),('bertPattern223',8),('bertPattern1in8',9),('bertPattern3in24',10),('bertPatternALT',11),('bertPatternCLEAR',12)))
_BertPattern_Type.__name__=_C
_BertPattern_Object=MibTableColumn
bertPattern=_BertPattern_Object((1,3,6,1,4,1,321,100,2,8,1,1,4),_BertPattern_Type())
bertPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:bertPattern.setStatus(_A)
class _BertLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('bertLengthOther',1),('bertLength15minutes',2),('bertLength30minutes',3),('bertLength60minutes',4),('bertLength24hours',5),('bertLengthContinuous',6)))
_BertLength_Type.__name__=_C
_BertLength_Object=MibTableColumn
bertLength=_BertLength_Object((1,3,6,1,4,1,321,100,2,8,1,1,5),_BertLength_Type())
bertLength.setMaxAccess(_D)
if mibBuilder.loadTexts:bertLength.setStatus(_A)
class _BertPatternSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bertPatternSyncOther',1),('bertPatternSyncNoTest',2),('bertPatternSyncNoSync',3),('bertPatternSyncInsync',4)))
_BertPatternSync_Type.__name__=_C
_BertPatternSync_Object=MibTableColumn
bertPatternSync=_BertPatternSync_Object((1,3,6,1,4,1,321,100,2,8,1,1,6),_BertPatternSync_Type())
bertPatternSync.setMaxAccess(_B)
if mibBuilder.loadTexts:bertPatternSync.setStatus(_A)
_BertElapsedTime_Type=Integer32
_BertElapsedTime_Object=MibTableColumn
bertElapsedTime=_BertElapsedTime_Object((1,3,6,1,4,1,321,100,2,8,1,1,7),_BertElapsedTime_Type())
bertElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bertElapsedTime.setStatus(_A)
_BertBitErrors_Type=Integer32
_BertBitErrors_Object=MibTableColumn
bertBitErrors=_BertBitErrors_Object((1,3,6,1,4,1,321,100,2,8,1,1,8),_BertBitErrors_Type())
bertBitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:bertBitErrors.setStatus(_A)
_BertErroredSeconds_Type=Integer32
_BertErroredSeconds_Object=MibTableColumn
bertErroredSeconds=_BertErroredSeconds_Object((1,3,6,1,4,1,321,100,2,8,1,1,9),_BertErroredSeconds_Type())
bertErroredSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:bertErroredSeconds.setStatus(_A)
_BertPercentEFS_Type=Integer32
_BertPercentEFS_Object=MibTableColumn
bertPercentEFS=_BertPercentEFS_Object((1,3,6,1,4,1,321,100,2,8,1,1,10),_BertPercentEFS_Type())
bertPercentEFS.setMaxAccess(_B)
if mibBuilder.loadTexts:bertPercentEFS.setStatus(_A)
class _BertCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('bertCommandOther',1),('bertCommandStart',2),('bertCommandStop',3),('bertCommandResetErrors',4),('bertCommandInjectError',5)))
_BertCommand_Type.__name__=_C
_BertCommand_Object=MibTableColumn
bertCommand=_BertCommand_Object((1,3,6,1,4,1,321,100,2,8,1,1,11),_BertCommand_Type())
bertCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:bertCommand.setStatus(_A)
_BertInterfaceTable_Object=MibTable
bertInterfaceTable=_BertInterfaceTable_Object((1,3,6,1,4,1,321,100,2,8,2))
if mibBuilder.loadTexts:bertInterfaceTable.setStatus(_A)
_BertInterfaceTableEntry_Object=MibTableRow
bertInterfaceTableEntry=_BertInterfaceTableEntry_Object((1,3,6,1,4,1,321,100,2,8,2,1))
bertInterfaceTableEntry.setIndexNames((0,_E,_AF),(0,_E,_AG),(0,_E,_AH),(0,_E,_AI))
if mibBuilder.loadTexts:bertInterfaceTableEntry.setStatus(_A)
_BertInterfaceNearIndex_Type=Integer32
_BertInterfaceNearIndex_Object=MibTableColumn
bertInterfaceNearIndex=_BertInterfaceNearIndex_Object((1,3,6,1,4,1,321,100,2,8,2,1,1),_BertInterfaceNearIndex_Type())
bertInterfaceNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bertInterfaceNearIndex.setStatus(_A)
_BertInterfaceFarIndex_Type=Integer32
_BertInterfaceFarIndex_Object=MibTableColumn
bertInterfaceFarIndex=_BertInterfaceFarIndex_Object((1,3,6,1,4,1,321,100,2,8,2,1,2),_BertInterfaceFarIndex_Type())
bertInterfaceFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bertInterfaceFarIndex.setStatus(_A)
_BertChipIndex_Type=Integer32
_BertChipIndex_Object=MibTableColumn
bertChipIndex=_BertChipIndex_Object((1,3,6,1,4,1,321,100,2,8,2,1,3),_BertChipIndex_Type())
bertChipIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bertChipIndex.setStatus(_A)
_BertInterfaceIndex_Type=Integer32
_BertInterfaceIndex_Object=MibTableColumn
bertInterfaceIndex=_BertInterfaceIndex_Object((1,3,6,1,4,1,321,100,2,8,2,1,4),_BertInterfaceIndex_Type())
bertInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:bertInterfaceIndex.setStatus(_A)
class _BertInterfaceSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*(('bertInterfaceSettingOther',1),('bertInterfaceSettingIdle',2),('bertInterfaceSettingChannel1',3),('bertInterfaceSettingChannel2',4),('bertInterfaceSettingChannel3',5),('bertInterfaceSettingChannel4',6),('bertInterfaceSettingChannel5',7),('bertInterfaceSettingChannel6',8),('bertInterfaceSettingChannel7',9),('bertInterfaceSettingChannel8',10),('bertInterfaceSettingChannel9',11),('bertInterfaceSettingChannel10',12),('bertInterfaceSettingChannel11',13),('bertInterfaceSettingChannel12',14),('bertInterfaceSettingChannel13',15),('bertInterfaceSettingChannel14',16),('bertInterfaceSettingChannel15',17),('bertInterfaceSettingChannel16',18),('bertInterfaceSettingChannel17',19),('bertInterfaceSettingChannel18',20),('bertInterfaceSettingChannel19',21),('bertInterfaceSettingChannel20',22),('bertInterfaceSettingChannel21',23),('bertInterfaceSettingChannel22',24),('bertInterfaceSettingChannel23',25),('bertInterfaceSettingChannel24',26),('bertInterfaceSettingChannel25',27),('bertInterfaceSettingChannel26',28),('bertInterfaceSettingChannel27',29),('bertInterfaceSettingChannel28',30),('bertInterfaceSettingChannel29',31),('bertInterfaceSettingChannel30',32),('bertInterfaceSettingChannel31',33),('bertInterfaceSettingChannel32',34),('bertInterfaceSettingNet',35),('bertInterfaceSettingDTE',36),('bertInterfaceSettingNotEnabled',37),('bertInterfaceSettingUseService',38)))
_BertInterfaceSetting_Type.__name__=_C
_BertInterfaceSetting_Object=MibTableColumn
bertInterfaceSetting=_BertInterfaceSetting_Object((1,3,6,1,4,1,321,100,2,8,2,1,5),_BertInterfaceSetting_Type())
bertInterfaceSetting.setMaxAccess(_D)
if mibBuilder.loadTexts:bertInterfaceSetting.setStatus(_A)
_BertInterfaceService_Type=Integer32
_BertInterfaceService_Object=MibTableColumn
bertInterfaceService=_BertInterfaceService_Object((1,3,6,1,4,1,321,100,2,8,2,1,6),_BertInterfaceService_Type())
bertInterfaceService.setMaxAccess(_D)
if mibBuilder.loadTexts:bertInterfaceService.setStatus(_A)
class _BertInterfaceChannelRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('nx56k',2),('nx64k',3)))
_BertInterfaceChannelRate_Type.__name__=_C
_BertInterfaceChannelRate_Object=MibTableColumn
bertInterfaceChannelRate=_BertInterfaceChannelRate_Object((1,3,6,1,4,1,321,100,2,8,2,1,7),_BertInterfaceChannelRate_Type())
bertInterfaceChannelRate.setMaxAccess(_D)
if mibBuilder.loadTexts:bertInterfaceChannelRate.setStatus(_A)
_TestTable_Object=MibTable
testTable=_TestTable_Object((1,3,6,1,4,1,321,100,2,8,3))
if mibBuilder.loadTexts:testTable.setStatus(_A)
_TestTableEntry_Object=MibTableRow
testTableEntry=_TestTableEntry_Object((1,3,6,1,4,1,321,100,2,8,3,1))
testTableEntry.setIndexNames((0,_E,_AJ),(0,_E,_AK),(0,_E,_AL))
if mibBuilder.loadTexts:testTableEntry.setStatus(_A)
_TestNearIndex_Type=Integer32
_TestNearIndex_Object=MibTableColumn
testNearIndex=_TestNearIndex_Object((1,3,6,1,4,1,321,100,2,8,3,1,1),_TestNearIndex_Type())
testNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:testNearIndex.setStatus(_A)
_TestFarIndex_Type=Integer32
_TestFarIndex_Object=MibTableColumn
testFarIndex=_TestFarIndex_Object((1,3,6,1,4,1,321,100,2,8,3,1,2),_TestFarIndex_Type())
testFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:testFarIndex.setStatus(_A)
_TestTableIndex_Type=Integer32
_TestTableIndex_Object=MibTableColumn
testTableIndex=_TestTableIndex_Object((1,3,6,1,4,1,321,100,2,8,3,1,3),_TestTableIndex_Type())
testTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:testTableIndex.setStatus(_A)
class _TestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('testTypeOther',1),('testTypeNoTest',2),('testTypePLB',3),('testTypeLLB',4),('testtypeMLB',5),('testTypeFarPLB',6),('testTypeFarLLB',7),('testTypeFarMLB',8),('testTypePortLoop',9),('testTypeV54Loop',10),('testTypeFarV54Loop',11),('testTypeFarPortLoop',12),('testTypeTDM',13),('testTypeFarPortUnloop',14),('testTypeFarV54Unloop',15),('testTypeDualLoop',16),('testTypeNetworkSideTransparent',17),('testTypeNetworkSideNonTransparent',18),('testTypeCustomerSideTransparent',19),('testTypeCustomerSideNonTransparent',20)))
_TestType_Type.__name__=_C
_TestType_Object=MibTableColumn
testType=_TestType_Object((1,3,6,1,4,1,321,100,2,8,3,1,4),_TestType_Type())
testType.setMaxAccess(_D)
if mibBuilder.loadTexts:testType.setStatus(_A)
class _TestLoopDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('testLoopOther',1),('testLoopUnidirectional',2),('testLoopBidirectional',3)))
_TestLoopDirection_Type.__name__=_C
_TestLoopDirection_Object=MibTableColumn
testLoopDirection=_TestLoopDirection_Object((1,3,6,1,4,1,321,100,2,8,3,1,5),_TestLoopDirection_Type())
testLoopDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:testLoopDirection.setStatus(_A)
class _TestFarLLBFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('testFarLLBFramingOther',1),('testFarLLBFramingUnframed',2),('testFarLLBFramingFramed',3)))
_TestFarLLBFraming_Type.__name__=_C
_TestFarLLBFraming_Object=MibTableColumn
testFarLLBFraming=_TestFarLLBFraming_Object((1,3,6,1,4,1,321,100,2,8,3,1,6),_TestFarLLBFraming_Type())
testFarLLBFraming.setMaxAccess(_D)
if mibBuilder.loadTexts:testFarLLBFraming.setStatus(_A)
class _TestLoopInitiator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('testLoopInitiatorOther',1),('testLoopInitiatorLMP',2),('testLoopInitiatorSNMP',3),('testLoopInitiatorWeb',4),('testLoopInitiatorEOC',5),('testLoopInitiatorButtons',6),('testLoopInitiatorDCEControl',7),('testLoopInitiatorISDNPRAV3',8)))
_TestLoopInitiator_Type.__name__=_C
_TestLoopInitiator_Object=MibTableColumn
testLoopInitiator=_TestLoopInitiator_Object((1,3,6,1,4,1,321,100,2,8,3,1,7),_TestLoopInitiator_Type())
testLoopInitiator.setMaxAccess(_B)
if mibBuilder.loadTexts:testLoopInitiator.setStatus(_A)
class _TestDefaultLoopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('testDefaultLoopTypeOther',1),('testDefaultLoopTypeTransparent',2),('testDefaultLoopTypeNonTransparent',3),('testDefaultLoopTypeDual',4)))
_TestDefaultLoopType_Type.__name__=_C
_TestDefaultLoopType_Object=MibTableColumn
testDefaultLoopType=_TestDefaultLoopType_Object((1,3,6,1,4,1,321,100,2,8,3,1,8),_TestDefaultLoopType_Type())
testDefaultLoopType.setMaxAccess(_D)
if mibBuilder.loadTexts:testDefaultLoopType.setStatus(_A)
_Performance_ObjectIdentity=ObjectIdentity
performance=_Performance_ObjectIdentity((1,3,6,1,4,1,321,100,2,9))
_Performance24Table_Object=MibTable
performance24Table=_Performance24Table_Object((1,3,6,1,4,1,321,100,2,9,1))
if mibBuilder.loadTexts:performance24Table.setStatus(_A)
_Performance24TableEntry_Object=MibTableRow
performance24TableEntry=_Performance24TableEntry_Object((1,3,6,1,4,1,321,100,2,9,1,1))
performance24TableEntry.setIndexNames((0,_E,_AM),(0,_E,_AN),(0,_E,_AO),(0,_E,_AP))
if mibBuilder.loadTexts:performance24TableEntry.setStatus(_A)
_Performance24NearIndex_Type=Integer32
_Performance24NearIndex_Object=MibTableColumn
performance24NearIndex=_Performance24NearIndex_Object((1,3,6,1,4,1,321,100,2,9,1,1,1),_Performance24NearIndex_Type())
performance24NearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24NearIndex.setStatus(_A)
_Performance24FarIndex_Type=Integer32
_Performance24FarIndex_Object=MibTableColumn
performance24FarIndex=_Performance24FarIndex_Object((1,3,6,1,4,1,321,100,2,9,1,1,2),_Performance24FarIndex_Type())
performance24FarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24FarIndex.setStatus(_A)
_Performance24InterfaceIndex_Type=Integer32
_Performance24InterfaceIndex_Object=MibTableColumn
performance24InterfaceIndex=_Performance24InterfaceIndex_Object((1,3,6,1,4,1,321,100,2,9,1,1,3),_Performance24InterfaceIndex_Type())
performance24InterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24InterfaceIndex.setStatus(_A)
class _Performance24Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98)));namedValues=NamedValues(*(('performance24Summary',1),('performance24Current',2),('performance24period1',3),('performance24period2',4),('performance24period3',5),('performance24period4',6),('performance24period5',7),('performance24period6',8),('performance24period7',9),('performance24period8',10),('performance24period9',11),('performance24period10',12),('performance24period11',13),('performance24period12',14),('performance24period13',15),('performance24period14',16),('performance24period15',17),('performance24period16',18),('performance24period17',19),('performance24period18',20),('performance24period19',21),('performance24period20',22),('performance24period21',23),('performance24period22',24),('performance24period23',25),('performance24period24',26),('performance24period25',27),('performance24period26',28),('performance24period27',29),('performance24period28',30),('performance24period29',31),('performance24period30',32),('performance24period31',33),('performance24period32',34),('performance24period33',35),('performance24period34',36),('performance24period35',37),('performance24period36',38),('performance24period37',39),('performance24period38',40),('performance24period39',41),('performance24period40',42),('performance24period41',43),('performance24period42',44),('performance24period43',45),('performance24period44',46),('performance24period45',47),('performance24period46',48),('performance24period47',49),('performance24period48',50),('performance24period49',51),('performance24period50',52),('performance24period51',53),('performance24period52',54),('performance24period53',55),('performance24period54',56),('performance24period55',57),('performance24period56',58),('performance24period57',59),('performance24period58',60),('performance24period59',61),('performance24period60',62),('performance24period61',63),('performance24period62',64),('performance24period63',65),('performance24period64',66),('performance24period65',67),('performance24period66',68),('performance24period67',69),('performance24period68',70),('performance24period69',71),('performance24period70',72),('performance24period71',73),('performance24period72',74),('performance24period73',75),('performance24period74',76),('performance24period75',77),('performance24period76',78),('performance24period77',79),('performance24period78',80),('performance24period79',81),('performance24period80',82),('performance24period81',83),('performance24period82',84),('performance24period83',85),('performance24period84',86),('performance24period85',87),('performance24period86',88),('performance24period87',89),('performance24period88',90),('performance24period89',91),('performance24period90',92),('performance24period91',93),('performance24period92',94),('performance24period93',95),('performance24period94',96),('performance24period95',97),('performance24period96',98)))
_Performance24Index_Type.__name__=_C
_Performance24Index_Object=MibTableColumn
performance24Index=_Performance24Index_Object((1,3,6,1,4,1,321,100,2,9,1,1,4),_Performance24Index_Type())
performance24Index.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24Index.setStatus(_A)
_Performance24ES_Type=Integer32
_Performance24ES_Object=MibTableColumn
performance24ES=_Performance24ES_Object((1,3,6,1,4,1,321,100,2,9,1,1,5),_Performance24ES_Type())
performance24ES.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24ES.setStatus(_A)
_Performance24BES_Type=Integer32
_Performance24BES_Object=MibTableColumn
performance24BES=_Performance24BES_Object((1,3,6,1,4,1,321,100,2,9,1,1,6),_Performance24BES_Type())
performance24BES.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24BES.setStatus(_A)
_Performance24SES_Type=Integer32
_Performance24SES_Object=MibTableColumn
performance24SES=_Performance24SES_Object((1,3,6,1,4,1,321,100,2,9,1,1,7),_Performance24SES_Type())
performance24SES.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24SES.setStatus(_A)
_Performance24UAS_Type=Integer32
_Performance24UAS_Object=MibTableColumn
performance24UAS=_Performance24UAS_Object((1,3,6,1,4,1,321,100,2,9,1,1,8),_Performance24UAS_Type())
performance24UAS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24UAS.setStatus(_A)
_Performance24LOFC_Type=Integer32
_Performance24LOFC_Object=MibTableColumn
performance24LOFC=_Performance24LOFC_Object((1,3,6,1,4,1,321,100,2,9,1,1,9),_Performance24LOFC_Type())
performance24LOFC.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24LOFC.setStatus(_A)
_Performance24CSS_Type=Integer32
_Performance24CSS_Object=MibTableColumn
performance24CSS=_Performance24CSS_Object((1,3,6,1,4,1,321,100,2,9,1,1,10),_Performance24CSS_Type())
performance24CSS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24CSS.setStatus(_A)
_Performance24CRCES_Type=Integer32
_Performance24CRCES_Object=MibTableColumn
performance24CRCES=_Performance24CRCES_Object((1,3,6,1,4,1,321,100,2,9,1,1,11),_Performance24CRCES_Type())
performance24CRCES.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24CRCES.setStatus(_A)
_Performance24OOFS_Type=Integer32
_Performance24OOFS_Object=MibTableColumn
performance24OOFS=_Performance24OOFS_Object((1,3,6,1,4,1,321,100,2,9,1,1,12),_Performance24OOFS_Type())
performance24OOFS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24OOFS.setStatus(_A)
_Performance24LOSS_Type=Integer32
_Performance24LOSS_Object=MibTableColumn
performance24LOSS=_Performance24LOSS_Object((1,3,6,1,4,1,321,100,2,9,1,1,13),_Performance24LOSS_Type())
performance24LOSS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24LOSS.setStatus(_A)
_Performance24AISS_Type=Integer32
_Performance24AISS_Object=MibTableColumn
performance24AISS=_Performance24AISS_Object((1,3,6,1,4,1,321,100,2,9,1,1,14),_Performance24AISS_Type())
performance24AISS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24AISS.setStatus(_A)
_Performance24RAS_Type=Integer32
_Performance24RAS_Object=MibTableColumn
performance24RAS=_Performance24RAS_Object((1,3,6,1,4,1,321,100,2,9,1,1,15),_Performance24RAS_Type())
performance24RAS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24RAS.setStatus(_A)
_Performance24BPVS_Type=Integer32
_Performance24BPVS_Object=MibTableColumn
performance24BPVS=_Performance24BPVS_Object((1,3,6,1,4,1,321,100,2,9,1,1,16),_Performance24BPVS_Type())
performance24BPVS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24BPVS.setStatus(_A)
_Performance24timestamp_Type=TimeTicks
_Performance24timestamp_Object=MibTableColumn
performance24timestamp=_Performance24timestamp_Object((1,3,6,1,4,1,321,100,2,9,1,1,17),_Performance24timestamp_Type())
performance24timestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:performance24timestamp.setStatus(_A)
_Performance30Table_Object=MibTable
performance30Table=_Performance30Table_Object((1,3,6,1,4,1,321,100,2,9,2))
if mibBuilder.loadTexts:performance30Table.setStatus(_A)
_Performance30TableEntry_Object=MibTableRow
performance30TableEntry=_Performance30TableEntry_Object((1,3,6,1,4,1,321,100,2,9,2,1))
performance30TableEntry.setIndexNames((0,_E,_AQ),(0,_E,_AR),(0,_E,_AS),(0,_E,_AT))
if mibBuilder.loadTexts:performance30TableEntry.setStatus(_A)
_Performance30NearIndex_Type=Integer32
_Performance30NearIndex_Object=MibTableColumn
performance30NearIndex=_Performance30NearIndex_Object((1,3,6,1,4,1,321,100,2,9,2,1,1),_Performance30NearIndex_Type())
performance30NearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30NearIndex.setStatus(_A)
_Performance30FarIndex_Type=Integer32
_Performance30FarIndex_Object=MibTableColumn
performance30FarIndex=_Performance30FarIndex_Object((1,3,6,1,4,1,321,100,2,9,2,1,2),_Performance30FarIndex_Type())
performance30FarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30FarIndex.setStatus(_A)
_Performance30InterfaceIndex_Type=Integer32
_Performance30InterfaceIndex_Object=MibTableColumn
performance30InterfaceIndex=_Performance30InterfaceIndex_Object((1,3,6,1,4,1,321,100,2,9,2,1,3),_Performance30InterfaceIndex_Type())
performance30InterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30InterfaceIndex.setStatus(_A)
class _Performance30Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('performance30Summary',1),('performance30day1',2),('performance30day2',3),('performance30day3',4),('performance30day4',5),('performance30day5',6),('performance30day6',7),('performance30day7',8),('performance30day8',9),('performance30day9',10),('performance30day10',11),('performance30day11',12),('performance30day12',13),('performance30day13',14),('performance30day14',15),('performance30day15',16),('performance30day16',17),('performance30day17',18),('performance30day18',19),('performance30day19',20),('performance30day20',21),('performance30day21',22),('performance30day22',23),('performance30day23',24),('performance30day24',25),('performance30day25',26),('performance30day26',27),('performance30day27',28),('performance30day28',29),('performance30day29',30),('performance30day30',31)))
_Performance30Index_Type.__name__=_C
_Performance30Index_Object=MibTableColumn
performance30Index=_Performance30Index_Object((1,3,6,1,4,1,321,100,2,9,2,1,4),_Performance30Index_Type())
performance30Index.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30Index.setStatus(_A)
_Performance30ES_Type=Integer32
_Performance30ES_Object=MibTableColumn
performance30ES=_Performance30ES_Object((1,3,6,1,4,1,321,100,2,9,2,1,5),_Performance30ES_Type())
performance30ES.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30ES.setStatus(_A)
_Performance30BES_Type=Integer32
_Performance30BES_Object=MibTableColumn
performance30BES=_Performance30BES_Object((1,3,6,1,4,1,321,100,2,9,2,1,6),_Performance30BES_Type())
performance30BES.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30BES.setStatus(_A)
_Performance30SES_Type=Integer32
_Performance30SES_Object=MibTableColumn
performance30SES=_Performance30SES_Object((1,3,6,1,4,1,321,100,2,9,2,1,7),_Performance30SES_Type())
performance30SES.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30SES.setStatus(_A)
_Performance30UAS_Type=Integer32
_Performance30UAS_Object=MibTableColumn
performance30UAS=_Performance30UAS_Object((1,3,6,1,4,1,321,100,2,9,2,1,8),_Performance30UAS_Type())
performance30UAS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30UAS.setStatus(_A)
_Performance30LOFC_Type=Integer32
_Performance30LOFC_Object=MibTableColumn
performance30LOFC=_Performance30LOFC_Object((1,3,6,1,4,1,321,100,2,9,2,1,9),_Performance30LOFC_Type())
performance30LOFC.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30LOFC.setStatus(_A)
_Performance30CSS_Type=Integer32
_Performance30CSS_Object=MibTableColumn
performance30CSS=_Performance30CSS_Object((1,3,6,1,4,1,321,100,2,9,2,1,10),_Performance30CSS_Type())
performance30CSS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30CSS.setStatus(_A)
_Performance30CRCES_Type=Integer32
_Performance30CRCES_Object=MibTableColumn
performance30CRCES=_Performance30CRCES_Object((1,3,6,1,4,1,321,100,2,9,2,1,11),_Performance30CRCES_Type())
performance30CRCES.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30CRCES.setStatus(_A)
_Performance30OOFS_Type=Integer32
_Performance30OOFS_Object=MibTableColumn
performance30OOFS=_Performance30OOFS_Object((1,3,6,1,4,1,321,100,2,9,2,1,12),_Performance30OOFS_Type())
performance30OOFS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30OOFS.setStatus(_A)
_Performance30LOSS_Type=Integer32
_Performance30LOSS_Object=MibTableColumn
performance30LOSS=_Performance30LOSS_Object((1,3,6,1,4,1,321,100,2,9,2,1,13),_Performance30LOSS_Type())
performance30LOSS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30LOSS.setStatus(_A)
_Performance30AISS_Type=Integer32
_Performance30AISS_Object=MibTableColumn
performance30AISS=_Performance30AISS_Object((1,3,6,1,4,1,321,100,2,9,2,1,14),_Performance30AISS_Type())
performance30AISS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30AISS.setStatus(_A)
_Performance30RAS_Type=Integer32
_Performance30RAS_Object=MibTableColumn
performance30RAS=_Performance30RAS_Object((1,3,6,1,4,1,321,100,2,9,2,1,15),_Performance30RAS_Type())
performance30RAS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30RAS.setStatus(_A)
_Performance30BPVS_Type=Integer32
_Performance30BPVS_Object=MibTableColumn
performance30BPVS=_Performance30BPVS_Object((1,3,6,1,4,1,321,100,2,9,2,1,16),_Performance30BPVS_Type())
performance30BPVS.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30BPVS.setStatus(_A)
_Performance30timestamp_Type=TimeTicks
_Performance30timestamp_Object=MibTableColumn
performance30timestamp=_Performance30timestamp_Object((1,3,6,1,4,1,321,100,2,9,2,1,17),_Performance30timestamp_Type())
performance30timestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:performance30timestamp.setStatus(_A)
_Itable_ObjectIdentity=ObjectIdentity
itable=_Itable_ObjectIdentity((1,3,6,1,4,1,321,100,2,10))
_ITable_Object=MibTable
iTable=_ITable_Object((1,3,6,1,4,1,321,100,2,10,1))
if mibBuilder.loadTexts:iTable.setStatus(_A)
_ITableEntry_Object=MibTableRow
iTableEntry=_ITableEntry_Object((1,3,6,1,4,1,321,100,2,10,1,1))
iTableEntry.setIndexNames((0,_E,_AU),(0,_E,_AV),(0,_E,_AW))
if mibBuilder.loadTexts:iTableEntry.setStatus(_A)
_ITableNearIndex_Type=Integer32
_ITableNearIndex_Object=MibTableColumn
iTableNearIndex=_ITableNearIndex_Object((1,3,6,1,4,1,321,100,2,10,1,1,1),_ITableNearIndex_Type())
iTableNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:iTableNearIndex.setStatus(_A)
_ITableFarIndex_Type=Integer32
_ITableFarIndex_Object=MibTableColumn
iTableFarIndex=_ITableFarIndex_Object((1,3,6,1,4,1,321,100,2,10,1,1,2),_ITableFarIndex_Type())
iTableFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:iTableFarIndex.setStatus(_A)
_ITableIndex_Type=Integer32
_ITableIndex_Object=MibTableColumn
iTableIndex=_ITableIndex_Object((1,3,6,1,4,1,321,100,2,10,1,1,3),_ITableIndex_Type())
iTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:iTableIndex.setStatus(_A)
class _IDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_IDescription_Type.__name__=_F
_IDescription_Object=MibTableColumn
iDescription=_IDescription_Object((1,3,6,1,4,1,321,100,2,10,1,1,4),_IDescription_Type())
iDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:iDescription.setStatus(_A)
class _IType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,128,129,130,131,132,133,134,135,136,137,138,139,192)));namedValues=NamedValues(*((_H,0),('v35',1),('eia530',2),('rs232',3),('voice',4),('hsdata',5),('dualt1dte',6),('dualddsv1',7),('hexdds',8),('ocudp',9),('x21',10),('dualddsv2',11),('rfdl',128),('alt',129),('t1dte',130),('didte',131),('t1ntw',132),('e1ntw',133),('ddsntw',134),('ddsdte',135),('ddsdbu',136),('fxs',137),('fxo',138),('eandm',139),('e1sig',192)))
_IType_Type.__name__=_C
_IType_Object=MibTableColumn
iType=_IType_Object((1,3,6,1,4,1,321,100,2,10,1,1,5),_IType_Type())
iType.setMaxAccess(_B)
if mibBuilder.loadTexts:iType.setStatus(_A)
_ISlot_Type=Integer32
_ISlot_Object=MibTableColumn
iSlot=_ISlot_Object((1,3,6,1,4,1,321,100,2,10,1,1,6),_ISlot_Type())
iSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:iSlot.setStatus(_A)
_IPort_Type=Integer32
_IPort_Object=MibTableColumn
iPort=_IPort_Object((1,3,6,1,4,1,321,100,2,10,1,1,7),_IPort_Type())
iPort.setMaxAccess(_B)
if mibBuilder.loadTexts:iPort.setStatus(_A)
class _IStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('iStatusOther',1),('iStatusOK',2),('iStatusErrored',3),('iStatusAlarmed',4),('iStatusTesting',5),('iStatusUnassigned',6),('iStatusLoopDetected',7)))
_IStatus_Type.__name__=_C
_IStatus_Object=MibTableColumn
iStatus=_IStatus_Object((1,3,6,1,4,1,321,100,2,10,1,1,8),_IStatus_Type())
iStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:iStatus.setStatus(_A)
_Traplog_ObjectIdentity=ObjectIdentity
traplog=_Traplog_ObjectIdentity((1,3,6,1,4,1,321,100,2,11))
_TraplogTable_Object=MibTable
traplogTable=_TraplogTable_Object((1,3,6,1,4,1,321,100,2,11,1))
if mibBuilder.loadTexts:traplogTable.setStatus(_A)
_TraplogEntry_Object=MibTableRow
traplogEntry=_TraplogEntry_Object((1,3,6,1,4,1,321,100,2,11,1,1))
traplogEntry.setIndexNames((0,_E,_AX))
if mibBuilder.loadTexts:traplogEntry.setStatus(_A)
_TraplogIndex_Type=Integer32
_TraplogIndex_Object=MibTableColumn
traplogIndex=_TraplogIndex_Object((1,3,6,1,4,1,321,100,2,11,1,1,1),_TraplogIndex_Type())
traplogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogIndex.setStatus(_A)
_TraplogNearIndex_Type=Integer32
_TraplogNearIndex_Object=MibTableColumn
traplogNearIndex=_TraplogNearIndex_Object((1,3,6,1,4,1,321,100,2,11,1,1,2),_TraplogNearIndex_Type())
traplogNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogNearIndex.setStatus(_A)
_TraplogFarIndex_Type=Integer32
_TraplogFarIndex_Object=MibTableColumn
traplogFarIndex=_TraplogFarIndex_Object((1,3,6,1,4,1,321,100,2,11,1,1,3),_TraplogFarIndex_Type())
traplogFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogFarIndex.setStatus(_A)
_TraplogInterfaceIndex_Type=Integer32
_TraplogInterfaceIndex_Object=MibTableColumn
traplogInterfaceIndex=_TraplogInterfaceIndex_Object((1,3,6,1,4,1,321,100,2,11,1,1,4),_TraplogInterfaceIndex_Type())
traplogInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogInterfaceIndex.setStatus(_A)
_TraplogTrapNum_Type=Integer32
_TraplogTrapNum_Object=MibTableColumn
traplogTrapNum=_TraplogTrapNum_Object((1,3,6,1,4,1,321,100,2,11,1,1,5),_TraplogTrapNum_Type())
traplogTrapNum.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogTrapNum.setStatus(_A)
class _TraplogTimeStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TraplogTimeStamp_Type.__name__=_F
_TraplogTimeStamp_Object=MibTableColumn
traplogTimeStamp=_TraplogTimeStamp_Object((1,3,6,1,4,1,321,100,2,11,1,1,6),_TraplogTimeStamp_Type())
traplogTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogTimeStamp.setStatus(_A)
class _TraplogDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*((_G,1),('none',2),('t12000',3),('e12048',4),('e13021',5),('t13000',6),('t13001',7),('t13002',8),('t13030',9),('t13060',10),('t13101',11),('t13102',12),('t13111',13),('t13112',14),('dds4001',15),('dds4101',16),('dds4051',17),('dds4151',18),('dds41TDM',19),('generic54016',20),('wanSuite',21)))
_TraplogDeviceType_Type.__name__=_C
_TraplogDeviceType_Object=MibTableColumn
traplogDeviceType=_TraplogDeviceType_Object((1,3,6,1,4,1,321,100,2,11,1,1,7),_TraplogDeviceType_Type())
traplogDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogDeviceType.setStatus(_A)
class _TraplogOID1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TraplogOID1_Type.__name__=_F
_TraplogOID1_Object=MibTableColumn
traplogOID1=_TraplogOID1_Object((1,3,6,1,4,1,321,100,2,11,1,1,8),_TraplogOID1_Type())
traplogOID1.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogOID1.setStatus(_A)
class _TraplogDescription1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TraplogDescription1_Type.__name__=_F
_TraplogDescription1_Object=MibTableColumn
traplogDescription1=_TraplogDescription1_Object((1,3,6,1,4,1,321,100,2,11,1,1,9),_TraplogDescription1_Type())
traplogDescription1.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogDescription1.setStatus(_A)
class _TraplogValue1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TraplogValue1_Type.__name__=_F
_TraplogValue1_Object=MibTableColumn
traplogValue1=_TraplogValue1_Object((1,3,6,1,4,1,321,100,2,11,1,1,10),_TraplogValue1_Type())
traplogValue1.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogValue1.setStatus(_A)
class _TraplogOID2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TraplogOID2_Type.__name__=_F
_TraplogOID2_Object=MibTableColumn
traplogOID2=_TraplogOID2_Object((1,3,6,1,4,1,321,100,2,11,1,1,11),_TraplogOID2_Type())
traplogOID2.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogOID2.setStatus(_A)
class _TraplogDescription2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TraplogDescription2_Type.__name__=_F
_TraplogDescription2_Object=MibTableColumn
traplogDescription2=_TraplogDescription2_Object((1,3,6,1,4,1,321,100,2,11,1,1,12),_TraplogDescription2_Type())
traplogDescription2.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogDescription2.setStatus(_A)
class _TraplogValue2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TraplogValue2_Type.__name__=_F
_TraplogValue2_Object=MibTableColumn
traplogValue2=_TraplogValue2_Object((1,3,6,1,4,1,321,100,2,11,1,1,13),_TraplogValue2_Type())
traplogValue2.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogValue2.setStatus(_A)
class _TraplogOID3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TraplogOID3_Type.__name__=_F
_TraplogOID3_Object=MibTableColumn
traplogOID3=_TraplogOID3_Object((1,3,6,1,4,1,321,100,2,11,1,1,14),_TraplogOID3_Type())
traplogOID3.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogOID3.setStatus(_A)
class _TraplogDescription3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TraplogDescription3_Type.__name__=_F
_TraplogDescription3_Object=MibTableColumn
traplogDescription3=_TraplogDescription3_Object((1,3,6,1,4,1,321,100,2,11,1,1,15),_TraplogDescription3_Type())
traplogDescription3.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogDescription3.setStatus(_A)
class _TraplogValue3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TraplogValue3_Type.__name__=_F
_TraplogValue3_Object=MibTableColumn
traplogValue3=_TraplogValue3_Object((1,3,6,1,4,1,321,100,2,11,1,1,16),_TraplogValue3_Type())
traplogValue3.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogValue3.setStatus(_A)
_TraplogDeleteEntry_Type=Integer32
_TraplogDeleteEntry_Object=MibScalar
traplogDeleteEntry=_TraplogDeleteEntry_Object((1,3,6,1,4,1,321,100,2,11,2),_TraplogDeleteEntry_Type())
traplogDeleteEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:traplogDeleteEntry.setStatus(_A)
class _TraplogSortOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('ascendingtimestamp',2),('ascendingunit',3)))
_TraplogSortOption_Type.__name__=_C
_TraplogSortOption_Object=MibScalar
traplogSortOption=_TraplogSortOption_Object((1,3,6,1,4,1,321,100,2,11,3),_TraplogSortOption_Type())
traplogSortOption.setMaxAccess(_D)
if mibBuilder.loadTexts:traplogSortOption.setStatus(_A)
_TraplogLastTimeStamp_Type=TimeTicks
_TraplogLastTimeStamp_Object=MibScalar
traplogLastTimeStamp=_TraplogLastTimeStamp_Object((1,3,6,1,4,1,321,100,2,11,4),_TraplogLastTimeStamp_Type())
traplogLastTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:traplogLastTimeStamp.setStatus(_A)
_UnitUtilities_ObjectIdentity=ObjectIdentity
unitUtilities=_UnitUtilities_ObjectIdentity((1,3,6,1,4,1,321,100,2,12))
_UnitUtilitiesTable_Object=MibTable
unitUtilitiesTable=_UnitUtilitiesTable_Object((1,3,6,1,4,1,321,100,2,12,1))
if mibBuilder.loadTexts:unitUtilitiesTable.setStatus(_A)
_UnitUtilitiesTableEntry_Object=MibTableRow
unitUtilitiesTableEntry=_UnitUtilitiesTableEntry_Object((1,3,6,1,4,1,321,100,2,12,1,1))
unitUtilitiesTableEntry.setIndexNames((0,_E,_AY),(0,_E,_AZ))
if mibBuilder.loadTexts:unitUtilitiesTableEntry.setStatus(_A)
_UnitUtilitiesNearIndex_Type=Integer32
_UnitUtilitiesNearIndex_Object=MibTableColumn
unitUtilitiesNearIndex=_UnitUtilitiesNearIndex_Object((1,3,6,1,4,1,321,100,2,12,1,1,1),_UnitUtilitiesNearIndex_Type())
unitUtilitiesNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:unitUtilitiesNearIndex.setStatus(_A)
_UnitUtilitiesFarIndex_Type=Integer32
_UnitUtilitiesFarIndex_Object=MibTableColumn
unitUtilitiesFarIndex=_UnitUtilitiesFarIndex_Object((1,3,6,1,4,1,321,100,2,12,1,1,2),_UnitUtilitiesFarIndex_Type())
unitUtilitiesFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:unitUtilitiesFarIndex.setStatus(_A)
_UnitUtilitiesLocalPassword_Type=DisplayString
_UnitUtilitiesLocalPassword_Object=MibTableColumn
unitUtilitiesLocalPassword=_UnitUtilitiesLocalPassword_Object((1,3,6,1,4,1,321,100,2,12,1,1,3),_UnitUtilitiesLocalPassword_Type())
unitUtilitiesLocalPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesLocalPassword.setStatus(_A)
class _UnitUtilitiesTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_UnitUtilitiesTime_Type.__name__=_F
_UnitUtilitiesTime_Object=MibTableColumn
unitUtilitiesTime=_UnitUtilitiesTime_Object((1,3,6,1,4,1,321,100,2,12,1,1,4),_UnitUtilitiesTime_Type())
unitUtilitiesTime.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesTime.setStatus(_A)
class _UnitUtilitiesDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_UnitUtilitiesDate_Type.__name__=_F
_UnitUtilitiesDate_Object=MibTableColumn
unitUtilitiesDate=_UnitUtilitiesDate_Object((1,3,6,1,4,1,321,100,2,12,1,1,5),_UnitUtilitiesDate_Type())
unitUtilitiesDate.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesDate.setStatus(_A)
class _UnitUtilitiesMaintenanceReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*((_G,1),('reset',2),('restart',3),('resetProfile1',4),('resetProfile2',5),('resetProfile3',6),('resetProfile4',7),('resetProfile5',8),('resetProfile6',9),('resetProfile7',10),('resetProfile8',11),('resetProfile9',12),('resetProfile10',13),('resetProfile11',14),('resetProfile12',15),('resetProfile13',16),('resetProfile14',17),('resetProfile15',18),('resetProfile16',19),('resetProfile17',20),('resetProfile18',21),('resetProfile19',22),('resetProfile20',23),('resetProfile21',24)))
_UnitUtilitiesMaintenanceReset_Type.__name__=_C
_UnitUtilitiesMaintenanceReset_Object=MibTableColumn
unitUtilitiesMaintenanceReset=_UnitUtilitiesMaintenanceReset_Object((1,3,6,1,4,1,321,100,2,12,1,1,6),_UnitUtilitiesMaintenanceReset_Type())
unitUtilitiesMaintenanceReset.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesMaintenanceReset.setStatus(_A)
_UnitUtilitiesAlarmResetTimer_Type=Integer32
_UnitUtilitiesAlarmResetTimer_Object=MibTableColumn
unitUtilitiesAlarmResetTimer=_UnitUtilitiesAlarmResetTimer_Object((1,3,6,1,4,1,321,100,2,12,1,1,7),_UnitUtilitiesAlarmResetTimer_Type())
unitUtilitiesAlarmResetTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesAlarmResetTimer.setStatus(_A)
class _UnitUtilitiesAlarmClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('utilitiesAlarmClearOther',1),('utilitiesAlarmClearNow',2)))
_UnitUtilitiesAlarmClear_Type.__name__=_C
_UnitUtilitiesAlarmClear_Object=MibTableColumn
unitUtilitiesAlarmClear=_UnitUtilitiesAlarmClear_Object((1,3,6,1,4,1,321,100,2,12,1,1,8),_UnitUtilitiesAlarmClear_Type())
unitUtilitiesAlarmClear.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesAlarmClear.setStatus(_A)
class _UnitUtilitiesSaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('saveConfig',2)))
_UnitUtilitiesSaveConfig_Type.__name__=_C
_UnitUtilitiesSaveConfig_Object=MibTableColumn
unitUtilitiesSaveConfig=_UnitUtilitiesSaveConfig_Object((1,3,6,1,4,1,321,100,2,12,1,1,9),_UnitUtilitiesSaveConfig_Type())
unitUtilitiesSaveConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesSaveConfig.setStatus(_A)
class _UnitUtilitiesRestartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('notNeeded',2),('recommended',3),('required',4)))
_UnitUtilitiesRestartStatus_Type.__name__=_C
_UnitUtilitiesRestartStatus_Object=MibTableColumn
unitUtilitiesRestartStatus=_UnitUtilitiesRestartStatus_Object((1,3,6,1,4,1,321,100,2,12,1,1,10),_UnitUtilitiesRestartStatus_Type())
unitUtilitiesRestartStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:unitUtilitiesRestartStatus.setStatus(_A)
_UnitUtilitiesReadOnlyPassword_Type=DisplayString
_UnitUtilitiesReadOnlyPassword_Object=MibTableColumn
unitUtilitiesReadOnlyPassword=_UnitUtilitiesReadOnlyPassword_Object((1,3,6,1,4,1,321,100,2,12,1,1,11),_UnitUtilitiesReadOnlyPassword_Type())
unitUtilitiesReadOnlyPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesReadOnlyPassword.setStatus(_A)
class _UnitUtilitiesPasswordLockoutEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_J,3)))
_UnitUtilitiesPasswordLockoutEnable_Type.__name__=_C
_UnitUtilitiesPasswordLockoutEnable_Object=MibTableColumn
unitUtilitiesPasswordLockoutEnable=_UnitUtilitiesPasswordLockoutEnable_Object((1,3,6,1,4,1,321,100,2,12,1,1,12),_UnitUtilitiesPasswordLockoutEnable_Type())
unitUtilitiesPasswordLockoutEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesPasswordLockoutEnable.setStatus(_A)
class _UnitUtilitiesPasswordLockoutStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_J,3),('locked',4)))
_UnitUtilitiesPasswordLockoutStatus_Type.__name__=_C
_UnitUtilitiesPasswordLockoutStatus_Object=MibTableColumn
unitUtilitiesPasswordLockoutStatus=_UnitUtilitiesPasswordLockoutStatus_Object((1,3,6,1,4,1,321,100,2,12,1,1,13),_UnitUtilitiesPasswordLockoutStatus_Type())
unitUtilitiesPasswordLockoutStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:unitUtilitiesPasswordLockoutStatus.setStatus(_A)
class _UnitUtilitiesPasswordLockoutClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('unlock',2)))
_UnitUtilitiesPasswordLockoutClear_Type.__name__=_C
_UnitUtilitiesPasswordLockoutClear_Object=MibTableColumn
unitUtilitiesPasswordLockoutClear=_UnitUtilitiesPasswordLockoutClear_Object((1,3,6,1,4,1,321,100,2,12,1,1,14),_UnitUtilitiesPasswordLockoutClear_Type())
unitUtilitiesPasswordLockoutClear.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUtilitiesPasswordLockoutClear.setStatus(_A)
_ProductInfo_ObjectIdentity=ObjectIdentity
productInfo=_ProductInfo_ObjectIdentity((1,3,6,1,4,1,321,100,2,13))
class _ProductModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ProductModelNumber_Type.__name__=_F
_ProductModelNumber_Object=MibScalar
productModelNumber=_ProductModelNumber_Object((1,3,6,1,4,1,321,100,2,13,1),_ProductModelNumber_Type())
productModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:productModelNumber.setStatus(_A)
class _ProductModelDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ProductModelDescr_Type.__name__=_F
_ProductModelDescr_Object=MibScalar
productModelDescr=_ProductModelDescr_Object((1,3,6,1,4,1,321,100,2,13,2),_ProductModelDescr_Type())
productModelDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:productModelDescr.setStatus(_A)
class _ProductElementId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ProductElementId_Type.__name__=_F
_ProductElementId_Object=MibScalar
productElementId=_ProductElementId_Object((1,3,6,1,4,1,321,100,2,13,3),_ProductElementId_Type())
productElementId.setMaxAccess(_D)
if mibBuilder.loadTexts:productElementId.setStatus(_A)
class _ProductSoftwareRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ProductSoftwareRev_Type.__name__=_F
_ProductSoftwareRev_Object=MibScalar
productSoftwareRev=_ProductSoftwareRev_Object((1,3,6,1,4,1,321,100,2,13,4),_ProductSoftwareRev_Type())
productSoftwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:productSoftwareRev.setStatus(_A)
class _ProductHardwareRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ProductHardwareRev_Type.__name__=_F
_ProductHardwareRev_Object=MibScalar
productHardwareRev=_ProductHardwareRev_Object((1,3,6,1,4,1,321,100,2,13,5),_ProductHardwareRev_Type())
productHardwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:productHardwareRev.setStatus(_A)
class _ProductSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ProductSerialNum_Type.__name__=_F
_ProductSerialNum_Object=MibScalar
productSerialNum=_ProductSerialNum_Object((1,3,6,1,4,1,321,100,2,13,6),_ProductSerialNum_Type())
productSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:productSerialNum.setStatus(_A)
class _ProductPhysicalAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ProductPhysicalAddress_Type.__name__=_F
_ProductPhysicalAddress_Object=MibScalar
productPhysicalAddress=_ProductPhysicalAddress_Object((1,3,6,1,4,1,321,100,2,13,7),_ProductPhysicalAddress_Type())
productPhysicalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:productPhysicalAddress.setStatus(_A)
class _ProductNmsAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ProductNmsAddress_Type.__name__=_F
_ProductNmsAddress_Object=MibScalar
productNmsAddress=_ProductNmsAddress_Object((1,3,6,1,4,1,321,100,2,13,8),_ProductNmsAddress_Type())
productNmsAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:productNmsAddress.setStatus(_A)
_ProductLabelTable_Object=MibTable
productLabelTable=_ProductLabelTable_Object((1,3,6,1,4,1,321,100,2,13,9))
if mibBuilder.loadTexts:productLabelTable.setStatus(_A)
_ProductLabelTableEntry_Object=MibTableRow
productLabelTableEntry=_ProductLabelTableEntry_Object((1,3,6,1,4,1,321,100,2,13,9,1))
productLabelTableEntry.setIndexNames((0,_E,_Aa))
if mibBuilder.loadTexts:productLabelTableEntry.setStatus(_A)
class _LabelTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_LabelTableIndex_Type.__name__=_C
_LabelTableIndex_Object=MibTableColumn
labelTableIndex=_LabelTableIndex_Object((1,3,6,1,4,1,321,100,2,13,9,1,1),_LabelTableIndex_Type())
labelTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:labelTableIndex.setStatus(_A)
class _LabelTableLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_LabelTableLabel_Type.__name__=_F
_LabelTableLabel_Object=MibTableColumn
labelTableLabel=_LabelTableLabel_Object((1,3,6,1,4,1,321,100,2,13,9,1,2),_LabelTableLabel_Type())
labelTableLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:labelTableLabel.setStatus(_A)
class _LabelTableValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_LabelTableValue_Type.__name__=_F
_LabelTableValue_Object=MibTableColumn
labelTableValue=_LabelTableValue_Object((1,3,6,1,4,1,321,100,2,13,9,1,3),_LabelTableValue_Type())
labelTableValue.setMaxAccess(_D)
if mibBuilder.loadTexts:labelTableValue.setStatus(_A)
_NetAPS_ObjectIdentity=ObjectIdentity
netAPS=_NetAPS_ObjectIdentity((1,3,6,1,4,1,321,100,2,14))
_NetAPSConfigTable_Object=MibTable
netAPSConfigTable=_NetAPSConfigTable_Object((1,3,6,1,4,1,321,100,2,14,1))
if mibBuilder.loadTexts:netAPSConfigTable.setStatus(_A)
_NetAPSConfigTableEntry_Object=MibTableRow
netAPSConfigTableEntry=_NetAPSConfigTableEntry_Object((1,3,6,1,4,1,321,100,2,14,1,1))
netAPSConfigTableEntry.setIndexNames((0,_E,_Ab),(0,_E,_Ac),(0,_E,_Ad))
if mibBuilder.loadTexts:netAPSConfigTableEntry.setStatus(_A)
_NetAPSConfigNearIndex_Type=Integer32
_NetAPSConfigNearIndex_Object=MibTableColumn
netAPSConfigNearIndex=_NetAPSConfigNearIndex_Object((1,3,6,1,4,1,321,100,2,14,1,1,1),_NetAPSConfigNearIndex_Type())
netAPSConfigNearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigNearIndex.setStatus(_A)
_NetAPSConfigFarIndex_Type=Integer32
_NetAPSConfigFarIndex_Object=MibTableColumn
netAPSConfigFarIndex=_NetAPSConfigFarIndex_Object((1,3,6,1,4,1,321,100,2,14,1,1,2),_NetAPSConfigFarIndex_Type())
netAPSConfigFarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigFarIndex.setStatus(_A)
_NetAPSConfigifIndex_Type=Integer32
_NetAPSConfigifIndex_Object=MibTableColumn
netAPSConfigifIndex=_NetAPSConfigifIndex_Object((1,3,6,1,4,1,321,100,2,14,1,1,3),_NetAPSConfigifIndex_Type())
netAPSConfigifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigifIndex.setStatus(_A)
_NetAPSConfigOtherifIndex_Type=Integer32
_NetAPSConfigOtherifIndex_Object=MibTableColumn
netAPSConfigOtherifIndex=_NetAPSConfigOtherifIndex_Object((1,3,6,1,4,1,321,100,2,14,1,1,4),_NetAPSConfigOtherifIndex_Type())
netAPSConfigOtherifIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:netAPSConfigOtherifIndex.setStatus(_A)
class _NetAPSConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('tr54017',2),('autoABswitch',3),('masterAltCarrier',4),('slaveAltCarrier',5)))
_NetAPSConfigMode_Type.__name__=_C
_NetAPSConfigMode_Object=MibTableColumn
netAPSConfigMode=_NetAPSConfigMode_Object((1,3,6,1,4,1,321,100,2,14,1,1,5),_NetAPSConfigMode_Type())
netAPSConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:netAPSConfigMode.setStatus(_A)
class _NetAPSConfigRevert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_J,3)))
_NetAPSConfigRevert_Type.__name__=_C
_NetAPSConfigRevert_Object=MibTableColumn
netAPSConfigRevert=_NetAPSConfigRevert_Object((1,3,6,1,4,1,321,100,2,14,1,1,6),_NetAPSConfigRevert_Type())
netAPSConfigRevert.setMaxAccess(_D)
if mibBuilder.loadTexts:netAPSConfigRevert.setStatus(_A)
class _NetAPSConfigManualInhibit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),('thisLine',3),('otherLine',4)))
_NetAPSConfigManualInhibit_Type.__name__=_C
_NetAPSConfigManualInhibit_Object=MibTableColumn
netAPSConfigManualInhibit=_NetAPSConfigManualInhibit_Object((1,3,6,1,4,1,321,100,2,14,1,1,7),_NetAPSConfigManualInhibit_Type())
netAPSConfigManualInhibit.setMaxAccess(_D)
if mibBuilder.loadTexts:netAPSConfigManualInhibit.setStatus(_A)
_NetAPSConfigAvailabilityTimer_Type=Integer32
_NetAPSConfigAvailabilityTimer_Object=MibTableColumn
netAPSConfigAvailabilityTimer=_NetAPSConfigAvailabilityTimer_Object((1,3,6,1,4,1,321,100,2,14,1,1,8),_NetAPSConfigAvailabilityTimer_Type())
netAPSConfigAvailabilityTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:netAPSConfigAvailabilityTimer.setStatus(_A)
_NetAPSConfigESThreshold_Type=Integer32
_NetAPSConfigESThreshold_Object=MibTableColumn
netAPSConfigESThreshold=_NetAPSConfigESThreshold_Object((1,3,6,1,4,1,321,100,2,14,1,1,9),_NetAPSConfigESThreshold_Type())
netAPSConfigESThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:netAPSConfigESThreshold.setStatus(_A)
_NetAPSConfigESCount_Type=Integer32
_NetAPSConfigESCount_Object=MibTableColumn
netAPSConfigESCount=_NetAPSConfigESCount_Object((1,3,6,1,4,1,321,100,2,14,1,1,10),_NetAPSConfigESCount_Type())
netAPSConfigESCount.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigESCount.setStatus(_A)
class _NetAPSConfigESSwitchEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('normal',2),(_Ae,3)))
_NetAPSConfigESSwitchEvent_Type.__name__=_C
_NetAPSConfigESSwitchEvent_Object=MibTableColumn
netAPSConfigESSwitchEvent=_NetAPSConfigESSwitchEvent_Object((1,3,6,1,4,1,321,100,2,14,1,1,11),_NetAPSConfigESSwitchEvent_Type())
netAPSConfigESSwitchEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigESSwitchEvent.setStatus(_A)
_NetAPSConfigCSESThreshold_Type=Integer32
_NetAPSConfigCSESThreshold_Object=MibTableColumn
netAPSConfigCSESThreshold=_NetAPSConfigCSESThreshold_Object((1,3,6,1,4,1,321,100,2,14,1,1,12),_NetAPSConfigCSESThreshold_Type())
netAPSConfigCSESThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:netAPSConfigCSESThreshold.setStatus(_A)
_NetAPSConfigCSESCount_Type=Integer32
_NetAPSConfigCSESCount_Object=MibTableColumn
netAPSConfigCSESCount=_NetAPSConfigCSESCount_Object((1,3,6,1,4,1,321,100,2,14,1,1,13),_NetAPSConfigCSESCount_Type())
netAPSConfigCSESCount.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigCSESCount.setStatus(_A)
class _NetAPSConfigCSESSwitchEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('normal',2),(_Ae,3)))
_NetAPSConfigCSESSwitchEvent_Type.__name__=_C
_NetAPSConfigCSESSwitchEvent_Object=MibTableColumn
netAPSConfigCSESSwitchEvent=_NetAPSConfigCSESSwitchEvent_Object((1,3,6,1,4,1,321,100,2,14,1,1,14),_NetAPSConfigCSESSwitchEvent_Type())
netAPSConfigCSESSwitchEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigCSESSwitchEvent.setStatus(_A)
_NetAPSConfigStatusBitmap_Type=Integer32
_NetAPSConfigStatusBitmap_Object=MibTableColumn
netAPSConfigStatusBitmap=_NetAPSConfigStatusBitmap_Object((1,3,6,1,4,1,321,100,2,14,1,1,15),_NetAPSConfigStatusBitmap_Type())
netAPSConfigStatusBitmap.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigStatusBitmap.setStatus(_A)
class _NetAPSConfigStatusString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_NetAPSConfigStatusString_Type.__name__=_F
_NetAPSConfigStatusString_Object=MibTableColumn
netAPSConfigStatusString=_NetAPSConfigStatusString_Object((1,3,6,1,4,1,321,100,2,14,1,1,16),_NetAPSConfigStatusString_Type())
netAPSConfigStatusString.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigStatusString.setStatus(_A)
_NetAPSConfigTimeInInterval_Type=Integer32
_NetAPSConfigTimeInInterval_Object=MibTableColumn
netAPSConfigTimeInInterval=_NetAPSConfigTimeInInterval_Object((1,3,6,1,4,1,321,100,2,14,1,1,17),_NetAPSConfigTimeInInterval_Type())
netAPSConfigTimeInInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigTimeInInterval.setStatus(_A)
_NetAPSConfigValidIntervals_Type=Integer32
_NetAPSConfigValidIntervals_Object=MibTableColumn
netAPSConfigValidIntervals=_NetAPSConfigValidIntervals_Object((1,3,6,1,4,1,321,100,2,14,1,1,18),_NetAPSConfigValidIntervals_Type())
netAPSConfigValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigValidIntervals.setStatus(_A)
_NetAPSConfigValidDays_Type=Integer32
_NetAPSConfigValidDays_Object=MibTableColumn
netAPSConfigValidDays=_NetAPSConfigValidDays_Object((1,3,6,1,4,1,321,100,2,14,1,1,19),_NetAPSConfigValidDays_Type())
netAPSConfigValidDays.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSConfigValidDays.setStatus(_A)
class _NetAPSConfigReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('clearAlarms',2),('clearHistory',3)))
_NetAPSConfigReset_Type.__name__=_C
_NetAPSConfigReset_Object=MibTableColumn
netAPSConfigReset=_NetAPSConfigReset_Object((1,3,6,1,4,1,321,100,2,14,1,1,20),_NetAPSConfigReset_Type())
netAPSConfigReset.setMaxAccess(_D)
if mibBuilder.loadTexts:netAPSConfigReset.setStatus(_A)
_NetAPSHist24Table_Object=MibTable
netAPSHist24Table=_NetAPSHist24Table_Object((1,3,6,1,4,1,321,100,2,14,2))
if mibBuilder.loadTexts:netAPSHist24Table.setStatus(_A)
_NetAPSHist24TableEntry_Object=MibTableRow
netAPSHist24TableEntry=_NetAPSHist24TableEntry_Object((1,3,6,1,4,1,321,100,2,14,2,1))
netAPSHist24TableEntry.setIndexNames((0,_E,_Af),(0,_E,_Ag),(0,_E,_Ah),(0,_E,_Ai))
if mibBuilder.loadTexts:netAPSHist24TableEntry.setStatus(_A)
_NetAPSHist24NearIndex_Type=Integer32
_NetAPSHist24NearIndex_Object=MibTableColumn
netAPSHist24NearIndex=_NetAPSHist24NearIndex_Object((1,3,6,1,4,1,321,100,2,14,2,1,1),_NetAPSHist24NearIndex_Type())
netAPSHist24NearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist24NearIndex.setStatus(_A)
_NetAPSHist24FarIndex_Type=Integer32
_NetAPSHist24FarIndex_Object=MibTableColumn
netAPSHist24FarIndex=_NetAPSHist24FarIndex_Object((1,3,6,1,4,1,321,100,2,14,2,1,2),_NetAPSHist24FarIndex_Type())
netAPSHist24FarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist24FarIndex.setStatus(_A)
_NetAPSHist24ifIndex_Type=Integer32
_NetAPSHist24ifIndex_Object=MibTableColumn
netAPSHist24ifIndex=_NetAPSHist24ifIndex_Object((1,3,6,1,4,1,321,100,2,14,2,1,3),_NetAPSHist24ifIndex_Type())
netAPSHist24ifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist24ifIndex.setStatus(_A)
class _NetAPSHist24Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98)));namedValues=NamedValues(*((_Aj,1),('statCurrent',2),('statPeriod1',3),('statPeriod2',4),('statPeriod3',5),('statPeriod4',6),('statPeriod5',7),('statPeriod6',8),('statPeriod7',9),('statPeriod8',10),('statPeriod9',11),('statPeriod10',12),('statPeriod11',13),('statPeriod12',14),('statPeriod13',15),('statPeriod14',16),('statPeriod15',17),('statPeriod16',18),('statPeriod17',19),('statPeriod18',20),('statPeriod19',21),('statPeriod20',22),('statPeriod21',23),('statPeriod22',24),('statPeriod23',25),('statPeriod24',26),('statPeriod25',27),('statPeriod26',28),('statPeriod27',29),('statPeriod28',30),('statPeriod29',31),('statPeriod30',32),('statPeriod31',33),('statPeriod32',34),('statPeriod33',35),('statPeriod34',36),('statPeriod35',37),('statPeriod36',38),('statPeriod37',39),('statPeriod38',40),('statPeriod39',41),('statPeriod40',42),('statPeriod41',43),('statPeriod42',44),('statPeriod43',45),('statPeriod44',46),('statPeriod45',47),('statPeriod46',48),('statPeriod47',49),('statPeriod48',50),('statPeriod49',51),('statPeriod50',52),('statPeriod51',53),('statPeriod52',54),('statPeriod53',55),('statPeriod54',56),('statPeriod55',57),('statPeriod56',58),('statPeriod57',59),('statPeriod58',60),('statPeriod59',61),('statPeriod60',62),('statPeriod61',63),('statPeriod62',64),('statPeriod63',65),('statPeriod64',66),('statPeriod65',67),('statPeriod66',68),('statPeriod67',69),('statPeriod68',70),('statPeriod69',71),('statPeriod70',72),('statPeriod71',73),('statPeriod72',74),('statPeriod73',75),('statPeriod74',76),('statPeriod75',77),('statPeriod76',78),('statPeriod77',79),('statPeriod78',80),('statPeriod79',81),('statPeriod80',82),('statPeriod81',83),('statPeriod82',84),('statPeriod83',85),('statPeriod84',86),('statPeriod85',87),('statPeriod86',88),('statPeriod87',89),('statPeriod88',90),('statPeriod89',91),('statPeriod90',92),('statPeriod91',93),('statPeriod92',94),('statPeriod93',95),('statPeriod94',96),('statPeriod95',97),('statPeriod96',98)))
_NetAPSHist24Index_Type.__name__=_C
_NetAPSHist24Index_Object=MibTableColumn
netAPSHist24Index=_NetAPSHist24Index_Object((1,3,6,1,4,1,321,100,2,14,2,1,4),_NetAPSHist24Index_Type())
netAPSHist24Index.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist24Index.setStatus(_A)
_NetAPSHist24Timestamp_Type=TimeTicks
_NetAPSHist24Timestamp_Object=MibTableColumn
netAPSHist24Timestamp=_NetAPSHist24Timestamp_Object((1,3,6,1,4,1,321,100,2,14,2,1,5),_NetAPSHist24Timestamp_Type())
netAPSHist24Timestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist24Timestamp.setStatus(_A)
_NetAPSHist24StatusBitmap_Type=Integer32
_NetAPSHist24StatusBitmap_Object=MibTableColumn
netAPSHist24StatusBitmap=_NetAPSHist24StatusBitmap_Object((1,3,6,1,4,1,321,100,2,14,2,1,6),_NetAPSHist24StatusBitmap_Type())
netAPSHist24StatusBitmap.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist24StatusBitmap.setStatus(_A)
class _NetAPSHist24StatusString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_NetAPSHist24StatusString_Type.__name__=_F
_NetAPSHist24StatusString_Object=MibTableColumn
netAPSHist24StatusString=_NetAPSHist24StatusString_Object((1,3,6,1,4,1,321,100,2,14,2,1,7),_NetAPSHist24StatusString_Type())
netAPSHist24StatusString.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist24StatusString.setStatus(_A)
_NetAPSHist24Occurrences_Type=Integer32
_NetAPSHist24Occurrences_Object=MibTableColumn
netAPSHist24Occurrences=_NetAPSHist24Occurrences_Object((1,3,6,1,4,1,321,100,2,14,2,1,8),_NetAPSHist24Occurrences_Type())
netAPSHist24Occurrences.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist24Occurrences.setStatus(_A)
_NetAPSHist24Duration_Type=Integer32
_NetAPSHist24Duration_Object=MibTableColumn
netAPSHist24Duration=_NetAPSHist24Duration_Object((1,3,6,1,4,1,321,100,2,14,2,1,9),_NetAPSHist24Duration_Type())
netAPSHist24Duration.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist24Duration.setStatus(_A)
_NetAPSHist30Table_Object=MibTable
netAPSHist30Table=_NetAPSHist30Table_Object((1,3,6,1,4,1,321,100,2,14,3))
if mibBuilder.loadTexts:netAPSHist30Table.setStatus(_A)
_NetAPSHist30TableEntry_Object=MibTableRow
netAPSHist30TableEntry=_NetAPSHist30TableEntry_Object((1,3,6,1,4,1,321,100,2,14,3,1))
netAPSHist30TableEntry.setIndexNames((0,_E,_Ak),(0,_E,_Al),(0,_E,_Am),(0,_E,_An))
if mibBuilder.loadTexts:netAPSHist30TableEntry.setStatus(_A)
_NetAPSHist30NearIndex_Type=Integer32
_NetAPSHist30NearIndex_Object=MibTableColumn
netAPSHist30NearIndex=_NetAPSHist30NearIndex_Object((1,3,6,1,4,1,321,100,2,14,3,1,1),_NetAPSHist30NearIndex_Type())
netAPSHist30NearIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist30NearIndex.setStatus(_A)
_NetAPSHist30FarIndex_Type=Integer32
_NetAPSHist30FarIndex_Object=MibTableColumn
netAPSHist30FarIndex=_NetAPSHist30FarIndex_Object((1,3,6,1,4,1,321,100,2,14,3,1,2),_NetAPSHist30FarIndex_Type())
netAPSHist30FarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist30FarIndex.setStatus(_A)
_NetAPSHist30ifIndex_Type=Integer32
_NetAPSHist30ifIndex_Object=MibTableColumn
netAPSHist30ifIndex=_NetAPSHist30ifIndex_Object((1,3,6,1,4,1,321,100,2,14,3,1,3),_NetAPSHist30ifIndex_Type())
netAPSHist30ifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist30ifIndex.setStatus(_A)
class _NetAPSHist30Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*((_Aj,1),('statDay1',2),('statDay2',3),('statDay3',4),('statDay4',5),('statDay5',6),('statDay6',7),('statDay7',8),('statDay8',9),('statDay9',10),('statDay10',11),('statDay11',12),('statDay12',13),('statDay13',14),('statDay14',15),('statDay15',16),('statDay16',17),('statDay17',18),('statDay18',19),('statDay19',20),('statDay20',21),('statDay21',22),('statDay22',23),('statDay23',24),('statDay24',25),('statDay25',26),('statDay26',27),('statDay27',28),('statDay28',29),('statDay29',30),('statDay30',31)))
_NetAPSHist30Index_Type.__name__=_C
_NetAPSHist30Index_Object=MibTableColumn
netAPSHist30Index=_NetAPSHist30Index_Object((1,3,6,1,4,1,321,100,2,14,3,1,4),_NetAPSHist30Index_Type())
netAPSHist30Index.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist30Index.setStatus(_A)
_NetAPSHist30Timestamp_Type=TimeTicks
_NetAPSHist30Timestamp_Object=MibTableColumn
netAPSHist30Timestamp=_NetAPSHist30Timestamp_Object((1,3,6,1,4,1,321,100,2,14,3,1,5),_NetAPSHist30Timestamp_Type())
netAPSHist30Timestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist30Timestamp.setStatus(_A)
_NetAPSHist30StatusBitmap_Type=Integer32
_NetAPSHist30StatusBitmap_Object=MibTableColumn
netAPSHist30StatusBitmap=_NetAPSHist30StatusBitmap_Object((1,3,6,1,4,1,321,100,2,14,3,1,6),_NetAPSHist30StatusBitmap_Type())
netAPSHist30StatusBitmap.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist30StatusBitmap.setStatus(_A)
class _NetAPSHist30StatusString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_NetAPSHist30StatusString_Type.__name__=_F
_NetAPSHist30StatusString_Object=MibTableColumn
netAPSHist30StatusString=_NetAPSHist30StatusString_Object((1,3,6,1,4,1,321,100,2,14,3,1,7),_NetAPSHist30StatusString_Type())
netAPSHist30StatusString.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist30StatusString.setStatus(_A)
_NetAPSHist30Occurrences_Type=Integer32
_NetAPSHist30Occurrences_Object=MibTableColumn
netAPSHist30Occurrences=_NetAPSHist30Occurrences_Object((1,3,6,1,4,1,321,100,2,14,3,1,8),_NetAPSHist30Occurrences_Type())
netAPSHist30Occurrences.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist30Occurrences.setStatus(_A)
_NetAPSHist30Duration_Type=Integer32
_NetAPSHist30Duration_Object=MibTableColumn
netAPSHist30Duration=_NetAPSHist30Duration_Object((1,3,6,1,4,1,321,100,2,14,3,1,9),_NetAPSHist30Duration_Type())
netAPSHist30Duration.setMaxAccess(_B)
if mibBuilder.loadTexts:netAPSHist30Duration.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'tinterfaces':tinterfaces,'mgmtPorts':mgmtPorts,'mgmtPortsTable':mgmtPortsTable,'mgmtPortsTableEntry':mgmtPortsTableEntry,_L:mgmtPortsTableIndex,'mgmtPortsDescription':mgmtPortsDescription,'mgmtPortsElementID':mgmtPortsElementID,'mgmtPortsMode':mgmtPortsMode,'mgmtPortsDialPrefix':mgmtPortsDialPrefix,'mgmtPortsPrimaryDialString':mgmtPortsPrimaryDialString,'mgmtPortsSecondaryDialString':mgmtPortsSecondaryDialString,'mgmtPortsExtInitString':mgmtPortsExtInitString,'mgmtPortsCompressedSlip':mgmtPortsCompressedSlip,'mgmtPortsInternalModem':mgmtPortsInternalModem,'dbu':dbu,'dbuConfigTable':dbuConfigTable,'dbuConfigTableEntry':dbuConfigTableEntry,_M:dbuNearIndex,_N:dbuFarIndex,_O:dbuConfigTableIndex,'dbuDescription':dbuDescription,'dbuRate':dbuRate,'dbuMode':dbuMode,'dbuFormat':dbuFormat,'dbuNumber':dbuNumber,'dbuStatus':dbuStatus,'dbuCommand':dbuCommand,'dbuActivator1':dbuActivator1,'dbuActivator2':dbuActivator2,'dbuDialStr':dbuDialStr,'dbuInitStr':dbuInitStr,'dbuHangupStr':dbuHangupStr,'dbuPasswordStr':dbuPasswordStr,'dbuSecurity':dbuSecurity,'dbuDtrDial':dbuDtrDial,'dbuISDNSwitchType':dbuISDNSwitchType,'dbuISDNSwitchVersion':dbuISDNSwitchVersion,'dbuISDNTEI':dbuISDNTEI,'dbuISDNSPID':dbuISDNSPID,'dbuISDNDDNUM':dbuISDNDDNUM,'dbuResetStringsTable':dbuResetStringsTable,'dbuResetStringsEntry':dbuResetStringsEntry,_b:dbuResetNearIndex,_c:dbuResetFarIndex,_d:dbuResetConfigEntryIndex,_e:dbuResetStringsIndex,'dbuResetString':dbuResetString,'dbuStartStopTable':dbuStartStopTable,'dbuStartStopTableEntry':dbuStartStopTableEntry,_f:dbuStartStopNearIndex,_g:dbuStartStopFarIndex,_h:dbuStartStopConfigEntryIndex,_i:dbuStartStopDayOfWeek,'dbuStart':dbuStart,'dbuStop':dbuStop,'t1e1':t1e1,'t1e1ConfigTable':t1e1ConfigTable,'t1e1ConfigTableEntry':t1e1ConfigTableEntry,_j:t1e1ConfigNearIndex,_k:t1e1ConfigFarIndex,_l:t1e1ConfigIndex,'t1e1Description':t1e1Description,'t1e1Mode':t1e1Mode,'t1e1FrameType':t1e1FrameType,'t1e1LineCode':t1e1LineCode,'t1e1LineBuildOut':t1e1LineBuildOut,'t1e1Timing':t1e1Timing,'t1e1StationInTiming':t1e1StationInTiming,'t1e1StationTiming':t1e1StationTiming,'t1e1PRM':t1e1PRM,'t1e1ZeroSuppress':t1e1ZeroSuppress,'t1e1NationalBit':t1e1NationalBit,'t1e1KeepAlive':t1e1KeepAlive,'t1e1CRC4Mode':t1e1CRC4Mode,'t1e1DSXLevel':t1e1DSXLevel,'t1e1CRC':t1e1CRC,'t1e1FDLPassThrough':t1e1FDLPassThrough,'t1e1AudibleAlarm':t1e1AudibleAlarm,'t1e1Function':t1e1Function,'t1e1EBitGeneration':t1e1EBitGeneration,'t1e1RAIGeneration':t1e1RAIGeneration,'t1e1SpareBitInsertion':t1e1SpareBitInsertion,'t1e1Sa4In':t1e1Sa4In,'t1e1Sa5In':t1e1Sa5In,'t1e1Sa6In':t1e1Sa6In,'t1e1Sa7In':t1e1Sa7In,'t1e1Sa8In':t1e1Sa8In,'t1e1Sa4Out':t1e1Sa4Out,'t1e1Sa5Out':t1e1Sa5Out,'t1e1Sa6Out':t1e1Sa6Out,'t1e1Sa7Out':t1e1Sa7Out,'t1e1Sa8Out':t1e1Sa8Out,'t1e1AlarmTable':t1e1AlarmTable,'t1e1AlarmTableEntry':t1e1AlarmTableEntry,_m:t1e1AlarmNearIndex,_n:t1e1AlarmFarIndex,_o:t1e1AlarmIndex,'t1e1StatusSummary':t1e1StatusSummary,'t1e1AlarmSummary':t1e1AlarmSummary,'t1e1ESStatus':t1e1ESStatus,'t1e1ESCount':t1e1ESCount,'t1e1ESThreshold':t1e1ESThreshold,'t1e1ESAlarm':t1e1ESAlarm,'t1e1SESStatus':t1e1SESStatus,'t1e1SESCount':t1e1SESCount,'t1e1SESThreshold':t1e1SESThreshold,'t1e1SESAlarm':t1e1SESAlarm,'t1e1LOSSStatus':t1e1LOSSStatus,'t1e1LOSSCount':t1e1LOSSCount,'t1e1LOSSThreshold':t1e1LOSSThreshold,'t1e1LOSSAlarm':t1e1LOSSAlarm,'t1e1UASStatus':t1e1UASStatus,'t1e1UASCount':t1e1UASCount,'t1e1UASThreshold':t1e1UASThreshold,'t1e1UASAlarm':t1e1UASAlarm,'t1e1CSSStatus':t1e1CSSStatus,'t1e1CSSCount':t1e1CSSCount,'t1e1CSSThreshold':t1e1CSSThreshold,'t1e1CSSAlarm':t1e1CSSAlarm,'t1e1BPVSStatus':t1e1BPVSStatus,'t1e1BPVSCount':t1e1BPVSCount,'t1e1BPVSThreshold':t1e1BPVSThreshold,'t1e1BPVSAlarm':t1e1BPVSAlarm,'t1e1OOFSStatus':t1e1OOFSStatus,'t1e1OOFSCount':t1e1OOFSCount,'t1e1OOFSThreshold':t1e1OOFSThreshold,'t1e1OOFSAlarm':t1e1OOFSAlarm,'t1e1AISStatus':t1e1AISStatus,'t1e1AISCount':t1e1AISCount,'t1e1AISThreshold':t1e1AISThreshold,'t1e1AISAlarm':t1e1AISAlarm,'t1e1RASStatus':t1e1RASStatus,'t1e1RASCount':t1e1RASCount,'t1e1RASThreshold':t1e1RASThreshold,'t1e1RASAlarm':t1e1RASAlarm,'t1e1AlarmResetTimer':t1e1AlarmResetTimer,'t1e1AlarmReset':t1e1AlarmReset,'ddsNet':ddsNet,'ddsNetConfigTable':ddsNetConfigTable,'ddsNetConfigTableEntry':ddsNetConfigTableEntry,_p:ddsNetConfigNearIndex,_q:ddsNetConfigFarIndex,_r:ddsNetConfigIndex,'ddsNetDescription':ddsNetDescription,'ddsNetRate':ddsNetRate,'ddsNetMode':ddsNetMode,'ddsNetTimingSource':ddsNetTimingSource,'ddsNetRemComm':ddsNetRemComm,'ddsNetCircuitAssur':ddsNetCircuitAssur,'ddsNetAntiStrTimer':ddsNetAntiStrTimer,'ddsNetAlarmTable':ddsNetAlarmTable,'ddsNetAlarmTableEntry':ddsNetAlarmTableEntry,_s:ddsNetAlarmNearIndex,_t:ddsNetAlarmFarIndex,_u:ddsNetAlarmIndex,'ddsNetStatusSummary':ddsNetStatusSummary,'ddsNetAlarmSummary':ddsNetAlarmSummary,'ddsNetLOSStatus':ddsNetLOSStatus,'ddsNetLOSCount':ddsNetLOSCount,'ddsNetLOSThreshold':ddsNetLOSThreshold,'ddsNetLOSAlarm':ddsNetLOSAlarm,'ddsNetOOFStatus':ddsNetOOFStatus,'ddsNetOOFCount':ddsNetOOFCount,'ddsNetOOFThreshold':ddsNetOOFThreshold,'ddsNetOOFAlarm':ddsNetOOFAlarm,'ddsNetOOSStatus':ddsNetOOSStatus,'ddsNetOOSCount':ddsNetOOSCount,'ddsNetOOSThreshold':ddsNetOOSThreshold,'ddsNetOOSAlarm':ddsNetOOSAlarm,'ddsNetFDLStatus':ddsNetFDLStatus,'ddsNetFDLCount':ddsNetFDLCount,'ddsNetFDLThreshold':ddsNetFDLThreshold,'ddsNetFDLAlarm':ddsNetFDLAlarm,'ddsNetAlarmResetTimer':ddsNetAlarmResetTimer,'ddsNetAlarmReset':ddsNetAlarmReset,'ddsNetBPVStatus':ddsNetBPVStatus,'ddsNetBPVCount':ddsNetBPVCount,'ddsNetBPVThreshold':ddsNetBPVThreshold,'ddsNetBPVAlarm':ddsNetBPVAlarm,'serialDte':serialDte,'serialDteConfigTable':serialDteConfigTable,'serialDteConfigTableEntry':serialDteConfigTableEntry,_v:serialDteConfigNearIndex,_w:serialDteConfigFarIndex,_x:serialDteConfigIndex,'serialDteDescription':serialDteDescription,'serialDteType':serialDteType,'serialDteRate':serialDteRate,'serialDteInvertData':serialDteInvertData,'serialDteFormat':serialDteFormat,'serialDteParity':serialDteParity,'serialDteStopBit':serialDteStopBit,'serialDteMode':serialDteMode,'serialDteDSR':serialDteDSR,'serialDteDCD':serialDteDCD,'serialDteRTS':serialDteRTS,'serialDteRTSDelay':serialDteRTSDelay,'serialDteDTR':serialDteDTR,'serialDteCTS':serialDteCTS,'serialDteV54':serialDteV54,'serialDteLL':serialDteLL,'serialDteRL':serialDteRL,'serialDteStartChannel':serialDteStartChannel,'serialDteNumberOfChannels':serialDteNumberOfChannels,'serialDteTxClock':serialDteTxClock,'serialDteBundle':serialDteBundle,'serialDteChannelRate':serialDteChannelRate,'serialDteInvertClock':serialDteInvertClock,'serialDteCharSize':serialDteCharSize,'serialDteFlowControl':serialDteFlowControl,'serialDtePinStatus':serialDtePinStatus,'serialDteInInvertClock':serialDteInInvertClock,'serialDteAlarmTable':serialDteAlarmTable,'serialDteAlarmTableEntry':serialDteAlarmTableEntry,_y:serialDteAlarmNearIndex,_z:serialDteAlarmFarIndex,_A0:serialDteAlarmIndex,'serialDteDTRAlarmControl':serialDteDTRAlarmControl,'serialDteDTRAlarmStatus':serialDteDTRAlarmStatus,'serialDteStatusSummary':serialDteStatusSummary,'serialDteAlarmSummary':serialDteAlarmSummary,'serialDteASCStatus':serialDteASCStatus,'serialDteASCCount':serialDteASCCount,'serialDteASCThreshold':serialDteASCThreshold,'serialDteASCAlarm':serialDteASCAlarm,'serialDteFDLStatus':serialDteFDLStatus,'serialDteFDLCount':serialDteFDLCount,'serialDteFDLThreshold':serialDteFDLThreshold,'serialDteFDLAlarm':serialDteFDLAlarm,'serialDteLOSStatus':serialDteLOSStatus,'serialDteLOSCount':serialDteLOSCount,'serialDteLOSThreshold':serialDteLOSThreshold,'serialDteLOSAlarm':serialDteLOSAlarm,'analogDte':analogDte,'analogDteTable':analogDteTable,'analogDteTableEntry':analogDteTableEntry,_A2:analogDteNearIndex,_A3:analogDteFarIndex,_A4:analogDteIndex,'analogDteDescription':analogDteDescription,'analogDteCardType':analogDteCardType,'analogDteMode':analogDteMode,'analogDteState':analogDteState,'analogDteElementID':analogDteElementID,'analogDteSignalling':analogDteSignalling,'analogDteDNISDelay':analogDteDNISDelay,'analogDteTxGain':analogDteTxGain,'analogDteRxGain':analogDteRxGain,'connection':connection,'connectionTable':connectionTable,'connectionTableEntry':connectionTableEntry,_A5:connectionNearIndex,_A6:connectionFarIndex,_A7:connectionTableIndex,'connectionTableDescription':connectionTableDescription,'connectionChannelTable':connectionChannelTable,'connectionChannelEntry':connectionChannelEntry,_A8:connectionChannelNearIndex,_A9:connectionChannelFarIndex,_AA:connectionChannelLineIndex,_AB:connectionChannelIndex,'channelInterfaceAssignment':channelInterfaceAssignment,'channelInterfaceDescription':channelInterfaceDescription,'channelInterfaceChannel':channelInterfaceChannel,'channelSignalling':channelSignalling,'maintenance':maintenance,'bertTable':bertTable,'bertTableEntry':bertTableEntry,_AC:bertNearIndex,_AD:bertFarIndex,_AE:bertIndex,'bertPattern':bertPattern,'bertLength':bertLength,'bertPatternSync':bertPatternSync,'bertElapsedTime':bertElapsedTime,'bertBitErrors':bertBitErrors,'bertErroredSeconds':bertErroredSeconds,'bertPercentEFS':bertPercentEFS,'bertCommand':bertCommand,'bertInterfaceTable':bertInterfaceTable,'bertInterfaceTableEntry':bertInterfaceTableEntry,_AF:bertInterfaceNearIndex,_AG:bertInterfaceFarIndex,_AH:bertChipIndex,_AI:bertInterfaceIndex,'bertInterfaceSetting':bertInterfaceSetting,'bertInterfaceService':bertInterfaceService,'bertInterfaceChannelRate':bertInterfaceChannelRate,'testTable':testTable,'testTableEntry':testTableEntry,_AJ:testNearIndex,_AK:testFarIndex,_AL:testTableIndex,'testType':testType,'testLoopDirection':testLoopDirection,'testFarLLBFraming':testFarLLBFraming,'testLoopInitiator':testLoopInitiator,'testDefaultLoopType':testDefaultLoopType,'performance':performance,'performance24Table':performance24Table,'performance24TableEntry':performance24TableEntry,_AM:performance24NearIndex,_AN:performance24FarIndex,_AO:performance24InterfaceIndex,_AP:performance24Index,'performance24ES':performance24ES,'performance24BES':performance24BES,'performance24SES':performance24SES,'performance24UAS':performance24UAS,'performance24LOFC':performance24LOFC,'performance24CSS':performance24CSS,'performance24CRCES':performance24CRCES,'performance24OOFS':performance24OOFS,'performance24LOSS':performance24LOSS,'performance24AISS':performance24AISS,'performance24RAS':performance24RAS,'performance24BPVS':performance24BPVS,'performance24timestamp':performance24timestamp,'performance30Table':performance30Table,'performance30TableEntry':performance30TableEntry,_AQ:performance30NearIndex,_AR:performance30FarIndex,_AS:performance30InterfaceIndex,_AT:performance30Index,'performance30ES':performance30ES,'performance30BES':performance30BES,'performance30SES':performance30SES,'performance30UAS':performance30UAS,'performance30LOFC':performance30LOFC,'performance30CSS':performance30CSS,'performance30CRCES':performance30CRCES,'performance30OOFS':performance30OOFS,'performance30LOSS':performance30LOSS,'performance30AISS':performance30AISS,'performance30RAS':performance30RAS,'performance30BPVS':performance30BPVS,'performance30timestamp':performance30timestamp,'itable':itable,'iTable':iTable,'iTableEntry':iTableEntry,_AU:iTableNearIndex,_AV:iTableFarIndex,_AW:iTableIndex,'iDescription':iDescription,'iType':iType,'iSlot':iSlot,'iPort':iPort,'iStatus':iStatus,'traplog':traplog,'traplogTable':traplogTable,'traplogEntry':traplogEntry,_AX:traplogIndex,'traplogNearIndex':traplogNearIndex,'traplogFarIndex':traplogFarIndex,'traplogInterfaceIndex':traplogInterfaceIndex,'traplogTrapNum':traplogTrapNum,'traplogTimeStamp':traplogTimeStamp,'traplogDeviceType':traplogDeviceType,'traplogOID1':traplogOID1,'traplogDescription1':traplogDescription1,'traplogValue1':traplogValue1,'traplogOID2':traplogOID2,'traplogDescription2':traplogDescription2,'traplogValue2':traplogValue2,'traplogOID3':traplogOID3,'traplogDescription3':traplogDescription3,'traplogValue3':traplogValue3,'traplogDeleteEntry':traplogDeleteEntry,'traplogSortOption':traplogSortOption,'traplogLastTimeStamp':traplogLastTimeStamp,'unitUtilities':unitUtilities,'unitUtilitiesTable':unitUtilitiesTable,'unitUtilitiesTableEntry':unitUtilitiesTableEntry,_AY:unitUtilitiesNearIndex,_AZ:unitUtilitiesFarIndex,'unitUtilitiesLocalPassword':unitUtilitiesLocalPassword,'unitUtilitiesTime':unitUtilitiesTime,'unitUtilitiesDate':unitUtilitiesDate,'unitUtilitiesMaintenanceReset':unitUtilitiesMaintenanceReset,'unitUtilitiesAlarmResetTimer':unitUtilitiesAlarmResetTimer,'unitUtilitiesAlarmClear':unitUtilitiesAlarmClear,'unitUtilitiesSaveConfig':unitUtilitiesSaveConfig,'unitUtilitiesRestartStatus':unitUtilitiesRestartStatus,'unitUtilitiesReadOnlyPassword':unitUtilitiesReadOnlyPassword,'unitUtilitiesPasswordLockoutEnable':unitUtilitiesPasswordLockoutEnable,'unitUtilitiesPasswordLockoutStatus':unitUtilitiesPasswordLockoutStatus,'unitUtilitiesPasswordLockoutClear':unitUtilitiesPasswordLockoutClear,'productInfo':productInfo,'productModelNumber':productModelNumber,'productModelDescr':productModelDescr,'productElementId':productElementId,'productSoftwareRev':productSoftwareRev,'productHardwareRev':productHardwareRev,'productSerialNum':productSerialNum,'productPhysicalAddress':productPhysicalAddress,'productNmsAddress':productNmsAddress,'productLabelTable':productLabelTable,'productLabelTableEntry':productLabelTableEntry,_Aa:labelTableIndex,'labelTableLabel':labelTableLabel,'labelTableValue':labelTableValue,'netAPS':netAPS,'netAPSConfigTable':netAPSConfigTable,'netAPSConfigTableEntry':netAPSConfigTableEntry,_Ab:netAPSConfigNearIndex,_Ac:netAPSConfigFarIndex,_Ad:netAPSConfigifIndex,'netAPSConfigOtherifIndex':netAPSConfigOtherifIndex,'netAPSConfigMode':netAPSConfigMode,'netAPSConfigRevert':netAPSConfigRevert,'netAPSConfigManualInhibit':netAPSConfigManualInhibit,'netAPSConfigAvailabilityTimer':netAPSConfigAvailabilityTimer,'netAPSConfigESThreshold':netAPSConfigESThreshold,'netAPSConfigESCount':netAPSConfigESCount,'netAPSConfigESSwitchEvent':netAPSConfigESSwitchEvent,'netAPSConfigCSESThreshold':netAPSConfigCSESThreshold,'netAPSConfigCSESCount':netAPSConfigCSESCount,'netAPSConfigCSESSwitchEvent':netAPSConfigCSESSwitchEvent,'netAPSConfigStatusBitmap':netAPSConfigStatusBitmap,'netAPSConfigStatusString':netAPSConfigStatusString,'netAPSConfigTimeInInterval':netAPSConfigTimeInInterval,'netAPSConfigValidIntervals':netAPSConfigValidIntervals,'netAPSConfigValidDays':netAPSConfigValidDays,'netAPSConfigReset':netAPSConfigReset,'netAPSHist24Table':netAPSHist24Table,'netAPSHist24TableEntry':netAPSHist24TableEntry,_Af:netAPSHist24NearIndex,_Ag:netAPSHist24FarIndex,_Ah:netAPSHist24ifIndex,_Ai:netAPSHist24Index,'netAPSHist24Timestamp':netAPSHist24Timestamp,'netAPSHist24StatusBitmap':netAPSHist24StatusBitmap,'netAPSHist24StatusString':netAPSHist24StatusString,'netAPSHist24Occurrences':netAPSHist24Occurrences,'netAPSHist24Duration':netAPSHist24Duration,'netAPSHist30Table':netAPSHist30Table,'netAPSHist30TableEntry':netAPSHist30TableEntry,_Ak:netAPSHist30NearIndex,_Al:netAPSHist30FarIndex,_Am:netAPSHist30ifIndex,_An:netAPSHist30Index,'netAPSHist30Timestamp':netAPSHist30Timestamp,'netAPSHist30StatusBitmap':netAPSHist30StatusBitmap,'netAPSHist30StatusString':netAPSHist30StatusString,'netAPSHist30Occurrences':netAPSHist30Occurrences,'netAPSHist30Duration':netAPSHist30Duration})