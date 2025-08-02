_O='nnOpticalPmDayMonType'
_N='nnOpticalPmDayIntIndex'
_M='nnOpticalPmDayIfIndex'
_L='nnOpticalPm15MinMonType'
_K='nnOpticalPm15MinIntIndex'
_J='nnOpticalPm15MinIfIndex'
_I='nnOpticalPmBaslnMonType'
_H='nnOpticalPmBaslnIfIndex'
_G='nnOpticalPmUntMonType'
_F='nnOpticalPmUntIfIndex'
_E='nnOpticalPmRecentMonType'
_D='nnOpticalPmRecentIfIndex'
_C='NORTEL-OPTICAL-PM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nnOpticalGenericMIBs,=mibBuilder.importSymbols('NORTEL-OPTICAL-GENERIC-MIB','nnOpticalGenericMIBs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
nnOpticalPmMIB=ModuleIdentity((1,3,6,1,4,1,562,68,10,1))
if mibBuilder.loadTexts:nnOpticalPmMIB.setRevisions(('2005-08-16 00:00','2006-04-12 00:00','2006-07-12 00:00','2007-05-21 00:00','2008-02-07 00:00','2008-03-25 00:00','2008-04-02 00:00','2008-08-27 00:00','2009-03-18 00:00','2009-06-15 00:00','2010-06-18 00:00','2010-12-31 00:00','2011-01-18 00:00','2012-06-26 00:00','2012-10-18 00:00','2012-11-06 00:00','2013-02-26 00:00','2013-06-23 00:00','2014-03-14 00:00','2014-05-14 00:00'))
class NnOpticalPmMonType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189)));namedValues=NamedValues(*(('cvSectionRxNe',1),('esSectionRxNe',2),('sesSectionRxNe',3),('sefsSectionRxNe',4),('cvSectionTxNe',5),('esSectionTxNe',6),('sesSectionTxNe',7),('cvLineRxNe',8),('esLineRxNe',9),('sesLineRxNe',10),('uasLineRxNe',11),('fcLineRxNe',12),('cvLineTxNe',13),('esLineTxNe',14),('sesLineTxNe',15),('uasLineTxNe',16),('fcLineTxNe',17),('inframesEthRxNe',18),('fcserrEthRxNe',19),('frtoolongsEthRxNe',20),('frtooshortsEthRxNe',21),('outframesEthTxNe',22),('fcserrEthTxNe',23),('cvPCSRxNe',24),('esPCSRxNe',25),('sesPCSRxNe',26),('uasPCSRxNe',27),('cvPCSTxNe',28),('esPCSTxNe',29),('sesPCSTxNe',30),('uasPCSTxNe',31),('oprOCHRxNe',32),('oprnOCHRxNe',33),('optOCHTxNe',34),('optnOCHTxNe',35),('cvOTURxNe',36),('esOTURxNe',37),('sesOTURxNe',38),('sefsOTURxNe',39),('fecOTURxNe',40),('hccsOTURxNe',41),('pfbereOTURxNe',42),('prfberOTURxNe',43),('cvODURxNe',44),('esODURxNe',45),('sesODURxNe',46),('uasODURxNe',47),('fcODURxNe',48),('oprOTSRxNe',49),('optOTSTxNe',50),('orlOTSNaNe',51),('opinOTSNaNe',52),('grpopinOTSNaNe',53),('grpgainOTSNaNe',54),('opoutOTSNaNe',55),('grpoptOTSTxNe',56),('grpopoutOTSNaNe',57),('esEthRxNe',58),('sesEthRxNe',59),('uasEthRxNe',60),('dfrEthRxNe',61),('inframeserrEthRxNe',62),('inframesdiscdsEthRxNe',63),('esEthTxNe',64),('sesEthTxNe',65),('uasEthTxNe',66),('dfrEthTxNe',67),('outframeserrEthTxNe',68),('outframesdiscdsEthTxNe',69),('esWanRxNe',70),('sesWanRxNe',71),('uasWanRxNe',72),('inframesWanRxNe',73),('inframeserrWanRxNe',74),('outframesWanTxNe',75),('oprMinOTSRxNe',76),('oprMaxOTSRxNe',77),('oprAvgOTSRxNe',78),('optMinOTSTxNe',79),('optMaxOTSTxNe',80),('optAvgOTSTxNe',81),('orlMinOTSNaNe',82),('orlMaxOTSNaNe',83),('orlAvgOTSNaNe',84),('opinMinOTSNaNe',85),('opinMaxOTSNaNe',86),('opinAvgOTSNaNe',87),('grpopinMinOTSNaNe',88),('grpopinMaxOTSNaNe',89),('grpopinAvgOTSNaNe',90),('grpgainMinOTSNaNe',91),('grpgainMaxOTSNaNe',92),('grpgainAvgOTSNaNe',93),('opoutMinOTSNaNe',94),('opoutMaxOTSNaNe',95),('opoutAvgOTSNaNe',96),('grpoptMinOTSTxNe',97),('grpoptMaxOTSTxNe',98),('grpoptAvgOTSTxNe',99),('grpopoutMinOTSNaNe',100),('grpopoutMaxOTSNaNe',101),('grpopoutAvgOTSNaNe',102),('dfrWanRxNe',103),('pscwODURxNe',104),('pscpODURxNe',105),('psdODURxNe',106),('cvLineRxFe',107),('esLineRxFe',108),('sesLineRxFe',109),('uasLineRxFe',110),('fcLineRxFe',111),('cvOTUTxNe',112),('esOTUTxNe',113),('sesOTUTxNe',114),('cvODUTxNe',115),('esODUTxNe',116),('sesODUTxNe',117),('uasODUTxNe',118),('fcODUTxNe',119),('oproscOTSNaNe',120),('oproscMinOTSNaNe',121),('oproscMaxOTSNaNe',122),('oproscAvgOTSNaNe',123),('pscwLineRxNe',124),('pscpLineRxNe',125),('psdLineRxNe',126),('dropgainOTSNaNe',127),('dropgainMinOTSNaNe',128),('dropgainMaxOTSNaNe',129),('dropgainAvgOTSNaNe',130),('dgdMaxOCHRxNe',131),('dgdAvgOCHRxNe',132),('optMinOCHTxNe',133),('optMaxOCHTxNe',134),('optAvgOCHTxNe',135),('prfBerMaxOTURxNe',136),('oprLowOCHRxNe',137),('oprHighOCHRxNe',138),('oprnLowOCHRxNe',139),('oprnHighOCHRxNe',140),('optLowOCHTxNe',141),('optHighOCHTxNe',142),('optnLowOCHTxNe',143),('optnHighOCHTxNe',144),('cvOTURxFe',145),('esOTURxFe',146),('sesOTURxFe',147),('cvODURxFe',148),('esODURxFe',149),('sesODURxFe',150),('uasODURxFe',151),('fcODURxFe',152),('oprnOTSRxNe',153),('sefsSectionTxNe',154),('spanLossOCH',155),('spanLossMinOCH',156),('spanLossMaxOCH',157),('spanLossAvgOCH',158),('qMinOTU',159),('qMaxOTU',160),('qAvgOTU',161),('qStdevOTU',162),('oprMinOCHRxNe',163),('oprMaxOCHRxNe',164),('oprAvgOCHRxNe',165),('optOCHRxNe',166),('optMinOCHRxNe',167),('optMaxOCHRxNe',168),('optAvgOCHRxNe',169),('orlInOTSNaNe',170),('orlInMinOTSNaNe',171),('orlInMaxOTSNaNe',172),('orlInAvgOTSNaNe',173),('orlOutOTSNaNe',174),('orlOutMinOTSNaNe',175),('orlOutMaxOTSNaNe',176),('orlOutAvgOTSNaNe',177),('dmMinODURxNe',178),('dmMaxODURxNe',179),('dmAvgODURxNe',180),('pscwEthRxNe',181),('pscpEthRxNe',182),('psdEthRxNe',183),('remoteInframesEthRxNe',184),('remoteInframesErrEthRxNe',185),('remoteFcsErrEthRxNe',186),('remoteOutframesEthTxNe',187),('remoteOutframesDiscdsEthTxNe',188),('uncfecblkOtuRxNe',189)))
class NnOpticalPmUnits(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('dB',2),('dBm',3),('percent',4),('ber',5),('pS',6)))
class NnOpticalPmValidity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notApplicable',1),('complete',2),('partial',3),('adjusted',4)))
_NnOpticalPmObjects_ObjectIdentity=ObjectIdentity
nnOpticalPmObjects=_NnOpticalPmObjects_ObjectIdentity((1,3,6,1,4,1,562,68,10,1,1))
_NnOpticalPmRecent_ObjectIdentity=ObjectIdentity
nnOpticalPmRecent=_NnOpticalPmRecent_ObjectIdentity((1,3,6,1,4,1,562,68,10,1,1,1))
_NnOpticalPmRecentTable_Object=MibTable
nnOpticalPmRecentTable=_NnOpticalPmRecentTable_Object((1,3,6,1,4,1,562,68,10,1,1,1,1))
if mibBuilder.loadTexts:nnOpticalPmRecentTable.setStatus(_A)
_NnOpticalPmRecentEntry_Object=MibTableRow
nnOpticalPmRecentEntry=_NnOpticalPmRecentEntry_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1))
nnOpticalPmRecentEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:nnOpticalPmRecentEntry.setStatus(_A)
_NnOpticalPmRecentIfIndex_Type=Integer32
_NnOpticalPmRecentIfIndex_Object=MibTableColumn
nnOpticalPmRecentIfIndex=_NnOpticalPmRecentIfIndex_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,1),_NnOpticalPmRecentIfIndex_Type())
nnOpticalPmRecentIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmRecentIfIndex.setStatus(_A)
_NnOpticalPmRecentMonType_Type=NnOpticalPmMonType
_NnOpticalPmRecentMonType_Object=MibTableColumn
nnOpticalPmRecentMonType=_NnOpticalPmRecentMonType_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,2),_NnOpticalPmRecentMonType_Type())
nnOpticalPmRecentMonType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmRecentMonType.setStatus(_A)
_NnOpticalPmRecentIfIndexDescr_Type=SnmpAdminString
_NnOpticalPmRecentIfIndexDescr_Object=MibTableColumn
nnOpticalPmRecentIfIndexDescr=_NnOpticalPmRecentIfIndexDescr_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,3),_NnOpticalPmRecentIfIndexDescr_Type())
nnOpticalPmRecentIfIndexDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmRecentIfIndexDescr.setStatus(_A)
_NnOpticalPmRecentMonTypeDescr_Type=SnmpAdminString
_NnOpticalPmRecentMonTypeDescr_Object=MibTableColumn
nnOpticalPmRecentMonTypeDescr=_NnOpticalPmRecentMonTypeDescr_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,4),_NnOpticalPmRecentMonTypeDescr_Type())
nnOpticalPmRecentMonTypeDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmRecentMonTypeDescr.setStatus(_A)
_NnOpticalPmRecentUnits_Type=NnOpticalPmUnits
_NnOpticalPmRecentUnits_Object=MibTableColumn
nnOpticalPmRecentUnits=_NnOpticalPmRecentUnits_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,5),_NnOpticalPmRecentUnits_Type())
nnOpticalPmRecentUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmRecentUnits.setStatus(_A)
_NnOpticalPmCurr15MinValue_Type=SnmpAdminString
_NnOpticalPmCurr15MinValue_Object=MibTableColumn
nnOpticalPmCurr15MinValue=_NnOpticalPmCurr15MinValue_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,6),_NnOpticalPmCurr15MinValue_Type())
nnOpticalPmCurr15MinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmCurr15MinValue.setStatus(_A)
_NnOpticalPmCurr15MinValidity_Type=NnOpticalPmValidity
_NnOpticalPmCurr15MinValidity_Object=MibTableColumn
nnOpticalPmCurr15MinValidity=_NnOpticalPmCurr15MinValidity_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,7),_NnOpticalPmCurr15MinValidity_Type())
nnOpticalPmCurr15MinValidity.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmCurr15MinValidity.setStatus(_A)
_NnOpticalPmCurr15MinDateAndTime_Type=DateAndTime
_NnOpticalPmCurr15MinDateAndTime_Object=MibTableColumn
nnOpticalPmCurr15MinDateAndTime=_NnOpticalPmCurr15MinDateAndTime_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,8),_NnOpticalPmCurr15MinDateAndTime_Type())
nnOpticalPmCurr15MinDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmCurr15MinDateAndTime.setStatus(_A)
_NnOpticalPmPrev15MinValue_Type=SnmpAdminString
_NnOpticalPmPrev15MinValue_Object=MibTableColumn
nnOpticalPmPrev15MinValue=_NnOpticalPmPrev15MinValue_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,9),_NnOpticalPmPrev15MinValue_Type())
nnOpticalPmPrev15MinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmPrev15MinValue.setStatus(_A)
_NnOpticalPmPrev15MinValidity_Type=NnOpticalPmValidity
_NnOpticalPmPrev15MinValidity_Object=MibTableColumn
nnOpticalPmPrev15MinValidity=_NnOpticalPmPrev15MinValidity_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,10),_NnOpticalPmPrev15MinValidity_Type())
nnOpticalPmPrev15MinValidity.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmPrev15MinValidity.setStatus(_A)
_NnOpticalPmPrev15MinDateAndTime_Type=DateAndTime
_NnOpticalPmPrev15MinDateAndTime_Object=MibTableColumn
nnOpticalPmPrev15MinDateAndTime=_NnOpticalPmPrev15MinDateAndTime_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,11),_NnOpticalPmPrev15MinDateAndTime_Type())
nnOpticalPmPrev15MinDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmPrev15MinDateAndTime.setStatus(_A)
_NnOpticalPmCurrDayValue_Type=SnmpAdminString
_NnOpticalPmCurrDayValue_Object=MibTableColumn
nnOpticalPmCurrDayValue=_NnOpticalPmCurrDayValue_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,12),_NnOpticalPmCurrDayValue_Type())
nnOpticalPmCurrDayValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmCurrDayValue.setStatus(_A)
_NnOpticalPmCurrDayValidity_Type=NnOpticalPmValidity
_NnOpticalPmCurrDayValidity_Object=MibTableColumn
nnOpticalPmCurrDayValidity=_NnOpticalPmCurrDayValidity_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,13),_NnOpticalPmCurrDayValidity_Type())
nnOpticalPmCurrDayValidity.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmCurrDayValidity.setStatus(_A)
_NnOpticalPmCurrDayDateAndTime_Type=DateAndTime
_NnOpticalPmCurrDayDateAndTime_Object=MibTableColumn
nnOpticalPmCurrDayDateAndTime=_NnOpticalPmCurrDayDateAndTime_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,14),_NnOpticalPmCurrDayDateAndTime_Type())
nnOpticalPmCurrDayDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmCurrDayDateAndTime.setStatus(_A)
_NnOpticalPmPrevDayValue_Type=SnmpAdminString
_NnOpticalPmPrevDayValue_Object=MibTableColumn
nnOpticalPmPrevDayValue=_NnOpticalPmPrevDayValue_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,15),_NnOpticalPmPrevDayValue_Type())
nnOpticalPmPrevDayValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmPrevDayValue.setStatus(_A)
_NnOpticalPmPrevDayValidity_Type=NnOpticalPmValidity
_NnOpticalPmPrevDayValidity_Object=MibTableColumn
nnOpticalPmPrevDayValidity=_NnOpticalPmPrevDayValidity_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,16),_NnOpticalPmPrevDayValidity_Type())
nnOpticalPmPrevDayValidity.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmPrevDayValidity.setStatus(_A)
_NnOpticalPmPrevDayDateAndTime_Type=DateAndTime
_NnOpticalPmPrevDayDateAndTime_Object=MibTableColumn
nnOpticalPmPrevDayDateAndTime=_NnOpticalPmPrevDayDateAndTime_Object((1,3,6,1,4,1,562,68,10,1,1,1,1,1,17),_NnOpticalPmPrevDayDateAndTime_Type())
nnOpticalPmPrevDayDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmPrevDayDateAndTime.setStatus(_A)
_NnOpticalPmUntimed_ObjectIdentity=ObjectIdentity
nnOpticalPmUntimed=_NnOpticalPmUntimed_ObjectIdentity((1,3,6,1,4,1,562,68,10,1,1,2))
_NnOpticalPmUntTable_Object=MibTable
nnOpticalPmUntTable=_NnOpticalPmUntTable_Object((1,3,6,1,4,1,562,68,10,1,1,2,1))
if mibBuilder.loadTexts:nnOpticalPmUntTable.setStatus(_A)
_NnOpticalPmUntEntry_Object=MibTableRow
nnOpticalPmUntEntry=_NnOpticalPmUntEntry_Object((1,3,6,1,4,1,562,68,10,1,1,2,1,1))
nnOpticalPmUntEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:nnOpticalPmUntEntry.setStatus(_A)
_NnOpticalPmUntIfIndex_Type=Integer32
_NnOpticalPmUntIfIndex_Object=MibTableColumn
nnOpticalPmUntIfIndex=_NnOpticalPmUntIfIndex_Object((1,3,6,1,4,1,562,68,10,1,1,2,1,1,1),_NnOpticalPmUntIfIndex_Type())
nnOpticalPmUntIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmUntIfIndex.setStatus(_A)
_NnOpticalPmUntMonType_Type=NnOpticalPmMonType
_NnOpticalPmUntMonType_Object=MibTableColumn
nnOpticalPmUntMonType=_NnOpticalPmUntMonType_Object((1,3,6,1,4,1,562,68,10,1,1,2,1,1,2),_NnOpticalPmUntMonType_Type())
nnOpticalPmUntMonType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmUntMonType.setStatus(_A)
_NnOpticalPmUntIfIndexDescr_Type=SnmpAdminString
_NnOpticalPmUntIfIndexDescr_Object=MibTableColumn
nnOpticalPmUntIfIndexDescr=_NnOpticalPmUntIfIndexDescr_Object((1,3,6,1,4,1,562,68,10,1,1,2,1,1,3),_NnOpticalPmUntIfIndexDescr_Type())
nnOpticalPmUntIfIndexDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmUntIfIndexDescr.setStatus(_A)
_NnOpticalPmUntMonTypeDescr_Type=SnmpAdminString
_NnOpticalPmUntMonTypeDescr_Object=MibTableColumn
nnOpticalPmUntMonTypeDescr=_NnOpticalPmUntMonTypeDescr_Object((1,3,6,1,4,1,562,68,10,1,1,2,1,1,4),_NnOpticalPmUntMonTypeDescr_Type())
nnOpticalPmUntMonTypeDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmUntMonTypeDescr.setStatus(_A)
_NnOpticalPmUntUnits_Type=NnOpticalPmUnits
_NnOpticalPmUntUnits_Object=MibTableColumn
nnOpticalPmUntUnits=_NnOpticalPmUntUnits_Object((1,3,6,1,4,1,562,68,10,1,1,2,1,1,5),_NnOpticalPmUntUnits_Type())
nnOpticalPmUntUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmUntUnits.setStatus(_A)
_NnOpticalPmUntValue_Type=SnmpAdminString
_NnOpticalPmUntValue_Object=MibTableColumn
nnOpticalPmUntValue=_NnOpticalPmUntValue_Object((1,3,6,1,4,1,562,68,10,1,1,2,1,1,6),_NnOpticalPmUntValue_Type())
nnOpticalPmUntValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmUntValue.setStatus(_A)
_NnOpticalPmUntValidity_Type=NnOpticalPmValidity
_NnOpticalPmUntValidity_Object=MibTableColumn
nnOpticalPmUntValidity=_NnOpticalPmUntValidity_Object((1,3,6,1,4,1,562,68,10,1,1,2,1,1,7),_NnOpticalPmUntValidity_Type())
nnOpticalPmUntValidity.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmUntValidity.setStatus(_A)
_NnOpticalPmUntDateAndTime_Type=DateAndTime
_NnOpticalPmUntDateAndTime_Object=MibTableColumn
nnOpticalPmUntDateAndTime=_NnOpticalPmUntDateAndTime_Object((1,3,6,1,4,1,562,68,10,1,1,2,1,1,8),_NnOpticalPmUntDateAndTime_Type())
nnOpticalPmUntDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmUntDateAndTime.setStatus(_A)
_NnOpticalPmBaseline_ObjectIdentity=ObjectIdentity
nnOpticalPmBaseline=_NnOpticalPmBaseline_ObjectIdentity((1,3,6,1,4,1,562,68,10,1,1,3))
_NnOpticalPmBaslnTable_Object=MibTable
nnOpticalPmBaslnTable=_NnOpticalPmBaslnTable_Object((1,3,6,1,4,1,562,68,10,1,1,3,1))
if mibBuilder.loadTexts:nnOpticalPmBaslnTable.setStatus(_A)
_NnOpticalPmBaslnEntry_Object=MibTableRow
nnOpticalPmBaslnEntry=_NnOpticalPmBaslnEntry_Object((1,3,6,1,4,1,562,68,10,1,1,3,1,1))
nnOpticalPmBaslnEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:nnOpticalPmBaslnEntry.setStatus(_A)
_NnOpticalPmBaslnIfIndex_Type=Integer32
_NnOpticalPmBaslnIfIndex_Object=MibTableColumn
nnOpticalPmBaslnIfIndex=_NnOpticalPmBaslnIfIndex_Object((1,3,6,1,4,1,562,68,10,1,1,3,1,1,1),_NnOpticalPmBaslnIfIndex_Type())
nnOpticalPmBaslnIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmBaslnIfIndex.setStatus(_A)
_NnOpticalPmBaslnMonType_Type=NnOpticalPmMonType
_NnOpticalPmBaslnMonType_Object=MibTableColumn
nnOpticalPmBaslnMonType=_NnOpticalPmBaslnMonType_Object((1,3,6,1,4,1,562,68,10,1,1,3,1,1,2),_NnOpticalPmBaslnMonType_Type())
nnOpticalPmBaslnMonType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmBaslnMonType.setStatus(_A)
_NnOpticalPmBaslnIfIndexDescr_Type=SnmpAdminString
_NnOpticalPmBaslnIfIndexDescr_Object=MibTableColumn
nnOpticalPmBaslnIfIndexDescr=_NnOpticalPmBaslnIfIndexDescr_Object((1,3,6,1,4,1,562,68,10,1,1,3,1,1,3),_NnOpticalPmBaslnIfIndexDescr_Type())
nnOpticalPmBaslnIfIndexDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmBaslnIfIndexDescr.setStatus(_A)
_NnOpticalPmBaslnMonTypeDescr_Type=SnmpAdminString
_NnOpticalPmBaslnMonTypeDescr_Object=MibTableColumn
nnOpticalPmBaslnMonTypeDescr=_NnOpticalPmBaslnMonTypeDescr_Object((1,3,6,1,4,1,562,68,10,1,1,3,1,1,4),_NnOpticalPmBaslnMonTypeDescr_Type())
nnOpticalPmBaslnMonTypeDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmBaslnMonTypeDescr.setStatus(_A)
_NnOpticalPmBaslnUnits_Type=NnOpticalPmUnits
_NnOpticalPmBaslnUnits_Object=MibTableColumn
nnOpticalPmBaslnUnits=_NnOpticalPmBaslnUnits_Object((1,3,6,1,4,1,562,68,10,1,1,3,1,1,5),_NnOpticalPmBaslnUnits_Type())
nnOpticalPmBaslnUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmBaslnUnits.setStatus(_A)
_NnOpticalPmBaslnValue_Type=SnmpAdminString
_NnOpticalPmBaslnValue_Object=MibTableColumn
nnOpticalPmBaslnValue=_NnOpticalPmBaslnValue_Object((1,3,6,1,4,1,562,68,10,1,1,3,1,1,6),_NnOpticalPmBaslnValue_Type())
nnOpticalPmBaslnValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmBaslnValue.setStatus(_A)
_NnOpticalPmBaslnValidity_Type=NnOpticalPmValidity
_NnOpticalPmBaslnValidity_Object=MibTableColumn
nnOpticalPmBaslnValidity=_NnOpticalPmBaslnValidity_Object((1,3,6,1,4,1,562,68,10,1,1,3,1,1,7),_NnOpticalPmBaslnValidity_Type())
nnOpticalPmBaslnValidity.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmBaslnValidity.setStatus(_A)
_NnOpticalPmBaslnDateAndTime_Type=DateAndTime
_NnOpticalPmBaslnDateAndTime_Object=MibTableColumn
nnOpticalPmBaslnDateAndTime=_NnOpticalPmBaslnDateAndTime_Object((1,3,6,1,4,1,562,68,10,1,1,3,1,1,8),_NnOpticalPmBaslnDateAndTime_Type())
nnOpticalPmBaslnDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmBaslnDateAndTime.setStatus(_A)
_NnOpticalPmTimed_ObjectIdentity=ObjectIdentity
nnOpticalPmTimed=_NnOpticalPmTimed_ObjectIdentity((1,3,6,1,4,1,562,68,10,1,1,4))
_NnOpticalPm15Min_ObjectIdentity=ObjectIdentity
nnOpticalPm15Min=_NnOpticalPm15Min_ObjectIdentity((1,3,6,1,4,1,562,68,10,1,1,4,1))
_NnOpticalPm15MinTable_Object=MibTable
nnOpticalPm15MinTable=_NnOpticalPm15MinTable_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1))
if mibBuilder.loadTexts:nnOpticalPm15MinTable.setStatus(_A)
_NnOpticalPm15MinEntry_Object=MibTableRow
nnOpticalPm15MinEntry=_NnOpticalPm15MinEntry_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1))
nnOpticalPm15MinEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:nnOpticalPm15MinEntry.setStatus(_A)
_NnOpticalPm15MinIfIndex_Type=Integer32
_NnOpticalPm15MinIfIndex_Object=MibTableColumn
nnOpticalPm15MinIfIndex=_NnOpticalPm15MinIfIndex_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1,1),_NnOpticalPm15MinIfIndex_Type())
nnOpticalPm15MinIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPm15MinIfIndex.setStatus(_A)
_NnOpticalPm15MinIntIndex_Type=Integer32
_NnOpticalPm15MinIntIndex_Object=MibTableColumn
nnOpticalPm15MinIntIndex=_NnOpticalPm15MinIntIndex_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1,2),_NnOpticalPm15MinIntIndex_Type())
nnOpticalPm15MinIntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPm15MinIntIndex.setStatus(_A)
_NnOpticalPm15MinMonType_Type=NnOpticalPmMonType
_NnOpticalPm15MinMonType_Object=MibTableColumn
nnOpticalPm15MinMonType=_NnOpticalPm15MinMonType_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1,3),_NnOpticalPm15MinMonType_Type())
nnOpticalPm15MinMonType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPm15MinMonType.setStatus(_A)
_NnOpticalPm15MinIfIndexDescr_Type=SnmpAdminString
_NnOpticalPm15MinIfIndexDescr_Object=MibTableColumn
nnOpticalPm15MinIfIndexDescr=_NnOpticalPm15MinIfIndexDescr_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1,4),_NnOpticalPm15MinIfIndexDescr_Type())
nnOpticalPm15MinIfIndexDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPm15MinIfIndexDescr.setStatus(_A)
_NnOpticalPm15MinMonTypeDescr_Type=SnmpAdminString
_NnOpticalPm15MinMonTypeDescr_Object=MibTableColumn
nnOpticalPm15MinMonTypeDescr=_NnOpticalPm15MinMonTypeDescr_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1,5),_NnOpticalPm15MinMonTypeDescr_Type())
nnOpticalPm15MinMonTypeDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPm15MinMonTypeDescr.setStatus(_A)
_NnOpticalPm15MinUnits_Type=NnOpticalPmUnits
_NnOpticalPm15MinUnits_Object=MibTableColumn
nnOpticalPm15MinUnits=_NnOpticalPm15MinUnits_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1,6),_NnOpticalPm15MinUnits_Type())
nnOpticalPm15MinUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPm15MinUnits.setStatus(_A)
_NnOpticalPm15MinValue_Type=SnmpAdminString
_NnOpticalPm15MinValue_Object=MibTableColumn
nnOpticalPm15MinValue=_NnOpticalPm15MinValue_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1,7),_NnOpticalPm15MinValue_Type())
nnOpticalPm15MinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPm15MinValue.setStatus(_A)
_NnOpticalPm15MinValidity_Type=NnOpticalPmValidity
_NnOpticalPm15MinValidity_Object=MibTableColumn
nnOpticalPm15MinValidity=_NnOpticalPm15MinValidity_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1,8),_NnOpticalPm15MinValidity_Type())
nnOpticalPm15MinValidity.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPm15MinValidity.setStatus(_A)
_NnOpticalPm15MinDateAndTime_Type=DateAndTime
_NnOpticalPm15MinDateAndTime_Object=MibTableColumn
nnOpticalPm15MinDateAndTime=_NnOpticalPm15MinDateAndTime_Object((1,3,6,1,4,1,562,68,10,1,1,4,1,1,1,9),_NnOpticalPm15MinDateAndTime_Type())
nnOpticalPm15MinDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPm15MinDateAndTime.setStatus(_A)
_NnOpticalPmDay_ObjectIdentity=ObjectIdentity
nnOpticalPmDay=_NnOpticalPmDay_ObjectIdentity((1,3,6,1,4,1,562,68,10,1,1,4,2))
_NnOpticalPmDayTable_Object=MibTable
nnOpticalPmDayTable=_NnOpticalPmDayTable_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1))
if mibBuilder.loadTexts:nnOpticalPmDayTable.setStatus(_A)
_NnOpticalPmDayEntry_Object=MibTableRow
nnOpticalPmDayEntry=_NnOpticalPmDayEntry_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1))
nnOpticalPmDayEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:nnOpticalPmDayEntry.setStatus(_A)
_NnOpticalPmDayIfIndex_Type=Integer32
_NnOpticalPmDayIfIndex_Object=MibTableColumn
nnOpticalPmDayIfIndex=_NnOpticalPmDayIfIndex_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1,1),_NnOpticalPmDayIfIndex_Type())
nnOpticalPmDayIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmDayIfIndex.setStatus(_A)
_NnOpticalPmDayIntIndex_Type=Integer32
_NnOpticalPmDayIntIndex_Object=MibTableColumn
nnOpticalPmDayIntIndex=_NnOpticalPmDayIntIndex_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1,2),_NnOpticalPmDayIntIndex_Type())
nnOpticalPmDayIntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmDayIntIndex.setStatus(_A)
_NnOpticalPmDayMonType_Type=NnOpticalPmMonType
_NnOpticalPmDayMonType_Object=MibTableColumn
nnOpticalPmDayMonType=_NnOpticalPmDayMonType_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1,3),_NnOpticalPmDayMonType_Type())
nnOpticalPmDayMonType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmDayMonType.setStatus(_A)
_NnOpticalPmDayIfIndexDescr_Type=SnmpAdminString
_NnOpticalPmDayIfIndexDescr_Object=MibTableColumn
nnOpticalPmDayIfIndexDescr=_NnOpticalPmDayIfIndexDescr_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1,4),_NnOpticalPmDayIfIndexDescr_Type())
nnOpticalPmDayIfIndexDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmDayIfIndexDescr.setStatus(_A)
_NnOpticalPmDayMonTypeDescr_Type=SnmpAdminString
_NnOpticalPmDayMonTypeDescr_Object=MibTableColumn
nnOpticalPmDayMonTypeDescr=_NnOpticalPmDayMonTypeDescr_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1,5),_NnOpticalPmDayMonTypeDescr_Type())
nnOpticalPmDayMonTypeDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmDayMonTypeDescr.setStatus(_A)
_NnOpticalPmDayUnits_Type=NnOpticalPmUnits
_NnOpticalPmDayUnits_Object=MibTableColumn
nnOpticalPmDayUnits=_NnOpticalPmDayUnits_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1,6),_NnOpticalPmDayUnits_Type())
nnOpticalPmDayUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmDayUnits.setStatus(_A)
_NnOpticalPmDayValue_Type=SnmpAdminString
_NnOpticalPmDayValue_Object=MibTableColumn
nnOpticalPmDayValue=_NnOpticalPmDayValue_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1,7),_NnOpticalPmDayValue_Type())
nnOpticalPmDayValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmDayValue.setStatus(_A)
_NnOpticalPmDayValidity_Type=NnOpticalPmValidity
_NnOpticalPmDayValidity_Object=MibTableColumn
nnOpticalPmDayValidity=_NnOpticalPmDayValidity_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1,8),_NnOpticalPmDayValidity_Type())
nnOpticalPmDayValidity.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmDayValidity.setStatus(_A)
_NnOpticalPmDayDateAndTime_Type=DateAndTime
_NnOpticalPmDayDateAndTime_Object=MibTableColumn
nnOpticalPmDayDateAndTime=_NnOpticalPmDayDateAndTime_Object((1,3,6,1,4,1,562,68,10,1,1,4,2,1,1,9),_NnOpticalPmDayDateAndTime_Type())
nnOpticalPmDayDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnOpticalPmDayDateAndTime.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'NnOpticalPmMonType':NnOpticalPmMonType,'NnOpticalPmUnits':NnOpticalPmUnits,'NnOpticalPmValidity':NnOpticalPmValidity,'nnOpticalPmMIB':nnOpticalPmMIB,'nnOpticalPmObjects':nnOpticalPmObjects,'nnOpticalPmRecent':nnOpticalPmRecent,'nnOpticalPmRecentTable':nnOpticalPmRecentTable,'nnOpticalPmRecentEntry':nnOpticalPmRecentEntry,_D:nnOpticalPmRecentIfIndex,_E:nnOpticalPmRecentMonType,'nnOpticalPmRecentIfIndexDescr':nnOpticalPmRecentIfIndexDescr,'nnOpticalPmRecentMonTypeDescr':nnOpticalPmRecentMonTypeDescr,'nnOpticalPmRecentUnits':nnOpticalPmRecentUnits,'nnOpticalPmCurr15MinValue':nnOpticalPmCurr15MinValue,'nnOpticalPmCurr15MinValidity':nnOpticalPmCurr15MinValidity,'nnOpticalPmCurr15MinDateAndTime':nnOpticalPmCurr15MinDateAndTime,'nnOpticalPmPrev15MinValue':nnOpticalPmPrev15MinValue,'nnOpticalPmPrev15MinValidity':nnOpticalPmPrev15MinValidity,'nnOpticalPmPrev15MinDateAndTime':nnOpticalPmPrev15MinDateAndTime,'nnOpticalPmCurrDayValue':nnOpticalPmCurrDayValue,'nnOpticalPmCurrDayValidity':nnOpticalPmCurrDayValidity,'nnOpticalPmCurrDayDateAndTime':nnOpticalPmCurrDayDateAndTime,'nnOpticalPmPrevDayValue':nnOpticalPmPrevDayValue,'nnOpticalPmPrevDayValidity':nnOpticalPmPrevDayValidity,'nnOpticalPmPrevDayDateAndTime':nnOpticalPmPrevDayDateAndTime,'nnOpticalPmUntimed':nnOpticalPmUntimed,'nnOpticalPmUntTable':nnOpticalPmUntTable,'nnOpticalPmUntEntry':nnOpticalPmUntEntry,_F:nnOpticalPmUntIfIndex,_G:nnOpticalPmUntMonType,'nnOpticalPmUntIfIndexDescr':nnOpticalPmUntIfIndexDescr,'nnOpticalPmUntMonTypeDescr':nnOpticalPmUntMonTypeDescr,'nnOpticalPmUntUnits':nnOpticalPmUntUnits,'nnOpticalPmUntValue':nnOpticalPmUntValue,'nnOpticalPmUntValidity':nnOpticalPmUntValidity,'nnOpticalPmUntDateAndTime':nnOpticalPmUntDateAndTime,'nnOpticalPmBaseline':nnOpticalPmBaseline,'nnOpticalPmBaslnTable':nnOpticalPmBaslnTable,'nnOpticalPmBaslnEntry':nnOpticalPmBaslnEntry,_H:nnOpticalPmBaslnIfIndex,_I:nnOpticalPmBaslnMonType,'nnOpticalPmBaslnIfIndexDescr':nnOpticalPmBaslnIfIndexDescr,'nnOpticalPmBaslnMonTypeDescr':nnOpticalPmBaslnMonTypeDescr,'nnOpticalPmBaslnUnits':nnOpticalPmBaslnUnits,'nnOpticalPmBaslnValue':nnOpticalPmBaslnValue,'nnOpticalPmBaslnValidity':nnOpticalPmBaslnValidity,'nnOpticalPmBaslnDateAndTime':nnOpticalPmBaslnDateAndTime,'nnOpticalPmTimed':nnOpticalPmTimed,'nnOpticalPm15Min':nnOpticalPm15Min,'nnOpticalPm15MinTable':nnOpticalPm15MinTable,'nnOpticalPm15MinEntry':nnOpticalPm15MinEntry,_J:nnOpticalPm15MinIfIndex,_K:nnOpticalPm15MinIntIndex,_L:nnOpticalPm15MinMonType,'nnOpticalPm15MinIfIndexDescr':nnOpticalPm15MinIfIndexDescr,'nnOpticalPm15MinMonTypeDescr':nnOpticalPm15MinMonTypeDescr,'nnOpticalPm15MinUnits':nnOpticalPm15MinUnits,'nnOpticalPm15MinValue':nnOpticalPm15MinValue,'nnOpticalPm15MinValidity':nnOpticalPm15MinValidity,'nnOpticalPm15MinDateAndTime':nnOpticalPm15MinDateAndTime,'nnOpticalPmDay':nnOpticalPmDay,'nnOpticalPmDayTable':nnOpticalPmDayTable,'nnOpticalPmDayEntry':nnOpticalPmDayEntry,_M:nnOpticalPmDayIfIndex,_N:nnOpticalPmDayIntIndex,_O:nnOpticalPmDayMonType,'nnOpticalPmDayIfIndexDescr':nnOpticalPmDayIfIndexDescr,'nnOpticalPmDayMonTypeDescr':nnOpticalPmDayMonTypeDescr,'nnOpticalPmDayUnits':nnOpticalPmDayUnits,'nnOpticalPmDayValue':nnOpticalPmDayValue,'nnOpticalPmDayValidity':nnOpticalPmDayValidity,'nnOpticalPmDayDateAndTime':nnOpticalPmDayDateAndTime})