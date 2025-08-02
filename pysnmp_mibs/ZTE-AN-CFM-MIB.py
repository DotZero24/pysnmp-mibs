_b='zxAnCfmMepEntry'
_a='zxAnCfmMaNetEntry'
_Z='zxAnCfmLogicalId'
_Y='zxAnCfmIfType'
_X='zxAnCfmOnu'
_W='zxAnCfmPort'
_V='zxAnCfmSlot'
_U='zxAnCfmShelf'
_T='zxAnCfmRack'
_S='OctetString'
_R='multicastClass1'
_Q='dot1agCfmMepIdentifier'
_P='dot1agCfmMdIndex'
_O='dot1agCfmMaIndex'
_N='disable'
_M='enable'
_L='multicastclass1'
_K='seconds'
_J='not-accessible'
_I='TruthValue'
_H='IEEE8021-CFM-MIB'
_G='unicast'
_F='Unsigned32'
_E='ZTE-AN-CFM-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmMepIdOrZero,dot1agCfmMaIndex,dot1agCfmMaNetEntry,dot1agCfmMdIndex,dot1agCfmMepEntry,dot1agCfmMepIdentifier=mibBuilder.importSymbols(_H,'Dot1agCfmMepIdOrZero',_O,'dot1agCfmMaNetEntry',_P,'dot1agCfmMepEntry',_Q)
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_I)
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnCfmMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,62))
_ZxAnCfmObjects_ObjectIdentity=ObjectIdentity
zxAnCfmObjects=_ZxAnCfmObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,62,1))
_ZxAnCfmGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnCfmGlobalObjects=_ZxAnCfmGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,62,1,1))
class _ZxAnCfmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ZxAnCfmEnable_Type.__name__=_C
_ZxAnCfmEnable_Object=MibScalar
zxAnCfmEnable=_ZxAnCfmEnable_Object((1,3,6,1,4,1,3902,1015,62,1,1,1),_ZxAnCfmEnable_Type())
zxAnCfmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmEnable.setStatus(_A)
_ZxAnCfmMa_ObjectIdentity=ObjectIdentity
zxAnCfmMa=_ZxAnCfmMa_ObjectIdentity((1,3,6,1,4,1,3902,1015,62,1,2))
_ZxAnCfmMaNetTable_Object=MibTable
zxAnCfmMaNetTable=_ZxAnCfmMaNetTable_Object((1,3,6,1,4,1,3902,1015,62,1,2,1))
if mibBuilder.loadTexts:zxAnCfmMaNetTable.setStatus(_A)
_ZxAnCfmMaNetEntry_Object=MibTableRow
zxAnCfmMaNetEntry=_ZxAnCfmMaNetEntry_Object((1,3,6,1,4,1,3902,1015,62,1,2,1,1))
if mibBuilder.loadTexts:zxAnCfmMaNetEntry.setStatus(_A)
class _ZxAnCfmMaNetCcmDaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_L,2)))
_ZxAnCfmMaNetCcmDaType_Type.__name__=_C
_ZxAnCfmMaNetCcmDaType_Object=MibTableColumn
zxAnCfmMaNetCcmDaType=_ZxAnCfmMaNetCcmDaType_Object((1,3,6,1,4,1,3902,1015,62,1,2,1,1,1),_ZxAnCfmMaNetCcmDaType_Type())
zxAnCfmMaNetCcmDaType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMaNetCcmDaType.setStatus(_A)
class _ZxAnCfmMaProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('maProtectNothing',1),('cfmMaProtectVlan',2),('cfmMaProtectTunnel',3),('cfmMaProtectPort',4),('cfmMaProtectLink',5)))
_ZxAnCfmMaProtect_Type.__name__=_C
_ZxAnCfmMaProtect_Object=MibTableColumn
zxAnCfmMaProtect=_ZxAnCfmMaProtect_Object((1,3,6,1,4,1,3902,1015,62,1,2,1,1,2),_ZxAnCfmMaProtect_Type())
zxAnCfmMaProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMaProtect.setStatus(_A)
class _ZxAnCfmMaTunnel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ZxAnCfmMaTunnel_Type.__name__=_F
_ZxAnCfmMaTunnel_Object=MibTableColumn
zxAnCfmMaTunnel=_ZxAnCfmMaTunnel_Object((1,3,6,1,4,1,3902,1015,62,1,2,1,1,3),_ZxAnCfmMaTunnel_Type())
zxAnCfmMaTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMaTunnel.setStatus(_A)
_ZxAnCfmMep_ObjectIdentity=ObjectIdentity
zxAnCfmMep=_ZxAnCfmMep_ObjectIdentity((1,3,6,1,4,1,3902,1015,62,1,3))
_ZxAnCfmMepTable_Object=MibTable
zxAnCfmMepTable=_ZxAnCfmMepTable_Object((1,3,6,1,4,1,3902,1015,62,1,3,1))
if mibBuilder.loadTexts:zxAnCfmMepTable.setStatus(_A)
_ZxAnCfmMepEntry_Object=MibTableRow
zxAnCfmMepEntry=_ZxAnCfmMepEntry_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1))
if mibBuilder.loadTexts:zxAnCfmMepEntry.setStatus(_A)
_ZxAnCfmMepCcCheckEnable_Type=TruthValue
_ZxAnCfmMepCcCheckEnable_Object=MibTableColumn
zxAnCfmMepCcCheckEnable=_ZxAnCfmMepCcCheckEnable_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,1),_ZxAnCfmMepCcCheckEnable_Type())
zxAnCfmMepCcCheckEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepCcCheckEnable.setStatus(_A)
_ZxAnCfmMepLmEnable_Type=TruthValue
_ZxAnCfmMepLmEnable_Object=MibTableColumn
zxAnCfmMepLmEnable=_ZxAnCfmMepLmEnable_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,2),_ZxAnCfmMepLmEnable_Type())
zxAnCfmMepLmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmEnable.setStatus(_A)
_ZxAnCfmMepDmEnable_Type=TruthValue
_ZxAnCfmMepDmEnable_Object=MibTableColumn
zxAnCfmMepDmEnable=_ZxAnCfmMepDmEnable_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,3),_ZxAnCfmMepDmEnable_Type())
zxAnCfmMepDmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDmEnable.setStatus(_A)
class _ZxAnCfmMepLbmTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_L,2)))
_ZxAnCfmMepLbmTestType_Type.__name__=_C
_ZxAnCfmMepLbmTestType_Object=MibTableColumn
zxAnCfmMepLbmTestType=_ZxAnCfmMepLbmTestType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,4),_ZxAnCfmMepLbmTestType_Type())
zxAnCfmMepLbmTestType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLbmTestType.setStatus(_A)
class _ZxAnCfmMepLbmAppType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('connectivity',1),('outofservicediagnostic',2),('inservicediagnostic',3)))
_ZxAnCfmMepLbmAppType_Type.__name__=_C
_ZxAnCfmMepLbmAppType_Object=MibTableColumn
zxAnCfmMepLbmAppType=_ZxAnCfmMepLbmAppType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,5),_ZxAnCfmMepLbmAppType_Type())
zxAnCfmMepLbmAppType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLbmAppType.setStatus(_A)
_ZxAnCfmMepLmTargetMacAddress_Type=MacAddress
_ZxAnCfmMepLmTargetMacAddress_Object=MibTableColumn
zxAnCfmMepLmTargetMacAddress=_ZxAnCfmMepLmTargetMacAddress_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,6),_ZxAnCfmMepLmTargetMacAddress_Type())
zxAnCfmMepLmTargetMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmTargetMacAddress.setStatus(_A)
_ZxAnCfmMepLmTargetMepId_Type=Dot1agCfmMepIdOrZero
_ZxAnCfmMepLmTargetMepId_Object=MibTableColumn
zxAnCfmMepLmTargetMepId=_ZxAnCfmMepLmTargetMepId_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,7),_ZxAnCfmMepLmTargetMepId_Type())
zxAnCfmMepLmTargetMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmTargetMepId.setStatus(_A)
_ZxAnCfmMepLmTargetIsMepId_Type=TruthValue
_ZxAnCfmMepLmTargetIsMepId_Object=MibTableColumn
zxAnCfmMepLmTargetIsMepId=_ZxAnCfmMepLmTargetIsMepId_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,8),_ZxAnCfmMepLmTargetIsMepId_Type())
zxAnCfmMepLmTargetIsMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmTargetIsMepId.setStatus(_A)
class _ZxAnCfmMepLmmDaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_L,2)))
_ZxAnCfmMepLmmDaType_Type.__name__=_C
_ZxAnCfmMepLmmDaType_Object=MibTableColumn
zxAnCfmMepLmmDaType=_ZxAnCfmMepLmmDaType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,9),_ZxAnCfmMepLmmDaType_Type())
zxAnCfmMepLmmDaType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmmDaType.setStatus(_A)
class _ZxAnCfmMepLmEndType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneended',1),('twoended',2)))
_ZxAnCfmMepLmEndType_Type.__name__=_C
_ZxAnCfmMepLmEndType_Object=MibTableColumn
zxAnCfmMepLmEndType=_ZxAnCfmMepLmEndType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,10),_ZxAnCfmMepLmEndType_Type())
zxAnCfmMepLmEndType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmEndType.setStatus(_A)
class _ZxAnCfmMepLmInterval_Type(Integer32):defaultValue=5
_ZxAnCfmMepLmInterval_Type.__name__=_C
_ZxAnCfmMepLmInterval_Object=MibTableColumn
zxAnCfmMepLmInterval=_ZxAnCfmMepLmInterval_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,11),_ZxAnCfmMepLmInterval_Type())
zxAnCfmMepLmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnCfmMepLmInterval.setUnits(_K)
class _ZxAnCfmMepLmDuration_Type(Integer32):defaultValue=60
_ZxAnCfmMepLmDuration_Type.__name__=_C
_ZxAnCfmMepLmDuration_Object=MibTableColumn
zxAnCfmMepLmDuration=_ZxAnCfmMepLmDuration_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,12),_ZxAnCfmMepLmDuration_Type())
zxAnCfmMepLmDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnCfmMepLmDuration.setUnits(_K)
class _ZxAnCfmMepLmPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnCfmMepLmPriority_Type.__name__=_F
_ZxAnCfmMepLmPriority_Object=MibTableColumn
zxAnCfmMepLmPriority=_ZxAnCfmMepLmPriority_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,13),_ZxAnCfmMepLmPriority_Type())
zxAnCfmMepLmPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmPriority.setStatus(_A)
_ZxAnCfmMepLmFarendLoss_Type=Integer32
_ZxAnCfmMepLmFarendLoss_Object=MibTableColumn
zxAnCfmMepLmFarendLoss=_ZxAnCfmMepLmFarendLoss_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,14),_ZxAnCfmMepLmFarendLoss_Type())
zxAnCfmMepLmFarendLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepLmFarendLoss.setStatus(_A)
_ZxAnCfmMepLmNearendLoss_Type=Integer32
_ZxAnCfmMepLmNearendLoss_Object=MibTableColumn
zxAnCfmMepLmNearendLoss=_ZxAnCfmMepLmNearendLoss_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,15),_ZxAnCfmMepLmNearendLoss_Type())
zxAnCfmMepLmNearendLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepLmNearendLoss.setStatus(_A)
class _ZxAnCfmMepLmLossRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnCfmMepLmLossRatio_Type.__name__=_C
_ZxAnCfmMepLmLossRatio_Object=MibTableColumn
zxAnCfmMepLmLossRatio=_ZxAnCfmMepLmLossRatio_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,16),_ZxAnCfmMepLmLossRatio_Type())
zxAnCfmMepLmLossRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepLmLossRatio.setStatus(_A)
class _ZxAnCfmMepLmStatus_Type(TruthValue):defaultValue=2
_ZxAnCfmMepLmStatus_Type.__name__=_I
_ZxAnCfmMepLmStatus_Object=MibTableColumn
zxAnCfmMepLmStatus=_ZxAnCfmMepLmStatus_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,17),_ZxAnCfmMepLmStatus_Type())
zxAnCfmMepLmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLmStatus.setStatus(_A)
class _ZxAnCfmMepLmResultOk_Type(TruthValue):defaultValue=1
_ZxAnCfmMepLmResultOk_Type.__name__=_I
_ZxAnCfmMepLmResultOk_Object=MibTableColumn
zxAnCfmMepLmResultOk=_ZxAnCfmMepLmResultOk_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,18),_ZxAnCfmMepLmResultOk_Type())
zxAnCfmMepLmResultOk.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepLmResultOk.setStatus(_A)
class _ZxAnCfmMepLmFarendLossRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnCfmMepLmFarendLossRatio_Type.__name__=_C
_ZxAnCfmMepLmFarendLossRatio_Object=MibTableColumn
zxAnCfmMepLmFarendLossRatio=_ZxAnCfmMepLmFarendLossRatio_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,19),_ZxAnCfmMepLmFarendLossRatio_Type())
zxAnCfmMepLmFarendLossRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepLmFarendLossRatio.setStatus(_A)
_ZxAnCfmMepDmTargetMacAddress_Type=MacAddress
_ZxAnCfmMepDmTargetMacAddress_Object=MibTableColumn
zxAnCfmMepDmTargetMacAddress=_ZxAnCfmMepDmTargetMacAddress_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,30),_ZxAnCfmMepDmTargetMacAddress_Type())
zxAnCfmMepDmTargetMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDmTargetMacAddress.setStatus(_A)
_ZxAnCfmMepDmTargetMepId_Type=Dot1agCfmMepIdOrZero
_ZxAnCfmMepDmTargetMepId_Object=MibTableColumn
zxAnCfmMepDmTargetMepId=_ZxAnCfmMepDmTargetMepId_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,31),_ZxAnCfmMepDmTargetMepId_Type())
zxAnCfmMepDmTargetMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDmTargetMepId.setStatus(_A)
_ZxAnCfmMepDmTargetIsMepId_Type=TruthValue
_ZxAnCfmMepDmTargetIsMepId_Object=MibTableColumn
zxAnCfmMepDmTargetIsMepId=_ZxAnCfmMepDmTargetIsMepId_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,32),_ZxAnCfmMepDmTargetIsMepId_Type())
zxAnCfmMepDmTargetIsMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDmTargetIsMepId.setStatus(_A)
class _ZxAnCfmMep1dmDaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_L,2)))
_ZxAnCfmMep1dmDaType_Type.__name__=_C
_ZxAnCfmMep1dmDaType_Object=MibTableColumn
zxAnCfmMep1dmDaType=_ZxAnCfmMep1dmDaType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,33),_ZxAnCfmMep1dmDaType_Type())
zxAnCfmMep1dmDaType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMep1dmDaType.setStatus(_A)
class _ZxAnCfmMepDdmDaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_L,2)))
_ZxAnCfmMepDdmDaType_Type.__name__=_C
_ZxAnCfmMepDdmDaType_Object=MibTableColumn
zxAnCfmMepDdmDaType=_ZxAnCfmMepDdmDaType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,34),_ZxAnCfmMepDdmDaType_Type())
zxAnCfmMepDdmDaType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDdmDaType.setStatus(_A)
class _ZxAnCfmMepDmWayType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneway',1),('twoway',2)))
_ZxAnCfmMepDmWayType_Type.__name__=_C
_ZxAnCfmMepDmWayType_Object=MibTableColumn
zxAnCfmMepDmWayType=_ZxAnCfmMepDmWayType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,35),_ZxAnCfmMepDmWayType_Type())
zxAnCfmMepDmWayType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDmWayType.setStatus(_A)
class _ZxAnCfmMepDmInterval_Type(Integer32):defaultValue=5
_ZxAnCfmMepDmInterval_Type.__name__=_C
_ZxAnCfmMepDmInterval_Object=MibTableColumn
zxAnCfmMepDmInterval=_ZxAnCfmMepDmInterval_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,36),_ZxAnCfmMepDmInterval_Type())
zxAnCfmMepDmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDmInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnCfmMepDmInterval.setUnits(_K)
class _ZxAnCfmMepDmDuration_Type(Integer32):defaultValue=60
_ZxAnCfmMepDmDuration_Type.__name__=_C
_ZxAnCfmMepDmDuration_Object=MibTableColumn
zxAnCfmMepDmDuration=_ZxAnCfmMepDmDuration_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,37),_ZxAnCfmMepDmDuration_Type())
zxAnCfmMepDmDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDmDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnCfmMepDmDuration.setUnits(_K)
class _ZxAnCfmMepDmPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnCfmMepDmPriority_Type.__name__=_F
_ZxAnCfmMepDmPriority_Object=MibTableColumn
zxAnCfmMepDmPriority=_ZxAnCfmMepDmPriority_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,38),_ZxAnCfmMepDmPriority_Type())
zxAnCfmMepDmPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDmPriority.setStatus(_A)
_ZxAnCfmMepDmOneWayAvgDelay_Type=Counter64
_ZxAnCfmMepDmOneWayAvgDelay_Object=MibTableColumn
zxAnCfmMepDmOneWayAvgDelay=_ZxAnCfmMepDmOneWayAvgDelay_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,39),_ZxAnCfmMepDmOneWayAvgDelay_Type())
zxAnCfmMepDmOneWayAvgDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepDmOneWayAvgDelay.setStatus(_A)
_ZxAnCfmMepDmOneWayAvgDv_Type=Counter64
_ZxAnCfmMepDmOneWayAvgDv_Object=MibTableColumn
zxAnCfmMepDmOneWayAvgDv=_ZxAnCfmMepDmOneWayAvgDv_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,40),_ZxAnCfmMepDmOneWayAvgDv_Type())
zxAnCfmMepDmOneWayAvgDv.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepDmOneWayAvgDv.setStatus(_A)
_ZxAnCfmMepDmTwoWayAvgDelay_Type=Counter64
_ZxAnCfmMepDmTwoWayAvgDelay_Object=MibTableColumn
zxAnCfmMepDmTwoWayAvgDelay=_ZxAnCfmMepDmTwoWayAvgDelay_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,41),_ZxAnCfmMepDmTwoWayAvgDelay_Type())
zxAnCfmMepDmTwoWayAvgDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepDmTwoWayAvgDelay.setStatus(_A)
_ZxAnCfmMepDmTwoWayAvgDv_Type=Counter64
_ZxAnCfmMepDmTwoWayAvgDv_Object=MibTableColumn
zxAnCfmMepDmTwoWayAvgDv=_ZxAnCfmMepDmTwoWayAvgDv_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,42),_ZxAnCfmMepDmTwoWayAvgDv_Type())
zxAnCfmMepDmTwoWayAvgDv.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepDmTwoWayAvgDv.setStatus(_A)
class _ZxAnCfmMepDmStatus_Type(TruthValue):defaultValue=2
_ZxAnCfmMepDmStatus_Type.__name__=_I
_ZxAnCfmMepDmStatus_Object=MibTableColumn
zxAnCfmMepDmStatus=_ZxAnCfmMepDmStatus_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,43),_ZxAnCfmMepDmStatus_Type())
zxAnCfmMepDmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepDmStatus.setStatus(_A)
class _ZxAnCfmMepDmResultOk_Type(TruthValue):defaultValue=1
_ZxAnCfmMepDmResultOk_Type.__name__=_I
_ZxAnCfmMepDmResultOk_Object=MibTableColumn
zxAnCfmMepDmResultOk=_ZxAnCfmMepDmResultOk_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,44),_ZxAnCfmMepDmResultOk_Type())
zxAnCfmMepDmResultOk.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepDmResultOk.setStatus(_A)
class _ZxAnCfmMepTestTlvLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_ZxAnCfmMepTestTlvLength_Type.__name__=_F
_ZxAnCfmMepTestTlvLength_Object=MibTableColumn
zxAnCfmMepTestTlvLength=_ZxAnCfmMepTestTlvLength_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,54),_ZxAnCfmMepTestTlvLength_Type())
zxAnCfmMepTestTlvLength.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestTlvLength.setStatus(_A)
class _ZxAnCfmMepTestEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnCfmMepTestEnable_Type.__name__=_C
_ZxAnCfmMepTestEnable_Object=MibTableColumn
zxAnCfmMepTestEnable=_ZxAnCfmMepTestEnable_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,55),_ZxAnCfmMepTestEnable_Type())
zxAnCfmMepTestEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestEnable.setStatus(_A)
class _ZxAnCfmMepTestAppType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inServiceDiagnostic',1),('outOfServiceDiagnostic',2)))
_ZxAnCfmMepTestAppType_Type.__name__=_C
_ZxAnCfmMepTestAppType_Object=MibTableColumn
zxAnCfmMepTestAppType=_ZxAnCfmMepTestAppType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,56),_ZxAnCfmMepTestAppType_Type())
zxAnCfmMepTestAppType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestAppType.setStatus(_A)
_ZxAnCfmMepTestDestMacAddress_Type=MacAddress
_ZxAnCfmMepTestDestMacAddress_Object=MibTableColumn
zxAnCfmMepTestDestMacAddress=_ZxAnCfmMepTestDestMacAddress_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,57),_ZxAnCfmMepTestDestMacAddress_Type())
zxAnCfmMepTestDestMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestDestMacAddress.setStatus(_A)
_ZxAnCfmMepTestDestMepId_Type=Dot1agCfmMepIdOrZero
_ZxAnCfmMepTestDestMepId_Object=MibTableColumn
zxAnCfmMepTestDestMepId=_ZxAnCfmMepTestDestMepId_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,58),_ZxAnCfmMepTestDestMepId_Type())
zxAnCfmMepTestDestMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestDestMepId.setStatus(_A)
_ZxAnCfmMepTestDestIsMepId_Type=TruthValue
_ZxAnCfmMepTestDestIsMepId_Object=MibTableColumn
zxAnCfmMepTestDestIsMepId=_ZxAnCfmMepTestDestIsMepId_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,59),_ZxAnCfmMepTestDestIsMepId_Type())
zxAnCfmMepTestDestIsMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestDestIsMepId.setStatus(_A)
class _ZxAnCfmMepTestInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_ZxAnCfmMepTestInterval_Type.__name__=_C
_ZxAnCfmMepTestInterval_Object=MibTableColumn
zxAnCfmMepTestInterval=_ZxAnCfmMepTestInterval_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,60),_ZxAnCfmMepTestInterval_Type())
zxAnCfmMepTestInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnCfmMepTestInterval.setUnits('milliseconds')
class _ZxAnCfmMepTestDuration_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_ZxAnCfmMepTestDuration_Type.__name__=_C
_ZxAnCfmMepTestDuration_Object=MibTableColumn
zxAnCfmMepTestDuration=_ZxAnCfmMepTestDuration_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,61),_ZxAnCfmMepTestDuration_Type())
zxAnCfmMepTestDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnCfmMepTestDuration.setUnits(_K)
class _ZxAnCfmMepTestPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnCfmMepTestPriority_Type.__name__=_F
_ZxAnCfmMepTestPriority_Object=MibTableColumn
zxAnCfmMepTestPriority=_ZxAnCfmMepTestPriority_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,62),_ZxAnCfmMepTestPriority_Type())
zxAnCfmMepTestPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestPriority.setStatus(_A)
class _ZxAnCfmMepTestDaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_R,2)))
_ZxAnCfmMepTestDaType_Type.__name__=_C
_ZxAnCfmMepTestDaType_Object=MibTableColumn
zxAnCfmMepTestDaType=_ZxAnCfmMepTestDaType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,63),_ZxAnCfmMepTestDaType_Type())
zxAnCfmMepTestDaType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestDaType.setStatus(_A)
class _ZxAnCfmMepTestTlvEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnCfmMepTestTlvEnable_Type.__name__=_C
_ZxAnCfmMepTestTlvEnable_Object=MibTableColumn
zxAnCfmMepTestTlvEnable=_ZxAnCfmMepTestTlvEnable_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,64),_ZxAnCfmMepTestTlvEnable_Type())
zxAnCfmMepTestTlvEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestTlvEnable.setStatus(_A)
class _ZxAnCfmMepTestPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('allZeroesWithoutCrc32',1),('allZeroesWithCrc32',2),('prbsWithoutCrc32',3),('prbsWithCrc32',4)))
_ZxAnCfmMepTestPattern_Type.__name__=_C
_ZxAnCfmMepTestPattern_Object=MibTableColumn
zxAnCfmMepTestPattern=_ZxAnCfmMepTestPattern_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,65),_ZxAnCfmMepTestPattern_Type())
zxAnCfmMepTestPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestPattern.setStatus(_A)
class _ZxAnCfmMepTestStatus_Type(TruthValue):defaultValue=2
_ZxAnCfmMepTestStatus_Type.__name__=_I
_ZxAnCfmMepTestStatus_Object=MibTableColumn
zxAnCfmMepTestStatus=_ZxAnCfmMepTestStatus_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,66),_ZxAnCfmMepTestStatus_Type())
zxAnCfmMepTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepTestStatus.setStatus(_A)
class _ZxAnCfmMepTestResultOk_Type(TruthValue):defaultValue=1
_ZxAnCfmMepTestResultOk_Type.__name__=_I
_ZxAnCfmMepTestResultOk_Object=MibTableColumn
zxAnCfmMepTestResultOk=_ZxAnCfmMepTestResultOk_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,67),_ZxAnCfmMepTestResultOk_Type())
zxAnCfmMepTestResultOk.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepTestResultOk.setStatus(_A)
_ZxAnCfmMepTestMsgSeqNumber_Type=Unsigned32
_ZxAnCfmMepTestMsgSeqNumber_Object=MibTableColumn
zxAnCfmMepTestMsgSeqNumber=_ZxAnCfmMepTestMsgSeqNumber_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,68),_ZxAnCfmMepTestMsgSeqNumber_Type())
zxAnCfmMepTestMsgSeqNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepTestMsgSeqNumber.setStatus(_A)
_ZxAnCfmMepTestNextMsgSeqNumber_Type=Unsigned32
_ZxAnCfmMepTestNextMsgSeqNumber_Object=MibTableColumn
zxAnCfmMepTestNextMsgSeqNumber=_ZxAnCfmMepTestNextMsgSeqNumber_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,69),_ZxAnCfmMepTestNextMsgSeqNumber_Type())
zxAnCfmMepTestNextMsgSeqNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepTestNextMsgSeqNumber.setStatus(_A)
class _ZxAnCfmMepTestTransmitRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ZxAnCfmMepTestTransmitRate_Type.__name__=_F
_ZxAnCfmMepTestTransmitRate_Object=MibTableColumn
zxAnCfmMepTestTransmitRate=_ZxAnCfmMepTestTransmitRate_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,70),_ZxAnCfmMepTestTransmitRate_Type())
zxAnCfmMepTestTransmitRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepTestTransmitRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnCfmMepTestTransmitRate.setUnits('kbps')
class _ZxAnCfmMepTestFarendLossRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnCfmMepTestFarendLossRatio_Type.__name__=_C
_ZxAnCfmMepTestFarendLossRatio_Object=MibTableColumn
zxAnCfmMepTestFarendLossRatio=_ZxAnCfmMepTestFarendLossRatio_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,71),_ZxAnCfmMepTestFarendLossRatio_Type())
zxAnCfmMepTestFarendLossRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepTestFarendLossRatio.setStatus(_A)
class _ZxAnCfmMepTestFarendBitErrRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnCfmMepTestFarendBitErrRatio_Type.__name__=_C
_ZxAnCfmMepTestFarendBitErrRatio_Object=MibTableColumn
zxAnCfmMepTestFarendBitErrRatio=_ZxAnCfmMepTestFarendBitErrRatio_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,72),_ZxAnCfmMepTestFarendBitErrRatio_Type())
zxAnCfmMepTestFarendBitErrRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepTestFarendBitErrRatio.setStatus(_A)
class _ZxAnCfmMepAisEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnCfmMepAisEnable_Type.__name__=_C
_ZxAnCfmMepAisEnable_Object=MibTableColumn
zxAnCfmMepAisEnable=_ZxAnCfmMepAisEnable_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,87),_ZxAnCfmMepAisEnable_Type())
zxAnCfmMepAisEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepAisEnable.setStatus(_A)
class _ZxAnCfmMepLckEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnCfmMepLckEnable_Type.__name__=_C
_ZxAnCfmMepLckEnable_Object=MibTableColumn
zxAnCfmMepLckEnable=_ZxAnCfmMepLckEnable_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,88),_ZxAnCfmMepLckEnable_Type())
zxAnCfmMepLckEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLckEnable.setStatus(_A)
class _ZxAnCfmMepAisClientMegLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnCfmMepAisClientMegLevel_Type.__name__=_C
_ZxAnCfmMepAisClientMegLevel_Object=MibTableColumn
zxAnCfmMepAisClientMegLevel=_ZxAnCfmMepAisClientMegLevel_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,89),_ZxAnCfmMepAisClientMegLevel_Type())
zxAnCfmMepAisClientMegLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepAisClientMegLevel.setStatus(_A)
class _ZxAnCfmMepLckClientMegLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnCfmMepLckClientMegLevel_Type.__name__=_C
_ZxAnCfmMepLckClientMegLevel_Object=MibTableColumn
zxAnCfmMepLckClientMegLevel=_ZxAnCfmMepLckClientMegLevel_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,90),_ZxAnCfmMepLckClientMegLevel_Type())
zxAnCfmMepLckClientMegLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLckClientMegLevel.setStatus(_A)
class _ZxAnCfmMepAisLckInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_ZxAnCfmMepAisLckInterval_Type.__name__=_C
_ZxAnCfmMepAisLckInterval_Object=MibTableColumn
zxAnCfmMepAisLckInterval=_ZxAnCfmMepAisLckInterval_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,91),_ZxAnCfmMepAisLckInterval_Type())
zxAnCfmMepAisLckInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepAisLckInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnCfmMepAisLckInterval.setUnits(_K)
class _ZxAnCfmMepAisPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnCfmMepAisPriority_Type.__name__=_F
_ZxAnCfmMepAisPriority_Object=MibTableColumn
zxAnCfmMepAisPriority=_ZxAnCfmMepAisPriority_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,92),_ZxAnCfmMepAisPriority_Type())
zxAnCfmMepAisPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepAisPriority.setStatus(_A)
class _ZxAnCfmMepLckPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnCfmMepLckPriority_Type.__name__=_F
_ZxAnCfmMepLckPriority_Object=MibTableColumn
zxAnCfmMepLckPriority=_ZxAnCfmMepLckPriority_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,93),_ZxAnCfmMepLckPriority_Type())
zxAnCfmMepLckPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLckPriority.setStatus(_A)
class _ZxAnCfmMepAisDaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_R,2)))
_ZxAnCfmMepAisDaType_Type.__name__=_C
_ZxAnCfmMepAisDaType_Object=MibTableColumn
zxAnCfmMepAisDaType=_ZxAnCfmMepAisDaType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,94),_ZxAnCfmMepAisDaType_Type())
zxAnCfmMepAisDaType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepAisDaType.setStatus(_A)
class _ZxAnCfmMepLckDaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_R,2)))
_ZxAnCfmMepLckDaType_Type.__name__=_C
_ZxAnCfmMepLckDaType_Object=MibTableColumn
zxAnCfmMepLckDaType=_ZxAnCfmMepLckDaType_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,95),_ZxAnCfmMepLckDaType_Type())
zxAnCfmMepLckDaType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLckDaType.setStatus(_A)
_ZxAnCfmMepAisStatus_Type=TruthValue
_ZxAnCfmMepAisStatus_Object=MibTableColumn
zxAnCfmMepAisStatus=_ZxAnCfmMepAisStatus_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,96),_ZxAnCfmMepAisStatus_Type())
zxAnCfmMepAisStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepAisStatus.setStatus(_A)
_ZxAnCfmMepLckStatus_Type=TruthValue
_ZxAnCfmMepLckStatus_Object=MibTableColumn
zxAnCfmMepLckStatus=_ZxAnCfmMepLckStatus_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,97),_ZxAnCfmMepLckStatus_Type())
zxAnCfmMepLckStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepLckStatus.setStatus(_A)
_ZxAnCfmMepLckSendEnable_Type=TruthValue
_ZxAnCfmMepLckSendEnable_Object=MibTableColumn
zxAnCfmMepLckSendEnable=_ZxAnCfmMepLckSendEnable_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,98),_ZxAnCfmMepLckSendEnable_Type())
zxAnCfmMepLckSendEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMepLckSendEnable.setStatus(_A)
_ZxAnCfmMepRdiStatus_Type=TruthValue
_ZxAnCfmMepRdiStatus_Object=MibTableColumn
zxAnCfmMepRdiStatus=_ZxAnCfmMepRdiStatus_Object((1,3,6,1,4,1,3902,1015,62,1,3,1,1,99),_ZxAnCfmMepRdiStatus_Type())
zxAnCfmMepRdiStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmMepRdiStatus.setStatus(_A)
_ZxAnCfmRemoteMepConfTable_Object=MibTable
zxAnCfmRemoteMepConfTable=_ZxAnCfmRemoteMepConfTable_Object((1,3,6,1,4,1,3902,1015,62,1,3,2))
if mibBuilder.loadTexts:zxAnCfmRemoteMepConfTable.setStatus(_A)
_ZxAnCfmRemoteMepConfEntry_Object=MibTableRow
zxAnCfmRemoteMepConfEntry=_ZxAnCfmRemoteMepConfEntry_Object((1,3,6,1,4,1,3902,1015,62,1,3,2,1))
zxAnCfmRemoteMepConfEntry.setIndexNames((0,_H,_P),(0,_H,_O),(0,_H,_Q))
if mibBuilder.loadTexts:zxAnCfmRemoteMepConfEntry.setStatus(_A)
_ZxAnCfmRemoteMepMacAddress_Type=MacAddress
_ZxAnCfmRemoteMepMacAddress_Object=MibTableColumn
zxAnCfmRemoteMepMacAddress=_ZxAnCfmRemoteMepMacAddress_Object((1,3,6,1,4,1,3902,1015,62,1,3,2,1,1),_ZxAnCfmRemoteMepMacAddress_Type())
zxAnCfmRemoteMepMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmRemoteMepMacAddress.setStatus(_A)
_ZxAnCfmRemoteMepConfRowStatus_Type=RowStatus
_ZxAnCfmRemoteMepConfRowStatus_Object=MibTableColumn
zxAnCfmRemoteMepConfRowStatus=_ZxAnCfmRemoteMepConfRowStatus_Object((1,3,6,1,4,1,3902,1015,62,1,3,2,1,20),_ZxAnCfmRemoteMepConfRowStatus_Type())
zxAnCfmRemoteMepConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmRemoteMepConfRowStatus.setStatus(_A)
_ZxAnCfmMipTable_Object=MibTable
zxAnCfmMipTable=_ZxAnCfmMipTable_Object((1,3,6,1,4,1,3902,1015,62,1,3,3))
if mibBuilder.loadTexts:zxAnCfmMipTable.setStatus(_A)
_ZxAnCfmMipEntry_Object=MibTableRow
zxAnCfmMipEntry=_ZxAnCfmMipEntry_Object((1,3,6,1,4,1,3902,1015,62,1,3,3,1))
zxAnCfmMipEntry.setIndexNames((0,_H,_P),(0,_H,_O),(0,_H,_Q))
if mibBuilder.loadTexts:zxAnCfmMipEntry.setStatus(_A)
_ZxAnCfmMipIfIndex_Type=InterfaceIndexOrZero
_ZxAnCfmMipIfIndex_Object=MibTableColumn
zxAnCfmMipIfIndex=_ZxAnCfmMipIfIndex_Object((1,3,6,1,4,1,3902,1015,62,1,3,3,1,1),_ZxAnCfmMipIfIndex_Type())
zxAnCfmMipIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMipIfIndex.setStatus(_A)
_ZxAnCfmMipRowStatus_Type=RowStatus
_ZxAnCfmMipRowStatus_Object=MibTableColumn
zxAnCfmMipRowStatus=_ZxAnCfmMipRowStatus_Object((1,3,6,1,4,1,3902,1015,62,1,3,3,1,20),_ZxAnCfmMipRowStatus_Type())
zxAnCfmMipRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnCfmMipRowStatus.setStatus(_A)
_ZxAnCfmCompatibleObjects_ObjectIdentity=ObjectIdentity
zxAnCfmCompatibleObjects=_ZxAnCfmCompatibleObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,62,1,4))
class _ZxAnCfmCompatible_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ZxAnCfmCompatible_Type.__name__=_S
_ZxAnCfmCompatible_Object=MibScalar
zxAnCfmCompatible=_ZxAnCfmCompatible_Object((1,3,6,1,4,1,3902,1015,62,1,4,1),_ZxAnCfmCompatible_Type())
zxAnCfmCompatible.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnCfmCompatible.setStatus(_A)
_ZxAnCfmInterfaceObjects_ObjectIdentity=ObjectIdentity
zxAnCfmInterfaceObjects=_ZxAnCfmInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,62,1,5))
_ZxAnCfmIfTable_Object=MibTable
zxAnCfmIfTable=_ZxAnCfmIfTable_Object((1,3,6,1,4,1,3902,1015,62,1,5,1))
if mibBuilder.loadTexts:zxAnCfmIfTable.setStatus(_A)
_ZxAnCfmIfEntry_Object=MibTableRow
zxAnCfmIfEntry=_ZxAnCfmIfEntry_Object((1,3,6,1,4,1,3902,1015,62,1,5,1,1))
zxAnCfmIfEntry.setIndexNames((0,_E,_T),(0,_E,_U),(0,_E,_V),(0,_E,_W),(0,_E,_X),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:zxAnCfmIfEntry.setStatus(_A)
_ZxAnCfmRack_Type=Integer32
_ZxAnCfmRack_Object=MibTableColumn
zxAnCfmRack=_ZxAnCfmRack_Object((1,3,6,1,4,1,3902,1015,62,1,5,1,1,1),_ZxAnCfmRack_Type())
zxAnCfmRack.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnCfmRack.setStatus(_A)
_ZxAnCfmShelf_Type=Integer32
_ZxAnCfmShelf_Object=MibTableColumn
zxAnCfmShelf=_ZxAnCfmShelf_Object((1,3,6,1,4,1,3902,1015,62,1,5,1,1,2),_ZxAnCfmShelf_Type())
zxAnCfmShelf.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnCfmShelf.setStatus(_A)
_ZxAnCfmSlot_Type=Integer32
_ZxAnCfmSlot_Object=MibTableColumn
zxAnCfmSlot=_ZxAnCfmSlot_Object((1,3,6,1,4,1,3902,1015,62,1,5,1,1,3),_ZxAnCfmSlot_Type())
zxAnCfmSlot.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnCfmSlot.setStatus(_A)
_ZxAnCfmPort_Type=Integer32
_ZxAnCfmPort_Object=MibTableColumn
zxAnCfmPort=_ZxAnCfmPort_Object((1,3,6,1,4,1,3902,1015,62,1,5,1,1,4),_ZxAnCfmPort_Type())
zxAnCfmPort.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnCfmPort.setStatus(_A)
_ZxAnCfmOnu_Type=Integer32
_ZxAnCfmOnu_Object=MibTableColumn
zxAnCfmOnu=_ZxAnCfmOnu_Object((1,3,6,1,4,1,3902,1015,62,1,5,1,1,5),_ZxAnCfmOnu_Type())
zxAnCfmOnu.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnCfmOnu.setStatus(_A)
class _ZxAnCfmIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*(('physicalPort',1),('onuUni',5)))
_ZxAnCfmIfType_Type.__name__=_C
_ZxAnCfmIfType_Object=MibTableColumn
zxAnCfmIfType=_ZxAnCfmIfType_Object((1,3,6,1,4,1,3902,1015,62,1,5,1,1,6),_ZxAnCfmIfType_Type())
zxAnCfmIfType.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnCfmIfType.setStatus(_A)
_ZxAnCfmLogicalId_Type=ObjectIdentifier
_ZxAnCfmLogicalId_Object=MibTableColumn
zxAnCfmLogicalId=_ZxAnCfmLogicalId_Object((1,3,6,1,4,1,3902,1015,62,1,5,1,1,7),_ZxAnCfmLogicalId_Type())
zxAnCfmLogicalId.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnCfmLogicalId.setStatus(_A)
class _ZxAnCfmIfOamPduFilterEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnCfmIfOamPduFilterEnable_Type.__name__=_C
_ZxAnCfmIfOamPduFilterEnable_Object=MibTableColumn
zxAnCfmIfOamPduFilterEnable=_ZxAnCfmIfOamPduFilterEnable_Object((1,3,6,1,4,1,3902,1015,62,1,5,1,1,8),_ZxAnCfmIfOamPduFilterEnable_Type())
zxAnCfmIfOamPduFilterEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:zxAnCfmIfOamPduFilterEnable.setStatus(_A)
_ZxAnCfmTrapObjects_ObjectIdentity=ObjectIdentity
zxAnCfmTrapObjects=_ZxAnCfmTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,62,2))
dot1agCfmMaNetEntry.registerAugmentions((_E,_a))
zxAnCfmMaNetEntry.setIndexNames(*dot1agCfmMaNetEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions((_E,_b))
zxAnCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'zxAnCfmMib':zxAnCfmMib,'zxAnCfmObjects':zxAnCfmObjects,'zxAnCfmGlobalObjects':zxAnCfmGlobalObjects,'zxAnCfmEnable':zxAnCfmEnable,'zxAnCfmMa':zxAnCfmMa,'zxAnCfmMaNetTable':zxAnCfmMaNetTable,_a:zxAnCfmMaNetEntry,'zxAnCfmMaNetCcmDaType':zxAnCfmMaNetCcmDaType,'zxAnCfmMaProtect':zxAnCfmMaProtect,'zxAnCfmMaTunnel':zxAnCfmMaTunnel,'zxAnCfmMep':zxAnCfmMep,'zxAnCfmMepTable':zxAnCfmMepTable,_b:zxAnCfmMepEntry,'zxAnCfmMepCcCheckEnable':zxAnCfmMepCcCheckEnable,'zxAnCfmMepLmEnable':zxAnCfmMepLmEnable,'zxAnCfmMepDmEnable':zxAnCfmMepDmEnable,'zxAnCfmMepLbmTestType':zxAnCfmMepLbmTestType,'zxAnCfmMepLbmAppType':zxAnCfmMepLbmAppType,'zxAnCfmMepLmTargetMacAddress':zxAnCfmMepLmTargetMacAddress,'zxAnCfmMepLmTargetMepId':zxAnCfmMepLmTargetMepId,'zxAnCfmMepLmTargetIsMepId':zxAnCfmMepLmTargetIsMepId,'zxAnCfmMepLmmDaType':zxAnCfmMepLmmDaType,'zxAnCfmMepLmEndType':zxAnCfmMepLmEndType,'zxAnCfmMepLmInterval':zxAnCfmMepLmInterval,'zxAnCfmMepLmDuration':zxAnCfmMepLmDuration,'zxAnCfmMepLmPriority':zxAnCfmMepLmPriority,'zxAnCfmMepLmFarendLoss':zxAnCfmMepLmFarendLoss,'zxAnCfmMepLmNearendLoss':zxAnCfmMepLmNearendLoss,'zxAnCfmMepLmLossRatio':zxAnCfmMepLmLossRatio,'zxAnCfmMepLmStatus':zxAnCfmMepLmStatus,'zxAnCfmMepLmResultOk':zxAnCfmMepLmResultOk,'zxAnCfmMepLmFarendLossRatio':zxAnCfmMepLmFarendLossRatio,'zxAnCfmMepDmTargetMacAddress':zxAnCfmMepDmTargetMacAddress,'zxAnCfmMepDmTargetMepId':zxAnCfmMepDmTargetMepId,'zxAnCfmMepDmTargetIsMepId':zxAnCfmMepDmTargetIsMepId,'zxAnCfmMep1dmDaType':zxAnCfmMep1dmDaType,'zxAnCfmMepDdmDaType':zxAnCfmMepDdmDaType,'zxAnCfmMepDmWayType':zxAnCfmMepDmWayType,'zxAnCfmMepDmInterval':zxAnCfmMepDmInterval,'zxAnCfmMepDmDuration':zxAnCfmMepDmDuration,'zxAnCfmMepDmPriority':zxAnCfmMepDmPriority,'zxAnCfmMepDmOneWayAvgDelay':zxAnCfmMepDmOneWayAvgDelay,'zxAnCfmMepDmOneWayAvgDv':zxAnCfmMepDmOneWayAvgDv,'zxAnCfmMepDmTwoWayAvgDelay':zxAnCfmMepDmTwoWayAvgDelay,'zxAnCfmMepDmTwoWayAvgDv':zxAnCfmMepDmTwoWayAvgDv,'zxAnCfmMepDmStatus':zxAnCfmMepDmStatus,'zxAnCfmMepDmResultOk':zxAnCfmMepDmResultOk,'zxAnCfmMepTestTlvLength':zxAnCfmMepTestTlvLength,'zxAnCfmMepTestEnable':zxAnCfmMepTestEnable,'zxAnCfmMepTestAppType':zxAnCfmMepTestAppType,'zxAnCfmMepTestDestMacAddress':zxAnCfmMepTestDestMacAddress,'zxAnCfmMepTestDestMepId':zxAnCfmMepTestDestMepId,'zxAnCfmMepTestDestIsMepId':zxAnCfmMepTestDestIsMepId,'zxAnCfmMepTestInterval':zxAnCfmMepTestInterval,'zxAnCfmMepTestDuration':zxAnCfmMepTestDuration,'zxAnCfmMepTestPriority':zxAnCfmMepTestPriority,'zxAnCfmMepTestDaType':zxAnCfmMepTestDaType,'zxAnCfmMepTestTlvEnable':zxAnCfmMepTestTlvEnable,'zxAnCfmMepTestPattern':zxAnCfmMepTestPattern,'zxAnCfmMepTestStatus':zxAnCfmMepTestStatus,'zxAnCfmMepTestResultOk':zxAnCfmMepTestResultOk,'zxAnCfmMepTestMsgSeqNumber':zxAnCfmMepTestMsgSeqNumber,'zxAnCfmMepTestNextMsgSeqNumber':zxAnCfmMepTestNextMsgSeqNumber,'zxAnCfmMepTestTransmitRate':zxAnCfmMepTestTransmitRate,'zxAnCfmMepTestFarendLossRatio':zxAnCfmMepTestFarendLossRatio,'zxAnCfmMepTestFarendBitErrRatio':zxAnCfmMepTestFarendBitErrRatio,'zxAnCfmMepAisEnable':zxAnCfmMepAisEnable,'zxAnCfmMepLckEnable':zxAnCfmMepLckEnable,'zxAnCfmMepAisClientMegLevel':zxAnCfmMepAisClientMegLevel,'zxAnCfmMepLckClientMegLevel':zxAnCfmMepLckClientMegLevel,'zxAnCfmMepAisLckInterval':zxAnCfmMepAisLckInterval,'zxAnCfmMepAisPriority':zxAnCfmMepAisPriority,'zxAnCfmMepLckPriority':zxAnCfmMepLckPriority,'zxAnCfmMepAisDaType':zxAnCfmMepAisDaType,'zxAnCfmMepLckDaType':zxAnCfmMepLckDaType,'zxAnCfmMepAisStatus':zxAnCfmMepAisStatus,'zxAnCfmMepLckStatus':zxAnCfmMepLckStatus,'zxAnCfmMepLckSendEnable':zxAnCfmMepLckSendEnable,'zxAnCfmMepRdiStatus':zxAnCfmMepRdiStatus,'zxAnCfmRemoteMepConfTable':zxAnCfmRemoteMepConfTable,'zxAnCfmRemoteMepConfEntry':zxAnCfmRemoteMepConfEntry,'zxAnCfmRemoteMepMacAddress':zxAnCfmRemoteMepMacAddress,'zxAnCfmRemoteMepConfRowStatus':zxAnCfmRemoteMepConfRowStatus,'zxAnCfmMipTable':zxAnCfmMipTable,'zxAnCfmMipEntry':zxAnCfmMipEntry,'zxAnCfmMipIfIndex':zxAnCfmMipIfIndex,'zxAnCfmMipRowStatus':zxAnCfmMipRowStatus,'zxAnCfmCompatibleObjects':zxAnCfmCompatibleObjects,'zxAnCfmCompatible':zxAnCfmCompatible,'zxAnCfmInterfaceObjects':zxAnCfmInterfaceObjects,'zxAnCfmIfTable':zxAnCfmIfTable,'zxAnCfmIfEntry':zxAnCfmIfEntry,_T:zxAnCfmRack,_U:zxAnCfmShelf,_V:zxAnCfmSlot,_W:zxAnCfmPort,_X:zxAnCfmOnu,_Y:zxAnCfmIfType,_Z:zxAnCfmLogicalId,'zxAnCfmIfOamPduFilterEnable':zxAnCfmIfOamPduFilterEnable,'zxAnCfmTrapObjects':zxAnCfmTrapObjects})