_p='juniAtm1483ProfileGroup6'
_o='juniAtm1483ProfileGroup3'
_n='juniAtm1483ProfileGroup2'
_m='juniAtm1483ProfileGroup'
_l='juniAtm1483ProfileVcClassName'
_k='juniAtm1483ProfileSubscriberEncaps'
_j='juniAtm1483ProfileSubscriberId'
_i='juniAtm1483ProfileNestedProfileEncaps'
_h='juniAtm1483ProfileNestedProfileId'
_g='juniAtm1483ProfileAutoConfEncaps'
_f='juniAtm1483ProfileAutoConfId'
_e='juniAtm1483ProfileId'
_d='Unsigned32'
_c='juniAtm1483ProfileAutoConfLockoutMax'
_b='juniAtm1483ProfileAutoConfLockoutMin'
_a='kilo-bits per second'
_Z='2004-11-02 21:07'
_Y='DisplayString'
_X='Gauge32'
_W='juniAtm1483ProfileVccOamLoopbackFrequency'
_V='juniAtm1483ProfileVccOamAdminStatus'
_U='juniAtm1483ProfileAdvisoryRxSpeed'
_T='juniAtm1483ProfileIfAlias'
_S='juniAtm1483ProfileSubscriberDomain'
_R='juniAtm1483ProfileSubscriberPassword'
_Q='juniAtm1483ProfileSubscriberPasswordPrefix'
_P='juniAtm1483ProfileSubscriberName'
_O='juniAtm1483ProfileSubscriberNamePrefix'
_N='juniAtm1483ProfileNestedProfileUpperIfProfileName'
_M='juniAtm1483ProfileAutoConfEnable'
_L='juniAtm1483ProfileVccMbs'
_K='juniAtm1483ProfileVccScr'
_J='juniAtm1483ProfileVccPcr'
_I='juniAtm1483ProfileVccServiceCategory'
_H='juniAtm1483ProfileVccType'
_G='juniAtm1483ProfileSetMap'
_F='not-accessible'
_E='Integer32'
_D='obsolete'
_C='read-write'
_B='current'
_A='Juniper-ATM-1483-Profile-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniProfileIfEncaps,=mibBuilder.importSymbols('Juniper-PROFILE-MIB','JuniProfileIfEncaps')
JuniEnable,JuniSetMap=mibBuilder.importSymbols('Juniper-TC','JuniEnable','JuniSetMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_X,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_d,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_Y,'PhysAddress','TextualConvention')
juniAtm1483ProfileMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,58))
if mibBuilder.loadTexts:juniAtm1483ProfileMIB.setRevisions(('2005-11-18 14:07',_Z,_Z,_Z))
_JuniAtm1483ProfileObjects_ObjectIdentity=ObjectIdentity
juniAtm1483ProfileObjects=_JuniAtm1483ProfileObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,58,1))
_JuniAtm1483Profile_ObjectIdentity=ObjectIdentity
juniAtm1483Profile=_JuniAtm1483Profile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,58,1,1))
_JuniAtm1483ProfileTable_Object=MibTable
juniAtm1483ProfileTable=_JuniAtm1483ProfileTable_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1))
if mibBuilder.loadTexts:juniAtm1483ProfileTable.setStatus(_B)
_JuniAtm1483ProfileEntry_Object=MibTableRow
juniAtm1483ProfileEntry=_JuniAtm1483ProfileEntry_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1))
juniAtm1483ProfileEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:juniAtm1483ProfileEntry.setStatus(_B)
_JuniAtm1483ProfileId_Type=Unsigned32
_JuniAtm1483ProfileId_Object=MibTableColumn
juniAtm1483ProfileId=_JuniAtm1483ProfileId_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,1),_JuniAtm1483ProfileId_Type())
juniAtm1483ProfileId.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAtm1483ProfileId.setStatus(_B)
_JuniAtm1483ProfileSetMap_Type=JuniSetMap
_JuniAtm1483ProfileSetMap_Object=MibTableColumn
juniAtm1483ProfileSetMap=_JuniAtm1483ProfileSetMap_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,2),_JuniAtm1483ProfileSetMap_Type())
juniAtm1483ProfileSetMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileSetMap.setStatus(_B)
class _JuniAtm1483ProfileVccType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('rfc1483VcMux',0),('rfc1483Llc',1),('autoconfig',2)))
_JuniAtm1483ProfileVccType_Type.__name__=_E
_JuniAtm1483ProfileVccType_Object=MibTableColumn
juniAtm1483ProfileVccType=_JuniAtm1483ProfileVccType_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,3),_JuniAtm1483ProfileVccType_Type())
juniAtm1483ProfileVccType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileVccType.setStatus(_B)
class _JuniAtm1483ProfileVccServiceCategory_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ubr',0),('ubrPcr',1),('nrtVbr',2),('cbr',3),('rtVbr',4)))
_JuniAtm1483ProfileVccServiceCategory_Type.__name__=_E
_JuniAtm1483ProfileVccServiceCategory_Object=MibTableColumn
juniAtm1483ProfileVccServiceCategory=_JuniAtm1483ProfileVccServiceCategory_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,4),_JuniAtm1483ProfileVccServiceCategory_Type())
juniAtm1483ProfileVccServiceCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileVccServiceCategory.setStatus(_B)
class _JuniAtm1483ProfileVccPcr_Type(Gauge32):defaultValue=0
_JuniAtm1483ProfileVccPcr_Type.__name__=_X
_JuniAtm1483ProfileVccPcr_Object=MibTableColumn
juniAtm1483ProfileVccPcr=_JuniAtm1483ProfileVccPcr_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,5),_JuniAtm1483ProfileVccPcr_Type())
juniAtm1483ProfileVccPcr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileVccPcr.setStatus(_B)
if mibBuilder.loadTexts:juniAtm1483ProfileVccPcr.setUnits(_a)
class _JuniAtm1483ProfileVccScr_Type(Gauge32):defaultValue=0
_JuniAtm1483ProfileVccScr_Type.__name__=_X
_JuniAtm1483ProfileVccScr_Object=MibTableColumn
juniAtm1483ProfileVccScr=_JuniAtm1483ProfileVccScr_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,6),_JuniAtm1483ProfileVccScr_Type())
juniAtm1483ProfileVccScr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileVccScr.setStatus(_B)
if mibBuilder.loadTexts:juniAtm1483ProfileVccScr.setUnits(_a)
class _JuniAtm1483ProfileVccMbs_Type(Gauge32):defaultValue=0
_JuniAtm1483ProfileVccMbs_Type.__name__=_X
_JuniAtm1483ProfileVccMbs_Object=MibTableColumn
juniAtm1483ProfileVccMbs=_JuniAtm1483ProfileVccMbs_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,7),_JuniAtm1483ProfileVccMbs_Type())
juniAtm1483ProfileVccMbs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileVccMbs.setStatus(_B)
if mibBuilder.loadTexts:juniAtm1483ProfileVccMbs.setUnits('cells')
class _JuniAtm1483ProfileIfAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JuniAtm1483ProfileIfAlias_Type.__name__=_Y
_JuniAtm1483ProfileIfAlias_Object=MibTableColumn
juniAtm1483ProfileIfAlias=_JuniAtm1483ProfileIfAlias_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,8),_JuniAtm1483ProfileIfAlias_Type())
juniAtm1483ProfileIfAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileIfAlias.setStatus(_B)
class _JuniAtm1483ProfileAdvisoryRxSpeed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniAtm1483ProfileAdvisoryRxSpeed_Type.__name__=_E
_JuniAtm1483ProfileAdvisoryRxSpeed_Object=MibTableColumn
juniAtm1483ProfileAdvisoryRxSpeed=_JuniAtm1483ProfileAdvisoryRxSpeed_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,9),_JuniAtm1483ProfileAdvisoryRxSpeed_Type())
juniAtm1483ProfileAdvisoryRxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileAdvisoryRxSpeed.setStatus(_B)
if mibBuilder.loadTexts:juniAtm1483ProfileAdvisoryRxSpeed.setUnits(_a)
class _JuniAtm1483ProfileVccOamAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oamAdminStateDisabled',1),('oamAdminStateEnabled',2)))
_JuniAtm1483ProfileVccOamAdminStatus_Type.__name__=_E
_JuniAtm1483ProfileVccOamAdminStatus_Object=MibTableColumn
juniAtm1483ProfileVccOamAdminStatus=_JuniAtm1483ProfileVccOamAdminStatus_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,10),_JuniAtm1483ProfileVccOamAdminStatus_Type())
juniAtm1483ProfileVccOamAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileVccOamAdminStatus.setStatus(_B)
class _JuniAtm1483ProfileVccOamLoopbackFrequency_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_JuniAtm1483ProfileVccOamLoopbackFrequency_Type.__name__=_d
_JuniAtm1483ProfileVccOamLoopbackFrequency_Object=MibTableColumn
juniAtm1483ProfileVccOamLoopbackFrequency=_JuniAtm1483ProfileVccOamLoopbackFrequency_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,11),_JuniAtm1483ProfileVccOamLoopbackFrequency_Type())
juniAtm1483ProfileVccOamLoopbackFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileVccOamLoopbackFrequency.setStatus(_B)
if mibBuilder.loadTexts:juniAtm1483ProfileVccOamLoopbackFrequency.setUnits('seconds')
class _JuniAtm1483ProfileVcClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniAtm1483ProfileVcClassName_Type.__name__=_Y
_JuniAtm1483ProfileVcClassName_Object=MibTableColumn
juniAtm1483ProfileVcClassName=_JuniAtm1483ProfileVcClassName_Object((1,3,6,1,4,1,4874,2,2,58,1,1,1,1,12),_JuniAtm1483ProfileVcClassName_Type())
juniAtm1483ProfileVcClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileVcClassName.setStatus(_B)
_JuniAtm1483ProfileAutoConfTable_Object=MibTable
juniAtm1483ProfileAutoConfTable=_JuniAtm1483ProfileAutoConfTable_Object((1,3,6,1,4,1,4874,2,2,58,1,1,2))
if mibBuilder.loadTexts:juniAtm1483ProfileAutoConfTable.setStatus(_B)
_JuniAtm1483ProfileAutoConfEntry_Object=MibTableRow
juniAtm1483ProfileAutoConfEntry=_JuniAtm1483ProfileAutoConfEntry_Object((1,3,6,1,4,1,4874,2,2,58,1,1,2,1))
juniAtm1483ProfileAutoConfEntry.setIndexNames((0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:juniAtm1483ProfileAutoConfEntry.setStatus(_B)
_JuniAtm1483ProfileAutoConfId_Type=Unsigned32
_JuniAtm1483ProfileAutoConfId_Object=MibTableColumn
juniAtm1483ProfileAutoConfId=_JuniAtm1483ProfileAutoConfId_Object((1,3,6,1,4,1,4874,2,2,58,1,1,2,1,1),_JuniAtm1483ProfileAutoConfId_Type())
juniAtm1483ProfileAutoConfId.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAtm1483ProfileAutoConfId.setStatus(_B)
_JuniAtm1483ProfileAutoConfEncaps_Type=JuniProfileIfEncaps
_JuniAtm1483ProfileAutoConfEncaps_Object=MibTableColumn
juniAtm1483ProfileAutoConfEncaps=_JuniAtm1483ProfileAutoConfEncaps_Object((1,3,6,1,4,1,4874,2,2,58,1,1,2,1,2),_JuniAtm1483ProfileAutoConfEncaps_Type())
juniAtm1483ProfileAutoConfEncaps.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAtm1483ProfileAutoConfEncaps.setStatus(_B)
_JuniAtm1483ProfileAutoConfEnable_Type=JuniEnable
_JuniAtm1483ProfileAutoConfEnable_Object=MibTableColumn
juniAtm1483ProfileAutoConfEnable=_JuniAtm1483ProfileAutoConfEnable_Object((1,3,6,1,4,1,4874,2,2,58,1,1,2,1,3),_JuniAtm1483ProfileAutoConfEnable_Type())
juniAtm1483ProfileAutoConfEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileAutoConfEnable.setStatus(_B)
class _JuniAtm1483ProfileAutoConfLockoutMin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniAtm1483ProfileAutoConfLockoutMin_Type.__name__=_E
_JuniAtm1483ProfileAutoConfLockoutMin_Object=MibTableColumn
juniAtm1483ProfileAutoConfLockoutMin=_JuniAtm1483ProfileAutoConfLockoutMin_Object((1,3,6,1,4,1,4874,2,2,58,1,1,2,1,4),_JuniAtm1483ProfileAutoConfLockoutMin_Type())
juniAtm1483ProfileAutoConfLockoutMin.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileAutoConfLockoutMin.setStatus(_B)
class _JuniAtm1483ProfileAutoConfLockoutMax_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniAtm1483ProfileAutoConfLockoutMax_Type.__name__=_E
_JuniAtm1483ProfileAutoConfLockoutMax_Object=MibTableColumn
juniAtm1483ProfileAutoConfLockoutMax=_JuniAtm1483ProfileAutoConfLockoutMax_Object((1,3,6,1,4,1,4874,2,2,58,1,1,2,1,5),_JuniAtm1483ProfileAutoConfLockoutMax_Type())
juniAtm1483ProfileAutoConfLockoutMax.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileAutoConfLockoutMax.setStatus(_B)
_JuniAtm1483ProfileNestedProfileTable_Object=MibTable
juniAtm1483ProfileNestedProfileTable=_JuniAtm1483ProfileNestedProfileTable_Object((1,3,6,1,4,1,4874,2,2,58,1,1,3))
if mibBuilder.loadTexts:juniAtm1483ProfileNestedProfileTable.setStatus(_B)
_JuniAtm1483ProfileNestedProfileEntry_Object=MibTableRow
juniAtm1483ProfileNestedProfileEntry=_JuniAtm1483ProfileNestedProfileEntry_Object((1,3,6,1,4,1,4874,2,2,58,1,1,3,1))
juniAtm1483ProfileNestedProfileEntry.setIndexNames((0,_A,_h),(0,_A,_i))
if mibBuilder.loadTexts:juniAtm1483ProfileNestedProfileEntry.setStatus(_B)
_JuniAtm1483ProfileNestedProfileId_Type=Unsigned32
_JuniAtm1483ProfileNestedProfileId_Object=MibTableColumn
juniAtm1483ProfileNestedProfileId=_JuniAtm1483ProfileNestedProfileId_Object((1,3,6,1,4,1,4874,2,2,58,1,1,3,1,1),_JuniAtm1483ProfileNestedProfileId_Type())
juniAtm1483ProfileNestedProfileId.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAtm1483ProfileNestedProfileId.setStatus(_B)
_JuniAtm1483ProfileNestedProfileEncaps_Type=JuniProfileIfEncaps
_JuniAtm1483ProfileNestedProfileEncaps_Object=MibTableColumn
juniAtm1483ProfileNestedProfileEncaps=_JuniAtm1483ProfileNestedProfileEncaps_Object((1,3,6,1,4,1,4874,2,2,58,1,1,3,1,2),_JuniAtm1483ProfileNestedProfileEncaps_Type())
juniAtm1483ProfileNestedProfileEncaps.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAtm1483ProfileNestedProfileEncaps.setStatus(_B)
_JuniAtm1483ProfileNestedProfileUpperIfProfileName_Type=DisplayString
_JuniAtm1483ProfileNestedProfileUpperIfProfileName_Object=MibTableColumn
juniAtm1483ProfileNestedProfileUpperIfProfileName=_JuniAtm1483ProfileNestedProfileUpperIfProfileName_Object((1,3,6,1,4,1,4874,2,2,58,1,1,3,1,3),_JuniAtm1483ProfileNestedProfileUpperIfProfileName_Type())
juniAtm1483ProfileNestedProfileUpperIfProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileNestedProfileUpperIfProfileName.setStatus(_B)
_JuniAtm1483ProfileSubscriberTable_Object=MibTable
juniAtm1483ProfileSubscriberTable=_JuniAtm1483ProfileSubscriberTable_Object((1,3,6,1,4,1,4874,2,2,58,1,1,4))
if mibBuilder.loadTexts:juniAtm1483ProfileSubscriberTable.setStatus(_B)
_JuniAtm1483ProfileSubscriberEntry_Object=MibTableRow
juniAtm1483ProfileSubscriberEntry=_JuniAtm1483ProfileSubscriberEntry_Object((1,3,6,1,4,1,4874,2,2,58,1,1,4,1))
juniAtm1483ProfileSubscriberEntry.setIndexNames((0,_A,_j),(0,_A,_k))
if mibBuilder.loadTexts:juniAtm1483ProfileSubscriberEntry.setStatus(_B)
_JuniAtm1483ProfileSubscriberId_Type=Unsigned32
_JuniAtm1483ProfileSubscriberId_Object=MibTableColumn
juniAtm1483ProfileSubscriberId=_JuniAtm1483ProfileSubscriberId_Object((1,3,6,1,4,1,4874,2,2,58,1,1,4,1,1),_JuniAtm1483ProfileSubscriberId_Type())
juniAtm1483ProfileSubscriberId.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAtm1483ProfileSubscriberId.setStatus(_B)
_JuniAtm1483ProfileSubscriberEncaps_Type=JuniProfileIfEncaps
_JuniAtm1483ProfileSubscriberEncaps_Object=MibTableColumn
juniAtm1483ProfileSubscriberEncaps=_JuniAtm1483ProfileSubscriberEncaps_Object((1,3,6,1,4,1,4874,2,2,58,1,1,4,1,2),_JuniAtm1483ProfileSubscriberEncaps_Type())
juniAtm1483ProfileSubscriberEncaps.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAtm1483ProfileSubscriberEncaps.setStatus(_B)
_JuniAtm1483ProfileSubscriberNamePrefix_Type=JuniEnable
_JuniAtm1483ProfileSubscriberNamePrefix_Object=MibTableColumn
juniAtm1483ProfileSubscriberNamePrefix=_JuniAtm1483ProfileSubscriberNamePrefix_Object((1,3,6,1,4,1,4874,2,2,58,1,1,4,1,3),_JuniAtm1483ProfileSubscriberNamePrefix_Type())
juniAtm1483ProfileSubscriberNamePrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileSubscriberNamePrefix.setStatus(_B)
_JuniAtm1483ProfileSubscriberName_Type=DisplayString
_JuniAtm1483ProfileSubscriberName_Object=MibTableColumn
juniAtm1483ProfileSubscriberName=_JuniAtm1483ProfileSubscriberName_Object((1,3,6,1,4,1,4874,2,2,58,1,1,4,1,4),_JuniAtm1483ProfileSubscriberName_Type())
juniAtm1483ProfileSubscriberName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileSubscriberName.setStatus(_B)
_JuniAtm1483ProfileSubscriberPasswordPrefix_Type=JuniEnable
_JuniAtm1483ProfileSubscriberPasswordPrefix_Object=MibTableColumn
juniAtm1483ProfileSubscriberPasswordPrefix=_JuniAtm1483ProfileSubscriberPasswordPrefix_Object((1,3,6,1,4,1,4874,2,2,58,1,1,4,1,5),_JuniAtm1483ProfileSubscriberPasswordPrefix_Type())
juniAtm1483ProfileSubscriberPasswordPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileSubscriberPasswordPrefix.setStatus(_B)
_JuniAtm1483ProfileSubscriberPassword_Type=DisplayString
_JuniAtm1483ProfileSubscriberPassword_Object=MibTableColumn
juniAtm1483ProfileSubscriberPassword=_JuniAtm1483ProfileSubscriberPassword_Object((1,3,6,1,4,1,4874,2,2,58,1,1,4,1,6),_JuniAtm1483ProfileSubscriberPassword_Type())
juniAtm1483ProfileSubscriberPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileSubscriberPassword.setStatus(_B)
_JuniAtm1483ProfileSubscriberDomain_Type=DisplayString
_JuniAtm1483ProfileSubscriberDomain_Object=MibTableColumn
juniAtm1483ProfileSubscriberDomain=_JuniAtm1483ProfileSubscriberDomain_Object((1,3,6,1,4,1,4874,2,2,58,1,1,4,1,7),_JuniAtm1483ProfileSubscriberDomain_Type())
juniAtm1483ProfileSubscriberDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAtm1483ProfileSubscriberDomain.setStatus(_B)
_JuniAtm1483ProfileConformance_ObjectIdentity=ObjectIdentity
juniAtm1483ProfileConformance=_JuniAtm1483ProfileConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,58,4))
_JuniAtm1483ProfileCompliances_ObjectIdentity=ObjectIdentity
juniAtm1483ProfileCompliances=_JuniAtm1483ProfileCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,58,4,1))
_JuniAtm1483ProfileGroups_ObjectIdentity=ObjectIdentity
juniAtm1483ProfileGroups=_JuniAtm1483ProfileGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,58,4,2))
juniAtm1483ProfileGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,58,4,2,1))
juniAtm1483ProfileGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniAtm1483ProfileGroup.setStatus(_D)
juniAtm1483ProfileGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,58,4,2,2))
juniAtm1483ProfileGroup2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_T),(_A,_U),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniAtm1483ProfileGroup2.setStatus(_D)
juniAtm1483ProfileGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,58,4,2,3))
juniAtm1483ProfileGroup3.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_V),(_A,_W),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniAtm1483ProfileGroup3.setStatus(_D)
juniAtm1483ProfileGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,58,4,2,4))
juniAtm1483ProfileGroup4.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniAtm1483ProfileGroup4.setStatus(_D)
juniAtm1483ProfileGroup5=ObjectGroup((1,3,6,1,4,1,4874,2,2,58,4,2,5))
juniAtm1483ProfileGroup5.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_M),(_A,_b),(_A,_c),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniAtm1483ProfileGroup5.setStatus(_D)
juniAtm1483ProfileGroup6=ObjectGroup((1,3,6,1,4,1,4874,2,2,58,4,2,6))
juniAtm1483ProfileGroup6.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_l),(_A,_M),(_A,_b),(_A,_c),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniAtm1483ProfileGroup6.setStatus(_B)
juniAtm1483ProfileCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,58,4,1,1))
juniAtm1483ProfileCompliance.setObjects((_A,_m))
if mibBuilder.loadTexts:juniAtm1483ProfileCompliance.setStatus(_D)
juniAtm1483ProfileCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,58,4,1,2))
juniAtm1483ProfileCompliance2.setObjects((_A,_n))
if mibBuilder.loadTexts:juniAtm1483ProfileCompliance2.setStatus(_D)
juniAtm1483ProfileCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,58,4,1,3))
juniAtm1483ProfileCompliance3.setObjects((_A,_o))
if mibBuilder.loadTexts:juniAtm1483ProfileCompliance3.setStatus(_D)
juniAtm1483ProfileCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,58,4,1,4))
juniAtm1483ProfileCompliance4.setObjects((_A,_p))
if mibBuilder.loadTexts:juniAtm1483ProfileCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniAtm1483ProfileMIB':juniAtm1483ProfileMIB,'juniAtm1483ProfileObjects':juniAtm1483ProfileObjects,'juniAtm1483Profile':juniAtm1483Profile,'juniAtm1483ProfileTable':juniAtm1483ProfileTable,'juniAtm1483ProfileEntry':juniAtm1483ProfileEntry,_e:juniAtm1483ProfileId,_G:juniAtm1483ProfileSetMap,_H:juniAtm1483ProfileVccType,_I:juniAtm1483ProfileVccServiceCategory,_J:juniAtm1483ProfileVccPcr,_K:juniAtm1483ProfileVccScr,_L:juniAtm1483ProfileVccMbs,_T:juniAtm1483ProfileIfAlias,_U:juniAtm1483ProfileAdvisoryRxSpeed,_V:juniAtm1483ProfileVccOamAdminStatus,_W:juniAtm1483ProfileVccOamLoopbackFrequency,_l:juniAtm1483ProfileVcClassName,'juniAtm1483ProfileAutoConfTable':juniAtm1483ProfileAutoConfTable,'juniAtm1483ProfileAutoConfEntry':juniAtm1483ProfileAutoConfEntry,_f:juniAtm1483ProfileAutoConfId,_g:juniAtm1483ProfileAutoConfEncaps,_M:juniAtm1483ProfileAutoConfEnable,_b:juniAtm1483ProfileAutoConfLockoutMin,_c:juniAtm1483ProfileAutoConfLockoutMax,'juniAtm1483ProfileNestedProfileTable':juniAtm1483ProfileNestedProfileTable,'juniAtm1483ProfileNestedProfileEntry':juniAtm1483ProfileNestedProfileEntry,_h:juniAtm1483ProfileNestedProfileId,_i:juniAtm1483ProfileNestedProfileEncaps,_N:juniAtm1483ProfileNestedProfileUpperIfProfileName,'juniAtm1483ProfileSubscriberTable':juniAtm1483ProfileSubscriberTable,'juniAtm1483ProfileSubscriberEntry':juniAtm1483ProfileSubscriberEntry,_j:juniAtm1483ProfileSubscriberId,_k:juniAtm1483ProfileSubscriberEncaps,_O:juniAtm1483ProfileSubscriberNamePrefix,_P:juniAtm1483ProfileSubscriberName,_Q:juniAtm1483ProfileSubscriberPasswordPrefix,_R:juniAtm1483ProfileSubscriberPassword,_S:juniAtm1483ProfileSubscriberDomain,'juniAtm1483ProfileConformance':juniAtm1483ProfileConformance,'juniAtm1483ProfileCompliances':juniAtm1483ProfileCompliances,'juniAtm1483ProfileCompliance':juniAtm1483ProfileCompliance,'juniAtm1483ProfileCompliance2':juniAtm1483ProfileCompliance2,'juniAtm1483ProfileCompliance3':juniAtm1483ProfileCompliance3,'juniAtm1483ProfileCompliance4':juniAtm1483ProfileCompliance4,'juniAtm1483ProfileGroups':juniAtm1483ProfileGroups,_m:juniAtm1483ProfileGroup,_n:juniAtm1483ProfileGroup2,_o:juniAtm1483ProfileGroup3,'juniAtm1483ProfileGroup4':juniAtm1483ProfileGroup4,'juniAtm1483ProfileGroup5':juniAtm1483ProfileGroup5,_p:juniAtm1483ProfileGroup6})