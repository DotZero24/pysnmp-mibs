_o='igRowStatus'
_n='igCrvTmcState'
_m='igCrvOperStatus'
_l='igCrvRemoteAdminState'
_k='igCrvLocalAdminState'
_j='igControlChannelEocSecondarySvcState'
_i='igControlChannelEocPrimarySvcState'
_h='igControlChannelTmcSecondarySvcState'
_g='igControlChannelTmcPrimarySvcState'
_f='igOperationalStatus'
_e='igAdminStatus'
_d='igStatsTotalEntry'
_c='igStatsCurrentEntry'
_b='igControlChannelEntry'
_a='ds1ChannelNumber'
_Z='dsnLgId'
_Y='igIntervalNumber'
_X='notApplicable'
_W='notInhibited'
_V='inhibit'
_U='intervals'
_T='zhoneSystemConfigurationDateAndTime'
_S='ZHONE-SYSTEM-MIB'
_R='TruthValue'
_Q='errors'
_P='seconds'
_O='Gauge32'
_N='milliseconds'
_M='inService'
_L='active'
_K='standby'
_J='not-accessible'
_I='igNameId'
_H='outOfService'
_G='calls'
_F='frames'
_E='read-create'
_D='ZhoneGR303-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
PerfCurrentCount,=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_O,_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_R)
zhoneSystemConfigurationDateAndTime,=mibBuilder.importSymbols(_S,_T)
zhoneVoice,=mibBuilder.importSymbols('Zhone','zhoneVoice')
ZhoneAdminString,ZhoneRowStatus,ZhoneShelfValueOrZero,ZhoneSlotValueOrZero=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString','ZhoneRowStatus','ZhoneShelfValueOrZero','ZhoneSlotValueOrZero')
zhoneGR303=ModuleIdentity((1,3,6,1,4,1,5504,4,3,1))
if mibBuilder.loadTexts:zhoneGR303.setRevisions(('2003-12-23 11:09','2003-11-14 13:10','2001-11-15 10:45','2001-08-31 12:30','2001-08-14 14:47','2001-06-26 15:00','2001-03-28 10:55','2001-02-15 18:47','2001-02-01 13:01','2001-01-26 11:48','2000-12-12 11:57','2000-09-12 12:12'))
_InterfaceGroupTable_Object=MibTable
interfaceGroupTable=_InterfaceGroupTable_Object((1,3,6,1,4,1,5504,4,3,1,1))
if mibBuilder.loadTexts:interfaceGroupTable.setStatus(_A)
_InterfaceGroupEntry_Object=MibTableRow
interfaceGroupEntry=_InterfaceGroupEntry_Object((1,3,6,1,4,1,5504,4,3,1,1,1))
interfaceGroupEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:interfaceGroupEntry.setStatus(_A)
_IgNameId_Type=ZhoneAdminString
_IgNameId_Object=MibTableColumn
igNameId=_IgNameId_Object((1,3,6,1,4,1,5504,4,3,1,1,1,1),_IgNameId_Type())
igNameId.setMaxAccess(_J)
if mibBuilder.loadTexts:igNameId.setStatus(_A)
_IgShelf_Type=ZhoneShelfValueOrZero
_IgShelf_Object=MibTableColumn
igShelf=_IgShelf_Object((1,3,6,1,4,1,5504,4,3,1,1,1,2),_IgShelf_Type())
igShelf.setMaxAccess(_B)
if mibBuilder.loadTexts:igShelf.setStatus(_A)
_IgSlot_Type=ZhoneSlotValueOrZero
_IgSlot_Object=MibTableColumn
igSlot=_IgSlot_Object((1,3,6,1,4,1,5504,4,3,1,1,1,3),_IgSlot_Type())
igSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:igSlot.setStatus(_A)
_IgPeerShelf_Type=ZhoneShelfValueOrZero
_IgPeerShelf_Object=MibTableColumn
igPeerShelf=_IgPeerShelf_Object((1,3,6,1,4,1,5504,4,3,1,1,1,4),_IgPeerShelf_Type())
igPeerShelf.setMaxAccess(_B)
if mibBuilder.loadTexts:igPeerShelf.setStatus(_A)
_IgPeerSlot_Type=ZhoneSlotValueOrZero
_IgPeerSlot_Object=MibTableColumn
igPeerSlot=_IgPeerSlot_Object((1,3,6,1,4,1,5504,4,3,1,1,1,5),_IgPeerSlot_Type())
igPeerSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:igPeerSlot.setStatus(_A)
class _IgSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*(('lucent5Ess',2),('nortelDms100',3),('lucentGtd5',4),('santeraSanteraOne',5),('telicaPlexus9000',6),('taquaIx7000',7)))
_IgSwitchType_Type.__name__=_C
_IgSwitchType_Object=MibTableColumn
igSwitchType=_IgSwitchType_Object((1,3,6,1,4,1,5504,4,3,1,1,1,6),_IgSwitchType_Type())
igSwitchType.setMaxAccess(_E)
if mibBuilder.loadTexts:igSwitchType.setStatus(_A)
_IgPrimaryEocTmcDs1IfIndex_Type=InterfaceIndexOrZero
_IgPrimaryEocTmcDs1IfIndex_Object=MibTableColumn
igPrimaryEocTmcDs1IfIndex=_IgPrimaryEocTmcDs1IfIndex_Object((1,3,6,1,4,1,5504,4,3,1,1,1,7),_IgPrimaryEocTmcDs1IfIndex_Type())
igPrimaryEocTmcDs1IfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:igPrimaryEocTmcDs1IfIndex.setStatus(_A)
_IgSecondaryEocTmcDs1IfIndex_Type=InterfaceIndexOrZero
_IgSecondaryEocTmcDs1IfIndex_Object=MibTableColumn
igSecondaryEocTmcDs1IfIndex=_IgSecondaryEocTmcDs1IfIndex_Object((1,3,6,1,4,1,5504,4,3,1,1,1,8),_IgSecondaryEocTmcDs1IfIndex_Type())
igSecondaryEocTmcDs1IfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:igSecondaryEocTmcDs1IfIndex.setStatus(_A)
class _IgAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_H,2)))
_IgAdminStatus_Type.__name__=_C
_IgAdminStatus_Object=MibTableColumn
igAdminStatus=_IgAdminStatus_Object((1,3,6,1,4,1,5504,4,3,1,1,1,9),_IgAdminStatus_Type())
igAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:igAdminStatus.setStatus(_A)
class _IgOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operable',1),('inoperable',2),(_K,3),('inoperableIsInProgress',4),('inoperableOosInProgress',5)))
_IgOperationalStatus_Type.__name__=_C
_IgOperationalStatus_Object=MibTableColumn
igOperationalStatus=_IgOperationalStatus_Object((1,3,6,1,4,1,5504,4,3,1,1,1,10),_IgOperationalStatus_Type())
igOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:igOperationalStatus.setStatus(_A)
class _IgPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noStandbyConfigured',1),('configuredAndAvailable',2),('configuredAndUnavailable',3)))
_IgPeerStatus_Type.__name__=_C
_IgPeerStatus_Object=MibTableColumn
igPeerStatus=_IgPeerStatus_Object((1,3,6,1,4,1,5504,4,3,1,1,1,11),_IgPeerStatus_Type())
igPeerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:igPeerStatus.setStatus(_A)
class _IgMaxConfigCalls_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(22,670))
_IgMaxConfigCalls_Type.__name__=_O
_IgMaxConfigCalls_Object=MibTableColumn
igMaxConfigCalls=_IgMaxConfigCalls_Object((1,3,6,1,4,1,5504,4,3,1,1,1,12),_IgMaxConfigCalls_Type())
igMaxConfigCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:igMaxConfigCalls.setStatus(_A)
if mibBuilder.loadTexts:igMaxConfigCalls.setUnits(_G)
class _IgCurrActiveCalls_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,670))
_IgCurrActiveCalls_Type.__name__=_O
_IgCurrActiveCalls_Object=MibTableColumn
igCurrActiveCalls=_IgCurrActiveCalls_Object((1,3,6,1,4,1,5504,4,3,1,1,1,13),_IgCurrActiveCalls_Type())
igCurrActiveCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrActiveCalls.setStatus(_A)
if mibBuilder.loadTexts:igCurrActiveCalls.setUnits(_G)
class _IgStatsTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_IgStatsTimeElapsed_Type.__name__=_C
_IgStatsTimeElapsed_Object=MibTableColumn
igStatsTimeElapsed=_IgStatsTimeElapsed_Object((1,3,6,1,4,1,5504,4,3,1,1,1,14),_IgStatsTimeElapsed_Type())
igStatsTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:igStatsTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:igStatsTimeElapsed.setUnits(_P)
class _IgStatsValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_IgStatsValidIntervals_Type.__name__=_C
_IgStatsValidIntervals_Object=MibTableColumn
igStatsValidIntervals=_IgStatsValidIntervals_Object((1,3,6,1,4,1,5504,4,3,1,1,1,15),_IgStatsValidIntervals_Type())
igStatsValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:igStatsValidIntervals.setStatus(_A)
if mibBuilder.loadTexts:igStatsValidIntervals.setUnits(_U)
class _IgStatsInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_IgStatsInvalidIntervals_Type.__name__=_C
_IgStatsInvalidIntervals_Object=MibTableColumn
igStatsInvalidIntervals=_IgStatsInvalidIntervals_Object((1,3,6,1,4,1,5504,4,3,1,1,1,16),_IgStatsInvalidIntervals_Type())
igStatsInvalidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:igStatsInvalidIntervals.setStatus(_A)
if mibBuilder.loadTexts:igStatsInvalidIntervals.setUnits(_U)
_IgRowStatus_Type=ZhoneRowStatus
_IgRowStatus_Object=MibTableColumn
igRowStatus=_IgRowStatus_Object((1,3,6,1,4,1,5504,4,3,1,1,1,17),_IgRowStatus_Type())
igRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:igRowStatus.setStatus(_A)
class _IgWorkingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('passive',2)))
_IgWorkingMode_Type.__name__=_C
_IgWorkingMode_Object=MibTableColumn
igWorkingMode=_IgWorkingMode_Object((1,3,6,1,4,1,5504,4,3,1,1,1,18),_IgWorkingMode_Type())
igWorkingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:igWorkingMode.setStatus(_A)
_IgControlChannelTable_Object=MibTable
igControlChannelTable=_IgControlChannelTable_Object((1,3,6,1,4,1,5504,4,3,1,2))
if mibBuilder.loadTexts:igControlChannelTable.setStatus(_A)
_IgControlChannelEntry_Object=MibTableRow
igControlChannelEntry=_IgControlChannelEntry_Object((1,3,6,1,4,1,5504,4,3,1,2,1))
if mibBuilder.loadTexts:igControlChannelEntry.setStatus(_A)
class _IgControlChannelTmcPrimarySvcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_K,2),(_H,3)))
_IgControlChannelTmcPrimarySvcState_Type.__name__=_C
_IgControlChannelTmcPrimarySvcState_Object=MibTableColumn
igControlChannelTmcPrimarySvcState=_IgControlChannelTmcPrimarySvcState_Object((1,3,6,1,4,1,5504,4,3,1,2,1,1),_IgControlChannelTmcPrimarySvcState_Type())
igControlChannelTmcPrimarySvcState.setMaxAccess(_B)
if mibBuilder.loadTexts:igControlChannelTmcPrimarySvcState.setStatus(_A)
class _IgControlChannelTmcSecondarySvcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_K,2),(_H,3)))
_IgControlChannelTmcSecondarySvcState_Type.__name__=_C
_IgControlChannelTmcSecondarySvcState_Object=MibTableColumn
igControlChannelTmcSecondarySvcState=_IgControlChannelTmcSecondarySvcState_Object((1,3,6,1,4,1,5504,4,3,1,2,1,2),_IgControlChannelTmcSecondarySvcState_Type())
igControlChannelTmcSecondarySvcState.setMaxAccess(_B)
if mibBuilder.loadTexts:igControlChannelTmcSecondarySvcState.setStatus(_A)
class _IgControlChannelT303_Type(Integer32):defaultValue=700;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(700,700),ValueRangeConstraint(1200,1200),ValueRangeConstraint(1700,1700),ValueRangeConstraint(2200,2200),ValueRangeConstraint(2700,2700),ValueRangeConstraint(3200,3200),ValueRangeConstraint(3700,3700),ValueRangeConstraint(4200,4200),ValueRangeConstraint(4700,4700))
_IgControlChannelT303_Type.__name__=_C
_IgControlChannelT303_Object=MibTableColumn
igControlChannelT303=_IgControlChannelT303_Object((1,3,6,1,4,1,5504,4,3,1,2,1,3),_IgControlChannelT303_Type())
igControlChannelT303.setMaxAccess(_E)
if mibBuilder.loadTexts:igControlChannelT303.setStatus(_A)
if mibBuilder.loadTexts:igControlChannelT303.setUnits(_N)
class _IgControlChannelT396_Type(Integer32):defaultValue=14700;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(700,700),ValueRangeConstraint(1700,1700),ValueRangeConstraint(2700,2700),ValueRangeConstraint(3700,3700),ValueRangeConstraint(4700,4700),ValueRangeConstraint(5700,5700),ValueRangeConstraint(6700,6700),ValueRangeConstraint(7700,7700),ValueRangeConstraint(8700,8700),ValueRangeConstraint(9700,9700),ValueRangeConstraint(10700,10700),ValueRangeConstraint(11700,11700),ValueRangeConstraint(12700,12700),ValueRangeConstraint(13700,13700),ValueRangeConstraint(14700,14700))
_IgControlChannelT396_Type.__name__=_C
_IgControlChannelT396_Object=MibTableColumn
igControlChannelT396=_IgControlChannelT396_Object((1,3,6,1,4,1,5504,4,3,1,2,1,4),_IgControlChannelT396_Type())
igControlChannelT396.setMaxAccess(_E)
if mibBuilder.loadTexts:igControlChannelT396.setStatus(_A)
if mibBuilder.loadTexts:igControlChannelT396.setUnits(_N)
class _IgSapi0MaxOutstandingFrames_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_IgSapi0MaxOutstandingFrames_Type.__name__=_C
_IgSapi0MaxOutstandingFrames_Object=MibTableColumn
igSapi0MaxOutstandingFrames=_IgSapi0MaxOutstandingFrames_Object((1,3,6,1,4,1,5504,4,3,1,2,1,5),_IgSapi0MaxOutstandingFrames_Type())
igSapi0MaxOutstandingFrames.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi0MaxOutstandingFrames.setStatus(_A)
if mibBuilder.loadTexts:igSapi0MaxOutstandingFrames.setUnits(_F)
class _IgSapi0N200_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_IgSapi0N200_Type.__name__=_C
_IgSapi0N200_Object=MibTableColumn
igSapi0N200=_IgSapi0N200_Object((1,3,6,1,4,1,5504,4,3,1,2,1,6),_IgSapi0N200_Type())
igSapi0N200.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi0N200.setStatus(_A)
class _IgSapi0T200_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100),ValueRangeConstraint(150,150),ValueRangeConstraint(200,200),ValueRangeConstraint(250,250),ValueRangeConstraint(300,300),ValueRangeConstraint(350,350))
_IgSapi0T200_Type.__name__=_C
_IgSapi0T200_Object=MibTableColumn
igSapi0T200=_IgSapi0T200_Object((1,3,6,1,4,1,5504,4,3,1,2,1,7),_IgSapi0T200_Type())
igSapi0T200.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi0T200.setStatus(_A)
if mibBuilder.loadTexts:igSapi0T200.setUnits(_N)
class _IgSapi0T203_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100),ValueRangeConstraint(110,110),ValueRangeConstraint(120,120),ValueRangeConstraint(130,130),ValueRangeConstraint(140,140),ValueRangeConstraint(150,150),ValueRangeConstraint(160,160),ValueRangeConstraint(170,170),ValueRangeConstraint(180,180),ValueRangeConstraint(190,190),ValueRangeConstraint(200,200),ValueRangeConstraint(210,210),ValueRangeConstraint(220,220),ValueRangeConstraint(230,230),ValueRangeConstraint(240,240),ValueRangeConstraint(250,250),ValueRangeConstraint(260,260),ValueRangeConstraint(270,270),ValueRangeConstraint(280,280),ValueRangeConstraint(290,290),ValueRangeConstraint(300,300))
_IgSapi0T203_Type.__name__=_C
_IgSapi0T203_Object=MibTableColumn
igSapi0T203=_IgSapi0T203_Object((1,3,6,1,4,1,5504,4,3,1,2,1,8),_IgSapi0T203_Type())
igSapi0T203.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi0T203.setStatus(_A)
if mibBuilder.loadTexts:igSapi0T203.setUnits(_P)
class _IgSapi0PpsMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3)))
_IgSapi0PpsMode_Type.__name__=_C
_IgSapi0PpsMode_Object=MibTableColumn
igSapi0PpsMode=_IgSapi0PpsMode_Object((1,3,6,1,4,1,5504,4,3,1,2,1,9),_IgSapi0PpsMode_Type())
igSapi0PpsMode.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi0PpsMode.setStatus(_A)
class _IgSapi1MaxOutstandingFrames_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_IgSapi1MaxOutstandingFrames_Type.__name__=_C
_IgSapi1MaxOutstandingFrames_Object=MibTableColumn
igSapi1MaxOutstandingFrames=_IgSapi1MaxOutstandingFrames_Object((1,3,6,1,4,1,5504,4,3,1,2,1,10),_IgSapi1MaxOutstandingFrames_Type())
igSapi1MaxOutstandingFrames.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi1MaxOutstandingFrames.setStatus(_A)
if mibBuilder.loadTexts:igSapi1MaxOutstandingFrames.setUnits(_F)
class _IgSapi1N200_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_IgSapi1N200_Type.__name__=_C
_IgSapi1N200_Object=MibTableColumn
igSapi1N200=_IgSapi1N200_Object((1,3,6,1,4,1,5504,4,3,1,2,1,11),_IgSapi1N200_Type())
igSapi1N200.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi1N200.setStatus(_A)
class _IgSapi1T200_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100),ValueRangeConstraint(150,150),ValueRangeConstraint(200,200),ValueRangeConstraint(250,250),ValueRangeConstraint(300,300),ValueRangeConstraint(350,350))
_IgSapi1T200_Type.__name__=_C
_IgSapi1T200_Object=MibTableColumn
igSapi1T200=_IgSapi1T200_Object((1,3,6,1,4,1,5504,4,3,1,2,1,12),_IgSapi1T200_Type())
igSapi1T200.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi1T200.setStatus(_A)
if mibBuilder.loadTexts:igSapi1T200.setUnits(_N)
class _IgSapi1T203_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100),ValueRangeConstraint(110,110),ValueRangeConstraint(120,120),ValueRangeConstraint(130,130),ValueRangeConstraint(140,140),ValueRangeConstraint(150,150),ValueRangeConstraint(160,160),ValueRangeConstraint(170,170),ValueRangeConstraint(180,180),ValueRangeConstraint(190,190),ValueRangeConstraint(200,200),ValueRangeConstraint(210,210),ValueRangeConstraint(220,220),ValueRangeConstraint(230,230),ValueRangeConstraint(240,240),ValueRangeConstraint(250,250),ValueRangeConstraint(260,260),ValueRangeConstraint(270,270),ValueRangeConstraint(280,280),ValueRangeConstraint(290,290),ValueRangeConstraint(300,300))
_IgSapi1T203_Type.__name__=_C
_IgSapi1T203_Object=MibTableColumn
igSapi1T203=_IgSapi1T203_Object((1,3,6,1,4,1,5504,4,3,1,2,1,13),_IgSapi1T203_Type())
igSapi1T203.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi1T203.setStatus(_A)
if mibBuilder.loadTexts:igSapi1T203.setUnits(_P)
class _IgSapi1PpsMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3)))
_IgSapi1PpsMode_Type.__name__=_C
_IgSapi1PpsMode_Object=MibTableColumn
igSapi1PpsMode=_IgSapi1PpsMode_Object((1,3,6,1,4,1,5504,4,3,1,2,1,14),_IgSapi1PpsMode_Type())
igSapi1PpsMode.setMaxAccess(_E)
if mibBuilder.loadTexts:igSapi1PpsMode.setStatus(_A)
class _IgControlChannelEocPrimarySvcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_K,2),(_H,3)))
_IgControlChannelEocPrimarySvcState_Type.__name__=_C
_IgControlChannelEocPrimarySvcState_Object=MibTableColumn
igControlChannelEocPrimarySvcState=_IgControlChannelEocPrimarySvcState_Object((1,3,6,1,4,1,5504,4,3,1,2,1,15),_IgControlChannelEocPrimarySvcState_Type())
igControlChannelEocPrimarySvcState.setMaxAccess(_B)
if mibBuilder.loadTexts:igControlChannelEocPrimarySvcState.setStatus(_A)
class _IgControlChannelEocSecondarySvcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_K,2),(_H,3)))
_IgControlChannelEocSecondarySvcState_Type.__name__=_C
_IgControlChannelEocSecondarySvcState_Object=MibTableColumn
igControlChannelEocSecondarySvcState=_IgControlChannelEocSecondarySvcState_Object((1,3,6,1,4,1,5504,4,3,1,2,1,17),_IgControlChannelEocSecondarySvcState_Type())
igControlChannelEocSecondarySvcState.setMaxAccess(_B)
if mibBuilder.loadTexts:igControlChannelEocSecondarySvcState.setStatus(_A)
_IgStatsCurrentTable_Object=MibTable
igStatsCurrentTable=_IgStatsCurrentTable_Object((1,3,6,1,4,1,5504,4,3,1,3))
if mibBuilder.loadTexts:igStatsCurrentTable.setStatus(_A)
_IgStatsCurrentEntry_Object=MibTableRow
igStatsCurrentEntry=_IgStatsCurrentEntry_Object((1,3,6,1,4,1,5504,4,3,1,3,1))
if mibBuilder.loadTexts:igStatsCurrentEntry.setStatus(_A)
_IgCurrentOutboundCalls_Type=PerfCurrentCount
_IgCurrentOutboundCalls_Object=MibTableColumn
igCurrentOutboundCalls=_IgCurrentOutboundCalls_Object((1,3,6,1,4,1,5504,4,3,1,3,1,1),_IgCurrentOutboundCalls_Type())
igCurrentOutboundCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentOutboundCalls.setStatus(_A)
if mibBuilder.loadTexts:igCurrentOutboundCalls.setUnits(_G)
_IgCurrentInboundCalls_Type=PerfCurrentCount
_IgCurrentInboundCalls_Object=MibTableColumn
igCurrentInboundCalls=_IgCurrentInboundCalls_Object((1,3,6,1,4,1,5504,4,3,1,3,1,2),_IgCurrentInboundCalls_Type())
igCurrentInboundCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentInboundCalls.setStatus(_A)
if mibBuilder.loadTexts:igCurrentInboundCalls.setUnits(_G)
_IgCurrentOutboundCallsBlocked_Type=PerfCurrentCount
_IgCurrentOutboundCallsBlocked_Object=MibTableColumn
igCurrentOutboundCallsBlocked=_IgCurrentOutboundCallsBlocked_Object((1,3,6,1,4,1,5504,4,3,1,3,1,3),_IgCurrentOutboundCallsBlocked_Type())
igCurrentOutboundCallsBlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentOutboundCallsBlocked.setStatus(_A)
if mibBuilder.loadTexts:igCurrentOutboundCallsBlocked.setUnits(_G)
_IgCurrentGR303ProtocolErrors_Type=PerfCurrentCount
_IgCurrentGR303ProtocolErrors_Object=MibTableColumn
igCurrentGR303ProtocolErrors=_IgCurrentGR303ProtocolErrors_Object((1,3,6,1,4,1,5504,4,3,1,3,1,4),_IgCurrentGR303ProtocolErrors_Type())
igCurrentGR303ProtocolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentGR303ProtocolErrors.setStatus(_A)
if mibBuilder.loadTexts:igCurrentGR303ProtocolErrors.setUnits(_Q)
_IgCurrentTMCLapdSent_Type=PerfCurrentCount
_IgCurrentTMCLapdSent_Object=MibTableColumn
igCurrentTMCLapdSent=_IgCurrentTMCLapdSent_Object((1,3,6,1,4,1,5504,4,3,1,3,1,5),_IgCurrentTMCLapdSent_Type())
igCurrentTMCLapdSent.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentTMCLapdSent.setStatus(_A)
if mibBuilder.loadTexts:igCurrentTMCLapdSent.setUnits(_F)
_IgCurrentTMCLapdRcvd_Type=PerfCurrentCount
_IgCurrentTMCLapdRcvd_Object=MibTableColumn
igCurrentTMCLapdRcvd=_IgCurrentTMCLapdRcvd_Object((1,3,6,1,4,1,5504,4,3,1,3,1,6),_IgCurrentTMCLapdRcvd_Type())
igCurrentTMCLapdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentTMCLapdRcvd.setStatus(_A)
if mibBuilder.loadTexts:igCurrentTMCLapdRcvd.setUnits(_F)
_IgCurrentTMCLapdRcvdErrs_Type=PerfCurrentCount
_IgCurrentTMCLapdRcvdErrs_Object=MibTableColumn
igCurrentTMCLapdRcvdErrs=_IgCurrentTMCLapdRcvdErrs_Object((1,3,6,1,4,1,5504,4,3,1,3,1,7),_IgCurrentTMCLapdRcvdErrs_Type())
igCurrentTMCLapdRcvdErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentTMCLapdRcvdErrs.setStatus(_A)
if mibBuilder.loadTexts:igCurrentTMCLapdRcvdErrs.setUnits(_F)
_IgCurrentEOCLapdSent_Type=PerfCurrentCount
_IgCurrentEOCLapdSent_Object=MibTableColumn
igCurrentEOCLapdSent=_IgCurrentEOCLapdSent_Object((1,3,6,1,4,1,5504,4,3,1,3,1,8),_IgCurrentEOCLapdSent_Type())
igCurrentEOCLapdSent.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentEOCLapdSent.setStatus(_A)
if mibBuilder.loadTexts:igCurrentEOCLapdSent.setUnits(_F)
_IgCurrentEOCLapdRcvd_Type=PerfCurrentCount
_IgCurrentEOCLapdRcvd_Object=MibTableColumn
igCurrentEOCLapdRcvd=_IgCurrentEOCLapdRcvd_Object((1,3,6,1,4,1,5504,4,3,1,3,1,9),_IgCurrentEOCLapdRcvd_Type())
igCurrentEOCLapdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentEOCLapdRcvd.setStatus(_A)
if mibBuilder.loadTexts:igCurrentEOCLapdRcvd.setUnits(_F)
_IgCurrentEOCLapdRcvdErrs_Type=PerfCurrentCount
_IgCurrentEOCLapdRcvdErrs_Object=MibTableColumn
igCurrentEOCLapdRcvdErrs=_IgCurrentEOCLapdRcvdErrs_Object((1,3,6,1,4,1,5504,4,3,1,3,1,10),_IgCurrentEOCLapdRcvdErrs_Type())
igCurrentEOCLapdRcvdErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:igCurrentEOCLapdRcvdErrs.setStatus(_A)
if mibBuilder.loadTexts:igCurrentEOCLapdRcvdErrs.setUnits(_F)
_IgStatsIntervalTable_Object=MibTable
igStatsIntervalTable=_IgStatsIntervalTable_Object((1,3,6,1,4,1,5504,4,3,1,4))
if mibBuilder.loadTexts:igStatsIntervalTable.setStatus(_A)
_IgStatsIntervalEntry_Object=MibTableRow
igStatsIntervalEntry=_IgStatsIntervalEntry_Object((1,3,6,1,4,1,5504,4,3,1,4,1))
igStatsIntervalEntry.setIndexNames((0,_D,_I),(0,_D,_Y))
if mibBuilder.loadTexts:igStatsIntervalEntry.setStatus(_A)
class _IgIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_IgIntervalNumber_Type.__name__=_C
_IgIntervalNumber_Object=MibTableColumn
igIntervalNumber=_IgIntervalNumber_Object((1,3,6,1,4,1,5504,4,3,1,4,1,1),_IgIntervalNumber_Type())
igIntervalNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:igIntervalNumber.setStatus(_A)
_IgIntervalOutboundCalls_Type=PerfCurrentCount
_IgIntervalOutboundCalls_Object=MibTableColumn
igIntervalOutboundCalls=_IgIntervalOutboundCalls_Object((1,3,6,1,4,1,5504,4,3,1,4,1,2),_IgIntervalOutboundCalls_Type())
igIntervalOutboundCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalOutboundCalls.setStatus(_A)
if mibBuilder.loadTexts:igIntervalOutboundCalls.setUnits(_G)
_IgIntervalInboundCalls_Type=PerfCurrentCount
_IgIntervalInboundCalls_Object=MibTableColumn
igIntervalInboundCalls=_IgIntervalInboundCalls_Object((1,3,6,1,4,1,5504,4,3,1,4,1,3),_IgIntervalInboundCalls_Type())
igIntervalInboundCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalInboundCalls.setStatus(_A)
if mibBuilder.loadTexts:igIntervalInboundCalls.setUnits(_G)
_IgIntervalOutboundCallsBlocked_Type=PerfCurrentCount
_IgIntervalOutboundCallsBlocked_Object=MibTableColumn
igIntervalOutboundCallsBlocked=_IgIntervalOutboundCallsBlocked_Object((1,3,6,1,4,1,5504,4,3,1,4,1,4),_IgIntervalOutboundCallsBlocked_Type())
igIntervalOutboundCallsBlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalOutboundCallsBlocked.setStatus(_A)
if mibBuilder.loadTexts:igIntervalOutboundCallsBlocked.setUnits(_G)
_IgIntervalGR303ProtocolErrors_Type=PerfCurrentCount
_IgIntervalGR303ProtocolErrors_Object=MibTableColumn
igIntervalGR303ProtocolErrors=_IgIntervalGR303ProtocolErrors_Object((1,3,6,1,4,1,5504,4,3,1,4,1,5),_IgIntervalGR303ProtocolErrors_Type())
igIntervalGR303ProtocolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalGR303ProtocolErrors.setStatus(_A)
if mibBuilder.loadTexts:igIntervalGR303ProtocolErrors.setUnits(_Q)
_IgIntervalTMCLapdSent_Type=PerfCurrentCount
_IgIntervalTMCLapdSent_Object=MibTableColumn
igIntervalTMCLapdSent=_IgIntervalTMCLapdSent_Object((1,3,6,1,4,1,5504,4,3,1,4,1,6),_IgIntervalTMCLapdSent_Type())
igIntervalTMCLapdSent.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalTMCLapdSent.setStatus(_A)
if mibBuilder.loadTexts:igIntervalTMCLapdSent.setUnits(_F)
_IgIntervalTMCLapdRcvd_Type=PerfCurrentCount
_IgIntervalTMCLapdRcvd_Object=MibTableColumn
igIntervalTMCLapdRcvd=_IgIntervalTMCLapdRcvd_Object((1,3,6,1,4,1,5504,4,3,1,4,1,7),_IgIntervalTMCLapdRcvd_Type())
igIntervalTMCLapdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalTMCLapdRcvd.setStatus(_A)
if mibBuilder.loadTexts:igIntervalTMCLapdRcvd.setUnits(_F)
_IgintervalTMCLapdRcvdErrs_Type=PerfCurrentCount
_IgintervalTMCLapdRcvdErrs_Object=MibTableColumn
igintervalTMCLapdRcvdErrs=_IgintervalTMCLapdRcvdErrs_Object((1,3,6,1,4,1,5504,4,3,1,4,1,8),_IgintervalTMCLapdRcvdErrs_Type())
igintervalTMCLapdRcvdErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:igintervalTMCLapdRcvdErrs.setStatus(_A)
if mibBuilder.loadTexts:igintervalTMCLapdRcvdErrs.setUnits(_F)
_IgIntervalEOCLapdSent_Type=PerfCurrentCount
_IgIntervalEOCLapdSent_Object=MibTableColumn
igIntervalEOCLapdSent=_IgIntervalEOCLapdSent_Object((1,3,6,1,4,1,5504,4,3,1,4,1,9),_IgIntervalEOCLapdSent_Type())
igIntervalEOCLapdSent.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalEOCLapdSent.setStatus(_A)
if mibBuilder.loadTexts:igIntervalEOCLapdSent.setUnits(_F)
_IgIntervalEOCLapdRcvd_Type=PerfCurrentCount
_IgIntervalEOCLapdRcvd_Object=MibTableColumn
igIntervalEOCLapdRcvd=_IgIntervalEOCLapdRcvd_Object((1,3,6,1,4,1,5504,4,3,1,4,1,10),_IgIntervalEOCLapdRcvd_Type())
igIntervalEOCLapdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalEOCLapdRcvd.setStatus(_A)
if mibBuilder.loadTexts:igIntervalEOCLapdRcvd.setUnits(_F)
_IgIntervalEOCLapdRcvdErrs_Type=PerfCurrentCount
_IgIntervalEOCLapdRcvdErrs_Object=MibTableColumn
igIntervalEOCLapdRcvdErrs=_IgIntervalEOCLapdRcvdErrs_Object((1,3,6,1,4,1,5504,4,3,1,4,1,11),_IgIntervalEOCLapdRcvdErrs_Type())
igIntervalEOCLapdRcvdErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalEOCLapdRcvdErrs.setStatus(_A)
if mibBuilder.loadTexts:igIntervalEOCLapdRcvdErrs.setUnits(_F)
class _IgIntervalValidData_Type(TruthValue):defaultValue=2
_IgIntervalValidData_Type.__name__=_R
_IgIntervalValidData_Object=MibTableColumn
igIntervalValidData=_IgIntervalValidData_Object((1,3,6,1,4,1,5504,4,3,1,4,1,12),_IgIntervalValidData_Type())
igIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:igIntervalValidData.setStatus(_A)
_IgStatsTotalTable_Object=MibTable
igStatsTotalTable=_IgStatsTotalTable_Object((1,3,6,1,4,1,5504,4,3,1,5))
if mibBuilder.loadTexts:igStatsTotalTable.setStatus(_A)
_IgStatsTotalEntry_Object=MibTableRow
igStatsTotalEntry=_IgStatsTotalEntry_Object((1,3,6,1,4,1,5504,4,3,1,5,1))
if mibBuilder.loadTexts:igStatsTotalEntry.setStatus(_A)
_IgTotalOutboundCalls_Type=PerfCurrentCount
_IgTotalOutboundCalls_Object=MibTableColumn
igTotalOutboundCalls=_IgTotalOutboundCalls_Object((1,3,6,1,4,1,5504,4,3,1,5,1,1),_IgTotalOutboundCalls_Type())
igTotalOutboundCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalOutboundCalls.setStatus(_A)
if mibBuilder.loadTexts:igTotalOutboundCalls.setUnits(_G)
_IgTotalInboundCalls_Type=PerfCurrentCount
_IgTotalInboundCalls_Object=MibTableColumn
igTotalInboundCalls=_IgTotalInboundCalls_Object((1,3,6,1,4,1,5504,4,3,1,5,1,2),_IgTotalInboundCalls_Type())
igTotalInboundCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalInboundCalls.setStatus(_A)
if mibBuilder.loadTexts:igTotalInboundCalls.setUnits(_G)
_IgTotalOutboundCallsBlocked_Type=PerfCurrentCount
_IgTotalOutboundCallsBlocked_Object=MibTableColumn
igTotalOutboundCallsBlocked=_IgTotalOutboundCallsBlocked_Object((1,3,6,1,4,1,5504,4,3,1,5,1,3),_IgTotalOutboundCallsBlocked_Type())
igTotalOutboundCallsBlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalOutboundCallsBlocked.setStatus(_A)
if mibBuilder.loadTexts:igTotalOutboundCallsBlocked.setUnits(_G)
_IgTotalGR303ProtocolErrors_Type=PerfCurrentCount
_IgTotalGR303ProtocolErrors_Object=MibTableColumn
igTotalGR303ProtocolErrors=_IgTotalGR303ProtocolErrors_Object((1,3,6,1,4,1,5504,4,3,1,5,1,4),_IgTotalGR303ProtocolErrors_Type())
igTotalGR303ProtocolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalGR303ProtocolErrors.setStatus(_A)
if mibBuilder.loadTexts:igTotalGR303ProtocolErrors.setUnits(_Q)
_IgTotalTMCLapdSent_Type=PerfCurrentCount
_IgTotalTMCLapdSent_Object=MibTableColumn
igTotalTMCLapdSent=_IgTotalTMCLapdSent_Object((1,3,6,1,4,1,5504,4,3,1,5,1,5),_IgTotalTMCLapdSent_Type())
igTotalTMCLapdSent.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalTMCLapdSent.setStatus(_A)
if mibBuilder.loadTexts:igTotalTMCLapdSent.setUnits(_F)
_IgTotalTMCLapdRcvd_Type=PerfCurrentCount
_IgTotalTMCLapdRcvd_Object=MibTableColumn
igTotalTMCLapdRcvd=_IgTotalTMCLapdRcvd_Object((1,3,6,1,4,1,5504,4,3,1,5,1,6),_IgTotalTMCLapdRcvd_Type())
igTotalTMCLapdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalTMCLapdRcvd.setStatus(_A)
if mibBuilder.loadTexts:igTotalTMCLapdRcvd.setUnits(_F)
_IgTotalTMCLapdRcvdErrs_Type=PerfCurrentCount
_IgTotalTMCLapdRcvdErrs_Object=MibTableColumn
igTotalTMCLapdRcvdErrs=_IgTotalTMCLapdRcvdErrs_Object((1,3,6,1,4,1,5504,4,3,1,5,1,7),_IgTotalTMCLapdRcvdErrs_Type())
igTotalTMCLapdRcvdErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalTMCLapdRcvdErrs.setStatus(_A)
if mibBuilder.loadTexts:igTotalTMCLapdRcvdErrs.setUnits(_F)
_IgTotalEOCLapdSent_Type=PerfCurrentCount
_IgTotalEOCLapdSent_Object=MibTableColumn
igTotalEOCLapdSent=_IgTotalEOCLapdSent_Object((1,3,6,1,4,1,5504,4,3,1,5,1,8),_IgTotalEOCLapdSent_Type())
igTotalEOCLapdSent.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalEOCLapdSent.setStatus(_A)
if mibBuilder.loadTexts:igTotalEOCLapdSent.setUnits(_F)
_IgTotalEOCLapdRcvd_Type=PerfCurrentCount
_IgTotalEOCLapdRcvd_Object=MibTableColumn
igTotalEOCLapdRcvd=_IgTotalEOCLapdRcvd_Object((1,3,6,1,4,1,5504,4,3,1,5,1,9),_IgTotalEOCLapdRcvd_Type())
igTotalEOCLapdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalEOCLapdRcvd.setStatus(_A)
if mibBuilder.loadTexts:igTotalEOCLapdRcvd.setUnits(_F)
_IgTotalEOCLapdRcvdErrs_Type=PerfCurrentCount
_IgTotalEOCLapdRcvdErrs_Object=MibTableColumn
igTotalEOCLapdRcvdErrs=_IgTotalEOCLapdRcvdErrs_Object((1,3,6,1,4,1,5504,4,3,1,5,1,10),_IgTotalEOCLapdRcvdErrs_Type())
igTotalEOCLapdRcvdErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:igTotalEOCLapdRcvdErrs.setStatus(_A)
if mibBuilder.loadTexts:igTotalEOCLapdRcvdErrs.setUnits(_F)
_Ds1LineMappingTable_Object=MibTable
ds1LineMappingTable=_Ds1LineMappingTable_Object((1,3,6,1,4,1,5504,4,3,1,6))
if mibBuilder.loadTexts:ds1LineMappingTable.setStatus(_A)
_Ds1LineMappingEntry_Object=MibTableRow
ds1LineMappingEntry=_Ds1LineMappingEntry_Object((1,3,6,1,4,1,5504,4,3,1,6,1))
ds1LineMappingEntry.setIndexNames((0,_D,_I),(0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:ds1LineMappingEntry.setStatus(_A)
class _DsnLgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DsnLgId_Type.__name__=_C
_DsnLgId_Object=MibTableColumn
dsnLgId=_DsnLgId_Object((1,3,6,1,4,1,5504,4,3,1,6,1,1),_DsnLgId_Type())
dsnLgId.setMaxAccess(_J)
if mibBuilder.loadTexts:dsnLgId.setStatus(_A)
class _Ds1ChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_Ds1ChannelNumber_Type.__name__=_C
_Ds1ChannelNumber_Object=MibTableColumn
ds1ChannelNumber=_Ds1ChannelNumber_Object((1,3,6,1,4,1,5504,4,3,1,6,1,2),_Ds1ChannelNumber_Type())
ds1ChannelNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:ds1ChannelNumber.setStatus(_A)
class _Ds1Role_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('payload',1),('secondary',2),('primary',3)))
_Ds1Role_Type.__name__=_C
_Ds1Role_Object=MibTableColumn
ds1Role=_Ds1Role_Object((1,3,6,1,4,1,5504,4,3,1,6,1,3),_Ds1Role_Type())
ds1Role.setMaxAccess(_E)
if mibBuilder.loadTexts:ds1Role.setStatus(_A)
_Ds1IfIndex_Type=InterfaceIndexOrZero
_Ds1IfIndex_Object=MibTableColumn
ds1IfIndex=_Ds1IfIndex_Object((1,3,6,1,4,1,5504,4,3,1,6,1,4),_Ds1IfIndex_Type())
ds1IfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ds1IfIndex.setStatus(_A)
_Ds1LineMappingRowStatus_Type=ZhoneRowStatus
_Ds1LineMappingRowStatus_Object=MibTableColumn
ds1LineMappingRowStatus=_Ds1LineMappingRowStatus_Object((1,3,6,1,4,1,5504,4,3,1,6,1,5),_Ds1LineMappingRowStatus_Type())
ds1LineMappingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ds1LineMappingRowStatus.setStatus(_A)
class _Ds1LogicalId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_Ds1LogicalId_Type.__name__=_C
_Ds1LogicalId_Object=MibTableColumn
ds1LogicalId=_Ds1LogicalId_Object((1,3,6,1,4,1,5504,4,3,1,6,1,6),_Ds1LogicalId_Type())
ds1LogicalId.setMaxAccess(_E)
if mibBuilder.loadTexts:ds1LogicalId.setStatus(_A)
_IgCrvTable_Object=MibTable
igCrvTable=_IgCrvTable_Object((1,3,6,1,4,1,5504,4,3,1,7))
if mibBuilder.loadTexts:igCrvTable.setStatus(_A)
_IgCrvEntry_Object=MibTableRow
igCrvEntry=_IgCrvEntry_Object((1,3,6,1,4,1,5504,4,3,1,7,1))
igCrvEntry.setIndexNames((0,_D,_I),(0,_D,'igCrv'))
if mibBuilder.loadTexts:igCrvEntry.setStatus(_A)
class _IgCrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_IgCrv_Type.__name__=_C
_IgCrv_Object=MibTableColumn
igCrv=_IgCrv_Object((1,3,6,1,4,1,5504,4,3,1,7,1,1),_IgCrv_Type())
igCrv.setMaxAccess(_J)
if mibBuilder.loadTexts:igCrv.setStatus(_A)
class _IgCrvLocalAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_H,2)))
_IgCrvLocalAdminState_Type.__name__=_C
_IgCrvLocalAdminState_Object=MibTableColumn
igCrvLocalAdminState=_IgCrvLocalAdminState_Object((1,3,6,1,4,1,5504,4,3,1,7,1,2),_IgCrvLocalAdminState_Type())
igCrvLocalAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:igCrvLocalAdminState.setStatus(_A)
class _IgCrvRemoteAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_H,2)))
_IgCrvRemoteAdminState_Type.__name__=_C
_IgCrvRemoteAdminState_Object=MibTableColumn
igCrvRemoteAdminState=_IgCrvRemoteAdminState_Object((1,3,6,1,4,1,5504,4,3,1,7,1,3),_IgCrvRemoteAdminState_Type())
igCrvRemoteAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:igCrvRemoteAdminState.setStatus(_A)
class _IgCrvOperStatus_Type(Bits):namedValues=NamedValues(*(('up',0),('fault',1),('manualOos',2),('removedFromServiceBySwitch',3),('unEquipped',4),('notConnected',5)))
_IgCrvOperStatus_Type.__name__='Bits'
_IgCrvOperStatus_Object=MibTableColumn
igCrvOperStatus=_IgCrvOperStatus_Object((1,3,6,1,4,1,5504,4,3,1,7,1,4),_IgCrvOperStatus_Type())
igCrvOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:igCrvOperStatus.setStatus(_A)
class _IgCrvTmcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('permanentSignal',2)))
_IgCrvTmcState_Type.__name__=_C
_IgCrvTmcState_Object=MibTableColumn
igCrvTmcState=_IgCrvTmcState_Object((1,3,6,1,4,1,5504,4,3,1,7,1,5),_IgCrvTmcState_Type())
igCrvTmcState.setMaxAccess(_B)
if mibBuilder.loadTexts:igCrvTmcState.setStatus(_A)
class _IgCrvSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*(('loopstart',2),('groundstart',3),('loopreversebattery',4),('electronicbusinessset',5)))
_IgCrvSignalType_Type.__name__=_C
_IgCrvSignalType_Object=MibTableColumn
igCrvSignalType=_IgCrvSignalType_Object((1,3,6,1,4,1,5504,4,3,1,7,1,6),_IgCrvSignalType_Type())
igCrvSignalType.setMaxAccess(_E)
if mibBuilder.loadTexts:igCrvSignalType.setStatus(_A)
_IgCrvRowStatus_Type=ZhoneRowStatus
_IgCrvRowStatus_Object=MibTableColumn
igCrvRowStatus=_IgCrvRowStatus_Object((1,3,6,1,4,1,5504,4,3,1,7,1,7),_IgCrvRowStatus_Type())
igCrvRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:igCrvRowStatus.setStatus(_A)
_Gr303Traps_ObjectIdentity=ObjectIdentity
gr303Traps=_Gr303Traps_ObjectIdentity((1,3,6,1,4,1,5504,4,3,1,8))
if mibBuilder.loadTexts:gr303Traps.setStatus(_A)
_Gr303TrapsPrefix_ObjectIdentity=ObjectIdentity
gr303TrapsPrefix=_Gr303TrapsPrefix_ObjectIdentity((1,3,6,1,4,1,5504,4,3,1,8,0))
if mibBuilder.loadTexts:gr303TrapsPrefix.setStatus(_A)
interfaceGroupEntry.registerAugmentions((_D,_b))
igControlChannelEntry.setIndexNames(*interfaceGroupEntry.getIndexNames())
interfaceGroupEntry.registerAugmentions((_D,_c))
igStatsCurrentEntry.setIndexNames(*interfaceGroupEntry.getIndexNames())
interfaceGroupEntry.registerAugmentions((_D,_d))
igStatsTotalEntry.setIndexNames(*interfaceGroupEntry.getIndexNames())
igOperStatusChange=NotificationType((1,3,6,1,4,1,5504,4,3,1,8,0,1))
igOperStatusChange.setObjects(*((_D,_e),(_D,_f)))
if mibBuilder.loadTexts:igOperStatusChange.setStatus(_A)
igTmcPrimaryStateChange=NotificationType((1,3,6,1,4,1,5504,4,3,1,8,0,2))
igTmcPrimaryStateChange.setObjects((_D,_g))
if mibBuilder.loadTexts:igTmcPrimaryStateChange.setStatus(_A)
igTmcSecondaryStateChange=NotificationType((1,3,6,1,4,1,5504,4,3,1,8,0,3))
igTmcSecondaryStateChange.setObjects((_D,_h))
if mibBuilder.loadTexts:igTmcSecondaryStateChange.setStatus(_A)
igEocPrimaryStateChange=NotificationType((1,3,6,1,4,1,5504,4,3,1,8,0,4))
igEocPrimaryStateChange.setObjects((_D,_i))
if mibBuilder.loadTexts:igEocPrimaryStateChange.setStatus(_A)
igEocSecondaryStateChange=NotificationType((1,3,6,1,4,1,5504,4,3,1,8,0,5))
igEocSecondaryStateChange.setObjects((_D,_j))
if mibBuilder.loadTexts:igEocSecondaryStateChange.setStatus(_A)
igCrvRemoteStateChange=NotificationType((1,3,6,1,4,1,5504,4,3,1,8,0,6))
igCrvRemoteStateChange.setObjects(*((_D,_k),(_D,_l),(_D,_m)))
if mibBuilder.loadTexts:igCrvRemoteStateChange.setStatus(_A)
igCrvTmcStateChange=NotificationType((1,3,6,1,4,1,5504,4,3,1,8,0,7))
igCrvTmcStateChange.setObjects((_D,_n))
if mibBuilder.loadTexts:igCrvTmcStateChange.setStatus(_A)
igSystemTimeChange=NotificationType((1,3,6,1,4,1,5504,4,3,1,8,0,8))
igSystemTimeChange.setObjects(*((_S,_T),(_D,_o)))
if mibBuilder.loadTexts:igSystemTimeChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zhoneGR303':zhoneGR303,'interfaceGroupTable':interfaceGroupTable,'interfaceGroupEntry':interfaceGroupEntry,_I:igNameId,'igShelf':igShelf,'igSlot':igSlot,'igPeerShelf':igPeerShelf,'igPeerSlot':igPeerSlot,'igSwitchType':igSwitchType,'igPrimaryEocTmcDs1IfIndex':igPrimaryEocTmcDs1IfIndex,'igSecondaryEocTmcDs1IfIndex':igSecondaryEocTmcDs1IfIndex,_e:igAdminStatus,_f:igOperationalStatus,'igPeerStatus':igPeerStatus,'igMaxConfigCalls':igMaxConfigCalls,'igCurrActiveCalls':igCurrActiveCalls,'igStatsTimeElapsed':igStatsTimeElapsed,'igStatsValidIntervals':igStatsValidIntervals,'igStatsInvalidIntervals':igStatsInvalidIntervals,_o:igRowStatus,'igWorkingMode':igWorkingMode,'igControlChannelTable':igControlChannelTable,_b:igControlChannelEntry,_g:igControlChannelTmcPrimarySvcState,_h:igControlChannelTmcSecondarySvcState,'igControlChannelT303':igControlChannelT303,'igControlChannelT396':igControlChannelT396,'igSapi0MaxOutstandingFrames':igSapi0MaxOutstandingFrames,'igSapi0N200':igSapi0N200,'igSapi0T200':igSapi0T200,'igSapi0T203':igSapi0T203,'igSapi0PpsMode':igSapi0PpsMode,'igSapi1MaxOutstandingFrames':igSapi1MaxOutstandingFrames,'igSapi1N200':igSapi1N200,'igSapi1T200':igSapi1T200,'igSapi1T203':igSapi1T203,'igSapi1PpsMode':igSapi1PpsMode,_i:igControlChannelEocPrimarySvcState,_j:igControlChannelEocSecondarySvcState,'igStatsCurrentTable':igStatsCurrentTable,_c:igStatsCurrentEntry,'igCurrentOutboundCalls':igCurrentOutboundCalls,'igCurrentInboundCalls':igCurrentInboundCalls,'igCurrentOutboundCallsBlocked':igCurrentOutboundCallsBlocked,'igCurrentGR303ProtocolErrors':igCurrentGR303ProtocolErrors,'igCurrentTMCLapdSent':igCurrentTMCLapdSent,'igCurrentTMCLapdRcvd':igCurrentTMCLapdRcvd,'igCurrentTMCLapdRcvdErrs':igCurrentTMCLapdRcvdErrs,'igCurrentEOCLapdSent':igCurrentEOCLapdSent,'igCurrentEOCLapdRcvd':igCurrentEOCLapdRcvd,'igCurrentEOCLapdRcvdErrs':igCurrentEOCLapdRcvdErrs,'igStatsIntervalTable':igStatsIntervalTable,'igStatsIntervalEntry':igStatsIntervalEntry,_Y:igIntervalNumber,'igIntervalOutboundCalls':igIntervalOutboundCalls,'igIntervalInboundCalls':igIntervalInboundCalls,'igIntervalOutboundCallsBlocked':igIntervalOutboundCallsBlocked,'igIntervalGR303ProtocolErrors':igIntervalGR303ProtocolErrors,'igIntervalTMCLapdSent':igIntervalTMCLapdSent,'igIntervalTMCLapdRcvd':igIntervalTMCLapdRcvd,'igintervalTMCLapdRcvdErrs':igintervalTMCLapdRcvdErrs,'igIntervalEOCLapdSent':igIntervalEOCLapdSent,'igIntervalEOCLapdRcvd':igIntervalEOCLapdRcvd,'igIntervalEOCLapdRcvdErrs':igIntervalEOCLapdRcvdErrs,'igIntervalValidData':igIntervalValidData,'igStatsTotalTable':igStatsTotalTable,_d:igStatsTotalEntry,'igTotalOutboundCalls':igTotalOutboundCalls,'igTotalInboundCalls':igTotalInboundCalls,'igTotalOutboundCallsBlocked':igTotalOutboundCallsBlocked,'igTotalGR303ProtocolErrors':igTotalGR303ProtocolErrors,'igTotalTMCLapdSent':igTotalTMCLapdSent,'igTotalTMCLapdRcvd':igTotalTMCLapdRcvd,'igTotalTMCLapdRcvdErrs':igTotalTMCLapdRcvdErrs,'igTotalEOCLapdSent':igTotalEOCLapdSent,'igTotalEOCLapdRcvd':igTotalEOCLapdRcvd,'igTotalEOCLapdRcvdErrs':igTotalEOCLapdRcvdErrs,'ds1LineMappingTable':ds1LineMappingTable,'ds1LineMappingEntry':ds1LineMappingEntry,_Z:dsnLgId,_a:ds1ChannelNumber,'ds1Role':ds1Role,'ds1IfIndex':ds1IfIndex,'ds1LineMappingRowStatus':ds1LineMappingRowStatus,'ds1LogicalId':ds1LogicalId,'igCrvTable':igCrvTable,'igCrvEntry':igCrvEntry,'igCrv':igCrv,_k:igCrvLocalAdminState,_l:igCrvRemoteAdminState,_m:igCrvOperStatus,_n:igCrvTmcState,'igCrvSignalType':igCrvSignalType,'igCrvRowStatus':igCrvRowStatus,'gr303Traps':gr303Traps,'gr303TrapsPrefix':gr303TrapsPrefix,'igOperStatusChange':igOperStatusChange,'igTmcPrimaryStateChange':igTmcPrimaryStateChange,'igTmcSecondaryStateChange':igTmcSecondaryStateChange,'igEocPrimaryStateChange':igEocPrimaryStateChange,'igEocSecondaryStateChange':igEocSecondaryStateChange,'igCrvRemoteStateChange':igCrvRemoteStateChange,'igCrvTmcStateChange':igCrvTmcStateChange,'igSystemTimeChange':igSystemTimeChange})