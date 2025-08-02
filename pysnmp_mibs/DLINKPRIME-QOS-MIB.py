_d='dpQosCoSGroup'
_c='dpQosPortBandwidthCtrlGroup'
_b='dpQosSchedulingGroup'
_a='dpQosCfgSetCos'
_Z='dpQosBandwidthTxRate'
_Y='dpQosBandwidthRxRate'
_X='dpQosSchedulingMode'
_W='limit_512Mbps'
_V='limit_256Mbps'
_U='limit_128Mbps'
_T='limit_64Mbps'
_S='limit_32Mbps'
_R='limit_16Mbps'
_Q='limit_8Mbps'
_P='limit_4Mbps'
_O='limit_2Mbps'
_N='limit_1Mbps'
_M='limit_512Kbps'
_L='limit_256Kbps'
_K='limit_128Kbps'
_J='limit_64Kbps'
_I='limit_32Kbps'
_H='limit_16Kbps'
_G='noLimit'
_F='read-write'
_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='Integer32'
_B='DLINKPRIME-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkPrimeQosMIB=ModuleIdentity((1,3,6,1,4,1,171,15,13))
if mibBuilder.loadTexts:dlinkPrimeQosMIB.setRevisions(('2014-04-26 00:00',))
_DpQosMIBObjects_ObjectIdentity=ObjectIdentity
dpQosMIBObjects=_DpQosMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,13,1))
_DpQosScheduling_ObjectIdentity=ObjectIdentity
dpQosScheduling=_DpQosScheduling_ObjectIdentity((1,3,6,1,4,1,171,15,13,1,1))
_DpQosSchedulingModeTable_Object=MibTable
dpQosSchedulingModeTable=_DpQosSchedulingModeTable_Object((1,3,6,1,4,1,171,15,13,1,1,1))
if mibBuilder.loadTexts:dpQosSchedulingModeTable.setStatus(_A)
_DpQosSchedulingModeEntry_Object=MibTableRow
dpQosSchedulingModeEntry=_DpQosSchedulingModeEntry_Object((1,3,6,1,4,1,171,15,13,1,1,1,1))
dpQosSchedulingModeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dpQosSchedulingModeEntry.setStatus(_A)
class _DpQosSchedulingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sp',1),('wrr',2)))
_DpQosSchedulingMode_Type.__name__=_C
_DpQosSchedulingMode_Object=MibTableColumn
dpQosSchedulingMode=_DpQosSchedulingMode_Object((1,3,6,1,4,1,171,15,13,1,1,1,1,1),_DpQosSchedulingMode_Type())
dpQosSchedulingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:dpQosSchedulingMode.setStatus(_A)
_DpQosBandwidthCtrl_ObjectIdentity=ObjectIdentity
dpQosBandwidthCtrl=_DpQosBandwidthCtrl_ObjectIdentity((1,3,6,1,4,1,171,15,13,1,2))
_DpQosBandwidthCtrlTable_Object=MibTable
dpQosBandwidthCtrlTable=_DpQosBandwidthCtrlTable_Object((1,3,6,1,4,1,171,15,13,1,2,1))
if mibBuilder.loadTexts:dpQosBandwidthCtrlTable.setStatus(_A)
_DpQosBandwidthCtrlEntry_Object=MibTableRow
dpQosBandwidthCtrlEntry=_DpQosBandwidthCtrlEntry_Object((1,3,6,1,4,1,171,15,13,1,2,1,1))
dpQosBandwidthCtrlEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dpQosBandwidthCtrlEntry.setStatus(_A)
class _DpQosBandwidthRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_G,1),('limit_8Kbps',2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),(_O,10),(_P,11),(_Q,12),(_R,13),(_S,14),(_T,15),(_U,16),(_V,17),(_W,18)))
_DpQosBandwidthRxRate_Type.__name__=_C
_DpQosBandwidthRxRate_Object=MibTableColumn
dpQosBandwidthRxRate=_DpQosBandwidthRxRate_Object((1,3,6,1,4,1,171,15,13,1,2,1,1,1),_DpQosBandwidthRxRate_Type())
dpQosBandwidthRxRate.setMaxAccess(_F)
if mibBuilder.loadTexts:dpQosBandwidthRxRate.setStatus(_A)
class _DpQosBandwidthTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_G,1),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),(_O,10),(_P,11),(_Q,12),(_R,13),(_S,14),(_T,15),(_U,16),(_V,17),(_W,18)))
_DpQosBandwidthTxRate_Type.__name__=_C
_DpQosBandwidthTxRate_Object=MibTableColumn
dpQosBandwidthTxRate=_DpQosBandwidthTxRate_Object((1,3,6,1,4,1,171,15,13,1,2,1,1,2),_DpQosBandwidthTxRate_Type())
dpQosBandwidthTxRate.setMaxAccess(_F)
if mibBuilder.loadTexts:dpQosBandwidthTxRate.setStatus(_A)
_DpQosCosCfg_ObjectIdentity=ObjectIdentity
dpQosCosCfg=_DpQosCosCfg_ObjectIdentity((1,3,6,1,4,1,171,15,13,1,3))
_DpQosCosCfgTable_Object=MibTable
dpQosCosCfgTable=_DpQosCosCfgTable_Object((1,3,6,1,4,1,171,15,13,1,3,1))
if mibBuilder.loadTexts:dpQosCosCfgTable.setStatus(_A)
_DpQosCosCfgEntry_Object=MibTableRow
dpQosCosCfgEntry=_DpQosCosCfgEntry_Object((1,3,6,1,4,1,171,15,13,1,3,1,1))
dpQosCosCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dpQosCosCfgEntry.setStatus(_A)
class _DpQosCfgSetCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3),('highest',4)))
_DpQosCfgSetCos_Type.__name__=_C
_DpQosCfgSetCos_Object=MibTableColumn
dpQosCfgSetCos=_DpQosCfgSetCos_Object((1,3,6,1,4,1,171,15,13,1,3,1,1,1),_DpQosCfgSetCos_Type())
dpQosCfgSetCos.setMaxAccess(_F)
if mibBuilder.loadTexts:dpQosCfgSetCos.setStatus(_A)
_DpQosMIBConformance_ObjectIdentity=ObjectIdentity
dpQosMIBConformance=_DpQosMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,13,2))
_DpQosCompliances_ObjectIdentity=ObjectIdentity
dpQosCompliances=_DpQosCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,13,2,1))
_DpQosGroups_ObjectIdentity=ObjectIdentity
dpQosGroups=_DpQosGroups_ObjectIdentity((1,3,6,1,4,1,171,15,13,2,2))
dpQosSchedulingGroup=ObjectGroup((1,3,6,1,4,1,171,15,13,2,2,1))
dpQosSchedulingGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:dpQosSchedulingGroup.setStatus(_A)
dpQosPortBandwidthCtrlGroup=ObjectGroup((1,3,6,1,4,1,171,15,13,2,2,2))
dpQosPortBandwidthCtrlGroup.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:dpQosPortBandwidthCtrlGroup.setStatus(_A)
dpQosCoSGroup=ObjectGroup((1,3,6,1,4,1,171,15,13,2,2,3))
dpQosCoSGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:dpQosCoSGroup.setStatus(_A)
dpQosCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,13,2,1,1))
dpQosCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:dpQosCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeQosMIB':dlinkPrimeQosMIB,'dpQosMIBObjects':dpQosMIBObjects,'dpQosScheduling':dpQosScheduling,'dpQosSchedulingModeTable':dpQosSchedulingModeTable,'dpQosSchedulingModeEntry':dpQosSchedulingModeEntry,_X:dpQosSchedulingMode,'dpQosBandwidthCtrl':dpQosBandwidthCtrl,'dpQosBandwidthCtrlTable':dpQosBandwidthCtrlTable,'dpQosBandwidthCtrlEntry':dpQosBandwidthCtrlEntry,_Y:dpQosBandwidthRxRate,_Z:dpQosBandwidthTxRate,'dpQosCosCfg':dpQosCosCfg,'dpQosCosCfgTable':dpQosCosCfgTable,'dpQosCosCfgEntry':dpQosCosCfgEntry,_a:dpQosCfgSetCos,'dpQosMIBConformance':dpQosMIBConformance,'dpQosCompliances':dpQosCompliances,'dpQosCompliance':dpQosCompliance,'dpQosGroups':dpQosGroups,_b:dpQosSchedulingGroup,_c:dpQosPortBandwidthCtrlGroup,_d:dpQosCoSGroup})