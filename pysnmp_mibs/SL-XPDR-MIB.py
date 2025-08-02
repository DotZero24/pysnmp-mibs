_K='oduXcConnConfigP2'
_J='oduXcConnConfigP1'
_I='standby'
_H='xpdrConnConfigIf2'
_G='xpdrConnConfigIf1'
_F='read-create'
_E='Integer32'
_D='read-only'
_C='SL-XPDR-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
slXpdr=ModuleIdentity((1,3,6,1,4,1,4515,1,8))
class XpdrServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,170,171,1701)));namedValues=NamedValues(*(('ds3Sts1',1),('fe',2),('escon',3),('dvbVideo',4),('fc1gFicon',5),('gbE',6),('fc2g',7),('oc3Stm1',8),('oc12Stm4',9),('oc48Stm16',10),('other',11),('fc4g',12),('infiniband25G',13),('otn27g',14),('oc24gpon',15),('smpteSdi',16),('copperFe',17),('copperGbe',18),('mux2GbE',19),('mux4GbE',20),('xpdr5G',21),('ficon1g',22),('ficon2g',23),('stm1',24),('stm4',25),('stm16',26),('gpon248',27),('ficon4g',28),('eth10m',29),('xfp10oc192',30),('xfp10stm64',31),('xfp10GbEWan',32),('xfp10GbELan',33),('xfp10otu2',34),('xfp10GFC',35),('xfp10GbEWanStm64',36),('mux1GbE',37),('mux1GbERegen',38),('mux2GbERegen',39),('mux4GbERegen',40),('fc8g',41),('ficon8g',42),('mux10GbE',43),('syncEgbE',44),('otu1e',50),('otu2e',51),('otu1f',52),('otu2f',53),('oc192ToOtu2',54),('stm64ToOtu2',55),('gbe10WanToOtu2',56),('gbe10LanToOtu2A',57),('gbe10LanToOtu1e',58),('gbe10LanToOtu2e',59),('gbe10LanToOtu2B',60),('fc10LanToOtu1f',61),('fc10LanToOtu2f',62),('fc8LanToOtu2',63),('otu3',64),('oc768',65),('stm256',66),('otu4',67),('gbe40lan',68),('gbe100lan',69),('fc16g',70),('smpteHdSdi',71),('smpteSdSdi',72),('smpte3gSdi',73),('smpte3dSdi',74),('smpteHdSdiNtsc',75),('smpte3gSdiNtsc',76),('fc16gNoIsl',77),('cpri1',81),('cpri2',82),('cpri3',83),('cpri4',84),('cpri5',85),('cpri6',86),('cpri7',87),('enc10GbELan',91),('enc1GbELan',92),('encfc1g',93),('encfc2g',94),('encfc4g',95),('encfc8g',96),('encfc16g',97),('encfc10g',98),('copper10m',170),('copper10mAn',171),('copperFeAn',1701)))
_SlXpdrConn_ObjectIdentity=ObjectIdentity
slXpdrConn=_SlXpdrConn_ObjectIdentity((1,3,6,1,4,1,4515,1,8,1))
_XpdrConnConfigTable_Object=MibTable
xpdrConnConfigTable=_XpdrConnConfigTable_Object((1,3,6,1,4,1,4515,1,8,1,1))
if mibBuilder.loadTexts:xpdrConnConfigTable.setStatus(_A)
_XpdrConnConfigEntry_Object=MibTableRow
xpdrConnConfigEntry=_XpdrConnConfigEntry_Object((1,3,6,1,4,1,4515,1,8,1,1,1))
xpdrConnConfigEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:xpdrConnConfigEntry.setStatus(_A)
_XpdrConnConfigIf1_Type=InterfaceIndex
_XpdrConnConfigIf1_Object=MibTableColumn
xpdrConnConfigIf1=_XpdrConnConfigIf1_Object((1,3,6,1,4,1,4515,1,8,1,1,1,1),_XpdrConnConfigIf1_Type())
xpdrConnConfigIf1.setMaxAccess(_D)
if mibBuilder.loadTexts:xpdrConnConfigIf1.setStatus(_A)
_XpdrConnConfigIf2_Type=InterfaceIndex
_XpdrConnConfigIf2_Object=MibTableColumn
xpdrConnConfigIf2=_XpdrConnConfigIf2_Object((1,3,6,1,4,1,4515,1,8,1,1,1,2),_XpdrConnConfigIf2_Type())
xpdrConnConfigIf2.setMaxAccess(_D)
if mibBuilder.loadTexts:xpdrConnConfigIf2.setStatus(_A)
_XpdrConnConfigRateControlAdmin_Type=Integer32
_XpdrConnConfigRateControlAdmin_Object=MibTableColumn
xpdrConnConfigRateControlAdmin=_XpdrConnConfigRateControlAdmin_Object((1,3,6,1,4,1,4515,1,8,1,1,1,3),_XpdrConnConfigRateControlAdmin_Type())
xpdrConnConfigRateControlAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrConnConfigRateControlAdmin.setStatus(_A)
_XpdrConnConfigRateControlOper_Type=Integer32
_XpdrConnConfigRateControlOper_Object=MibTableColumn
xpdrConnConfigRateControlOper=_XpdrConnConfigRateControlOper_Object((1,3,6,1,4,1,4515,1,8,1,1,1,4),_XpdrConnConfigRateControlOper_Type())
xpdrConnConfigRateControlOper.setMaxAccess(_D)
if mibBuilder.loadTexts:xpdrConnConfigRateControlOper.setStatus(_A)
_XpdrConnConfigLosPropagation_Type=TruthValue
_XpdrConnConfigLosPropagation_Object=MibTableColumn
xpdrConnConfigLosPropagation=_XpdrConnConfigLosPropagation_Object((1,3,6,1,4,1,4515,1,8,1,1,1,5),_XpdrConnConfigLosPropagation_Type())
xpdrConnConfigLosPropagation.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrConnConfigLosPropagation.setStatus(_A)
_XpdrServiceType_Type=XpdrServiceType
_XpdrServiceType_Object=MibTableColumn
xpdrServiceType=_XpdrServiceType_Object((1,3,6,1,4,1,4515,1,8,1,1,1,6),_XpdrServiceType_Type())
xpdrServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrServiceType.setStatus(_A)
_XpdrConnAddMask_Type=Integer32
_XpdrConnAddMask_Object=MibTableColumn
xpdrConnAddMask=_XpdrConnAddMask_Object((1,3,6,1,4,1,4515,1,8,1,1,1,7),_XpdrConnAddMask_Type())
xpdrConnAddMask.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrConnAddMask.setStatus(_A)
class _XpdrMuxInbandAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3)))
_XpdrMuxInbandAdmin_Type.__name__=_E
_XpdrMuxInbandAdmin_Object=MibTableColumn
xpdrMuxInbandAdmin=_XpdrMuxInbandAdmin_Object((1,3,6,1,4,1,4515,1,8,1,1,1,8),_XpdrMuxInbandAdmin_Type())
xpdrMuxInbandAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrMuxInbandAdmin.setStatus(_A)
class _XpdrMuxInbandOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3)))
_XpdrMuxInbandOper_Type.__name__=_E
_XpdrMuxInbandOper_Object=MibTableColumn
xpdrMuxInbandOper=_XpdrMuxInbandOper_Object((1,3,6,1,4,1,4515,1,8,1,1,1,9),_XpdrMuxInbandOper_Type())
xpdrMuxInbandOper.setMaxAccess(_D)
if mibBuilder.loadTexts:xpdrMuxInbandOper.setStatus(_A)
class _XpdrDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bidirectional',1),('unidirectionalTx',2),('unidirectionalRx',3),('loopback',4)))
_XpdrDirection_Type.__name__=_E
_XpdrDirection_Object=MibTableColumn
xpdrDirection=_XpdrDirection_Object((1,3,6,1,4,1,4515,1,8,1,1,1,10),_XpdrDirection_Type())
xpdrDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrDirection.setStatus(_A)
_XpdrConnConfigCpriRateControl_Type=TruthValue
_XpdrConnConfigCpriRateControl_Object=MibTableColumn
xpdrConnConfigCpriRateControl=_XpdrConnConfigCpriRateControl_Object((1,3,6,1,4,1,4515,1,8,1,1,1,11),_XpdrConnConfigCpriRateControl_Type())
xpdrConnConfigCpriRateControl.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrConnConfigCpriRateControl.setStatus(_A)
_XpdrFaultPropagationDelay_Type=Integer32
_XpdrFaultPropagationDelay_Object=MibTableColumn
xpdrFaultPropagationDelay=_XpdrFaultPropagationDelay_Object((1,3,6,1,4,1,4515,1,8,1,1,1,12),_XpdrFaultPropagationDelay_Type())
xpdrFaultPropagationDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrFaultPropagationDelay.setStatus(_A)
_XpdrFecMode_Type=Integer32
_XpdrFecMode_Object=MibTableColumn
xpdrFecMode=_XpdrFecMode_Object((1,3,6,1,4,1,4515,1,8,1,1,1,13),_XpdrFecMode_Type())
xpdrFecMode.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrFecMode.setStatus(_A)
_OduXcConnConfigTable_Object=MibTable
oduXcConnConfigTable=_OduXcConnConfigTable_Object((1,3,6,1,4,1,4515,1,8,1,2))
if mibBuilder.loadTexts:oduXcConnConfigTable.setStatus(_A)
_OduXcConnConfigEntry_Object=MibTableRow
oduXcConnConfigEntry=_OduXcConnConfigEntry_Object((1,3,6,1,4,1,4515,1,8,1,2,1))
oduXcConnConfigEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:oduXcConnConfigEntry.setStatus(_A)
_OduXcConnConfigP1_Type=Integer32
_OduXcConnConfigP1_Object=MibTableColumn
oduXcConnConfigP1=_OduXcConnConfigP1_Object((1,3,6,1,4,1,4515,1,8,1,2,1,1),_OduXcConnConfigP1_Type())
oduXcConnConfigP1.setMaxAccess(_F)
if mibBuilder.loadTexts:oduXcConnConfigP1.setStatus(_A)
_OduXcConnConfigP2_Type=Integer32
_OduXcConnConfigP2_Object=MibTableColumn
oduXcConnConfigP2=_OduXcConnConfigP2_Object((1,3,6,1,4,1,4515,1,8,1,2,1,2),_OduXcConnConfigP2_Type())
oduXcConnConfigP2.setMaxAccess(_F)
if mibBuilder.loadTexts:oduXcConnConfigP2.setStatus(_A)
_OduXcConnConfigProtected_Type=TruthValue
_OduXcConnConfigProtected_Object=MibTableColumn
oduXcConnConfigProtected=_OduXcConnConfigProtected_Object((1,3,6,1,4,1,4515,1,8,1,2,1,3),_OduXcConnConfigProtected_Type())
oduXcConnConfigProtected.setMaxAccess(_F)
if mibBuilder.loadTexts:oduXcConnConfigProtected.setStatus(_A)
_OduXcConnConfigRowStatus_Type=RowStatus
_OduXcConnConfigRowStatus_Object=MibTableColumn
oduXcConnConfigRowStatus=_OduXcConnConfigRowStatus_Object((1,3,6,1,4,1,4515,1,8,1,2,1,4),_OduXcConnConfigRowStatus_Type())
oduXcConnConfigRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:oduXcConnConfigRowStatus.setStatus(_A)
_XpdrOduMappingStatus_Type=Integer32
_XpdrOduMappingStatus_Object=MibScalar
xpdrOduMappingStatus=_XpdrOduMappingStatus_Object((1,3,6,1,4,1,4515,1,8,1,3),_XpdrOduMappingStatus_Type())
xpdrOduMappingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:xpdrOduMappingStatus.setStatus(_A)
_XpdrOduMappingMaskedAdmin_Type=Integer32
_XpdrOduMappingMaskedAdmin_Object=MibScalar
xpdrOduMappingMaskedAdmin=_XpdrOduMappingMaskedAdmin_Object((1,3,6,1,4,1,4515,1,8,1,4),_XpdrOduMappingMaskedAdmin_Type())
xpdrOduMappingMaskedAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:xpdrOduMappingMaskedAdmin.setStatus(_A)
_SlXpdrLastChange_ObjectIdentity=ObjectIdentity
slXpdrLastChange=_SlXpdrLastChange_ObjectIdentity((1,3,6,1,4,1,4515,1,8,6))
_SlXpdrTraps_ObjectIdentity=ObjectIdentity
slXpdrTraps=_SlXpdrTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,8,7))
_SlXpdrTraps0_ObjectIdentity=ObjectIdentity
slXpdrTraps0=_SlXpdrTraps0_ObjectIdentity((1,3,6,1,4,1,4515,1,8,7,0))
xpdrConnConfigTableChange0=NotificationType((1,3,6,1,4,1,4515,1,8,7,0,1))
if mibBuilder.loadTexts:xpdrConnConfigTableChange0.setStatus(_A)
xpdrConnConfigTableChange=NotificationType((1,3,6,1,4,1,4515,1,8,7,1))
if mibBuilder.loadTexts:xpdrConnConfigTableChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'XpdrServiceType':XpdrServiceType,'slXpdr':slXpdr,'slXpdrConn':slXpdrConn,'xpdrConnConfigTable':xpdrConnConfigTable,'xpdrConnConfigEntry':xpdrConnConfigEntry,_G:xpdrConnConfigIf1,_H:xpdrConnConfigIf2,'xpdrConnConfigRateControlAdmin':xpdrConnConfigRateControlAdmin,'xpdrConnConfigRateControlOper':xpdrConnConfigRateControlOper,'xpdrConnConfigLosPropagation':xpdrConnConfigLosPropagation,'xpdrServiceType':xpdrServiceType,'xpdrConnAddMask':xpdrConnAddMask,'xpdrMuxInbandAdmin':xpdrMuxInbandAdmin,'xpdrMuxInbandOper':xpdrMuxInbandOper,'xpdrDirection':xpdrDirection,'xpdrConnConfigCpriRateControl':xpdrConnConfigCpriRateControl,'xpdrFaultPropagationDelay':xpdrFaultPropagationDelay,'xpdrFecMode':xpdrFecMode,'oduXcConnConfigTable':oduXcConnConfigTable,'oduXcConnConfigEntry':oduXcConnConfigEntry,_J:oduXcConnConfigP1,_K:oduXcConnConfigP2,'oduXcConnConfigProtected':oduXcConnConfigProtected,'oduXcConnConfigRowStatus':oduXcConnConfigRowStatus,'xpdrOduMappingStatus':xpdrOduMappingStatus,'xpdrOduMappingMaskedAdmin':xpdrOduMappingMaskedAdmin,'slXpdrLastChange':slXpdrLastChange,'slXpdrTraps':slXpdrTraps,'slXpdrTraps0':slXpdrTraps0,'xpdrConnConfigTableChange0':xpdrConnConfigTableChange0,'xpdrConnConfigTableChange':xpdrConnConfigTableChange})