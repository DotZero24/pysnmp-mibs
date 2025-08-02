_q='hwlicenseTrapGroup'
_p='hwlicenseMoniGroup'
_o='hwLicenseFileWillExpired'
_n='hwLicenseFeatureGracePeriodExpired'
_m='hwLicenseFeatureExpired'
_l='hwLicenseFileGracePeriodExpired'
_k='hwLicenseFileExpired'
_j='hwLicenseDSLiteSessBelowThreshold'
_i='hwLicenseDSLiteSessOverThreshold'
_h='hwLicenseNAT64SessBelowThreshold'
_g='hwLicenseNAT64SessOverThreshold'
_f='hwLicense6RDSessBelowThreshold'
_e='hwLicense6RDSessOverThreshold'
_d='hwLicenseCurDSLiteSessCount'
_c='hwLicenseTotalDSLiteSessCount'
_b='hwLicenseCurNAT64SessCount'
_a='hwLicenseTotalNAT64SessCount'
_Z='hwLicenseCur6RDSessCount'
_Y='hwLicenseTotal6RDSessCount'
_X='hwLicenseCurIPsecTunnelNumber'
_W='hwLicenseTotalIPsecTunnelNumber'
_V='hwLicenseCurVfwNumber'
_U='hwLicenseTotalVfwNumber'
_T='hwLicenseSysRemainTime'
_S='Integer32'
_R='hwLicenseSysGracePeriodTime'
_Q='hwLicenseSysUpdateServiceName'
_P='hwLicenseSysDSLiteSessThreshold'
_O='hwLicenseSysDSLiteSessPercent'
_N='hwLicenseSysTotalDSLiteSessCount'
_M='hwLicenseSysCurDSLiteSessCount'
_L='hwLicenseSysNAT64SessThreshold'
_K='hwLicenseSysNAT64SessPercent'
_J='hwLicenseSysTotalNAT64SessCount'
_I='hwLicenseSysCurNAT64SessCount'
_H='hwLicenseSys6RDSessThreshold'
_G='hwLicenseSys6RDSessPercent'
_F='hwLicenseSysTotal6RDSessCount'
_E='hwLicenseSysCur6RDSessCount'
_D='read-only'
_C='accessible-for-notify'
_B='current'
_A='HUAWEI-SECURITY-LICENSE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_S,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwLicenseMibObjects=ModuleIdentity((1,3,6,1,4,1,2011,6,122,16))
if mibBuilder.loadTexts:hwLicenseMibObjects.setRevisions(('2016-01-22 09:00','2015-04-15 09:00','2003-03-18 09:00'))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_HuaweiUtility_ObjectIdentity=ObjectIdentity
huaweiUtility=_HuaweiUtility_ObjectIdentity((1,3,6,1,4,1,2011,6))
_HwSecurity_ObjectIdentity=ObjectIdentity
hwSecurity=_HwSecurity_ObjectIdentity((1,3,6,1,4,1,2011,6,122))
_HwLicenseCfgObjects_ObjectIdentity=ObjectIdentity
hwLicenseCfgObjects=_HwLicenseCfgObjects_ObjectIdentity((1,3,6,1,4,1,2011,6,122,16,1))
_HwLicenseMonitorObjects_ObjectIdentity=ObjectIdentity
hwLicenseMonitorObjects=_HwLicenseMonitorObjects_ObjectIdentity((1,3,6,1,4,1,2011,6,122,16,2))
_HwLicenseTotalVfwNumber_Type=Counter64
_HwLicenseTotalVfwNumber_Object=MibScalar
hwLicenseTotalVfwNumber=_HwLicenseTotalVfwNumber_Object((1,3,6,1,4,1,2011,6,122,16,2,1),_HwLicenseTotalVfwNumber_Type())
hwLicenseTotalVfwNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseTotalVfwNumber.setStatus(_B)
_HwLicenseCurVfwNumber_Type=Counter64
_HwLicenseCurVfwNumber_Object=MibScalar
hwLicenseCurVfwNumber=_HwLicenseCurVfwNumber_Object((1,3,6,1,4,1,2011,6,122,16,2,2),_HwLicenseCurVfwNumber_Type())
hwLicenseCurVfwNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseCurVfwNumber.setStatus(_B)
_HwLicenseTotalIPsecTunnelNumber_Type=Counter64
_HwLicenseTotalIPsecTunnelNumber_Object=MibScalar
hwLicenseTotalIPsecTunnelNumber=_HwLicenseTotalIPsecTunnelNumber_Object((1,3,6,1,4,1,2011,6,122,16,2,3),_HwLicenseTotalIPsecTunnelNumber_Type())
hwLicenseTotalIPsecTunnelNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseTotalIPsecTunnelNumber.setStatus(_B)
_HwLicenseCurIPsecTunnelNumber_Type=Counter64
_HwLicenseCurIPsecTunnelNumber_Object=MibScalar
hwLicenseCurIPsecTunnelNumber=_HwLicenseCurIPsecTunnelNumber_Object((1,3,6,1,4,1,2011,6,122,16,2,4),_HwLicenseCurIPsecTunnelNumber_Type())
hwLicenseCurIPsecTunnelNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseCurIPsecTunnelNumber.setStatus(_B)
_HwLicenseTotal6RDSessCount_Type=Counter64
_HwLicenseTotal6RDSessCount_Object=MibScalar
hwLicenseTotal6RDSessCount=_HwLicenseTotal6RDSessCount_Object((1,3,6,1,4,1,2011,6,122,16,2,5),_HwLicenseTotal6RDSessCount_Type())
hwLicenseTotal6RDSessCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseTotal6RDSessCount.setStatus(_B)
_HwLicenseCur6RDSessCount_Type=Counter64
_HwLicenseCur6RDSessCount_Object=MibScalar
hwLicenseCur6RDSessCount=_HwLicenseCur6RDSessCount_Object((1,3,6,1,4,1,2011,6,122,16,2,6),_HwLicenseCur6RDSessCount_Type())
hwLicenseCur6RDSessCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseCur6RDSessCount.setStatus(_B)
_HwLicenseTotalNAT64SessCount_Type=Counter64
_HwLicenseTotalNAT64SessCount_Object=MibScalar
hwLicenseTotalNAT64SessCount=_HwLicenseTotalNAT64SessCount_Object((1,3,6,1,4,1,2011,6,122,16,2,7),_HwLicenseTotalNAT64SessCount_Type())
hwLicenseTotalNAT64SessCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseTotalNAT64SessCount.setStatus(_B)
_HwLicenseCurNAT64SessCount_Type=Counter64
_HwLicenseCurNAT64SessCount_Object=MibScalar
hwLicenseCurNAT64SessCount=_HwLicenseCurNAT64SessCount_Object((1,3,6,1,4,1,2011,6,122,16,2,8),_HwLicenseCurNAT64SessCount_Type())
hwLicenseCurNAT64SessCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseCurNAT64SessCount.setStatus(_B)
_HwLicenseTotalDSLiteSessCount_Type=Counter64
_HwLicenseTotalDSLiteSessCount_Object=MibScalar
hwLicenseTotalDSLiteSessCount=_HwLicenseTotalDSLiteSessCount_Object((1,3,6,1,4,1,2011,6,122,16,2,9),_HwLicenseTotalDSLiteSessCount_Type())
hwLicenseTotalDSLiteSessCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseTotalDSLiteSessCount.setStatus(_B)
_HwLicenseCurDSLiteSessCount_Type=Counter64
_HwLicenseCurDSLiteSessCount_Object=MibScalar
hwLicenseCurDSLiteSessCount=_HwLicenseCurDSLiteSessCount_Object((1,3,6,1,4,1,2011,6,122,16,2,10),_HwLicenseCurDSLiteSessCount_Type())
hwLicenseCurDSLiteSessCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hwLicenseCurDSLiteSessCount.setStatus(_B)
_HwLicenseConformance_ObjectIdentity=ObjectIdentity
hwLicenseConformance=_HwLicenseConformance_ObjectIdentity((1,3,6,1,4,1,2011,6,122,16,3))
_HwLicenseGroups_ObjectIdentity=ObjectIdentity
hwLicenseGroups=_HwLicenseGroups_ObjectIdentity((1,3,6,1,4,1,2011,6,122,16,3,1))
_HwLicenseCompliances_ObjectIdentity=ObjectIdentity
hwLicenseCompliances=_HwLicenseCompliances_ObjectIdentity((1,3,6,1,4,1,2011,6,122,16,3,2))
_HwLicenseSysObjects_ObjectIdentity=ObjectIdentity
hwLicenseSysObjects=_HwLicenseSysObjects_ObjectIdentity((1,3,6,1,4,1,2011,6,122,16,4))
_HwLicenseSysCur6RDSessCount_Type=Gauge32
_HwLicenseSysCur6RDSessCount_Object=MibScalar
hwLicenseSysCur6RDSessCount=_HwLicenseSysCur6RDSessCount_Object((1,3,6,1,4,1,2011,6,122,16,4,1),_HwLicenseSysCur6RDSessCount_Type())
hwLicenseSysCur6RDSessCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysCur6RDSessCount.setStatus(_B)
_HwLicenseSysTotal6RDSessCount_Type=Gauge32
_HwLicenseSysTotal6RDSessCount_Object=MibScalar
hwLicenseSysTotal6RDSessCount=_HwLicenseSysTotal6RDSessCount_Object((1,3,6,1,4,1,2011,6,122,16,4,2),_HwLicenseSysTotal6RDSessCount_Type())
hwLicenseSysTotal6RDSessCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysTotal6RDSessCount.setStatus(_B)
_HwLicenseSys6RDSessPercent_Type=Gauge32
_HwLicenseSys6RDSessPercent_Object=MibScalar
hwLicenseSys6RDSessPercent=_HwLicenseSys6RDSessPercent_Object((1,3,6,1,4,1,2011,6,122,16,4,3),_HwLicenseSys6RDSessPercent_Type())
hwLicenseSys6RDSessPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSys6RDSessPercent.setStatus(_B)
_HwLicenseSys6RDSessThreshold_Type=Gauge32
_HwLicenseSys6RDSessThreshold_Object=MibScalar
hwLicenseSys6RDSessThreshold=_HwLicenseSys6RDSessThreshold_Object((1,3,6,1,4,1,2011,6,122,16,4,4),_HwLicenseSys6RDSessThreshold_Type())
hwLicenseSys6RDSessThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSys6RDSessThreshold.setStatus(_B)
_HwLicenseSysCurNAT64SessCount_Type=Gauge32
_HwLicenseSysCurNAT64SessCount_Object=MibScalar
hwLicenseSysCurNAT64SessCount=_HwLicenseSysCurNAT64SessCount_Object((1,3,6,1,4,1,2011,6,122,16,4,5),_HwLicenseSysCurNAT64SessCount_Type())
hwLicenseSysCurNAT64SessCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysCurNAT64SessCount.setStatus(_B)
_HwLicenseSysTotalNAT64SessCount_Type=Gauge32
_HwLicenseSysTotalNAT64SessCount_Object=MibScalar
hwLicenseSysTotalNAT64SessCount=_HwLicenseSysTotalNAT64SessCount_Object((1,3,6,1,4,1,2011,6,122,16,4,6),_HwLicenseSysTotalNAT64SessCount_Type())
hwLicenseSysTotalNAT64SessCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysTotalNAT64SessCount.setStatus(_B)
_HwLicenseSysNAT64SessPercent_Type=Gauge32
_HwLicenseSysNAT64SessPercent_Object=MibScalar
hwLicenseSysNAT64SessPercent=_HwLicenseSysNAT64SessPercent_Object((1,3,6,1,4,1,2011,6,122,16,4,7),_HwLicenseSysNAT64SessPercent_Type())
hwLicenseSysNAT64SessPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysNAT64SessPercent.setStatus(_B)
_HwLicenseSysNAT64SessThreshold_Type=Gauge32
_HwLicenseSysNAT64SessThreshold_Object=MibScalar
hwLicenseSysNAT64SessThreshold=_HwLicenseSysNAT64SessThreshold_Object((1,3,6,1,4,1,2011,6,122,16,4,8),_HwLicenseSysNAT64SessThreshold_Type())
hwLicenseSysNAT64SessThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysNAT64SessThreshold.setStatus(_B)
_HwLicenseSysCurDSLiteSessCount_Type=Gauge32
_HwLicenseSysCurDSLiteSessCount_Object=MibScalar
hwLicenseSysCurDSLiteSessCount=_HwLicenseSysCurDSLiteSessCount_Object((1,3,6,1,4,1,2011,6,122,16,4,9),_HwLicenseSysCurDSLiteSessCount_Type())
hwLicenseSysCurDSLiteSessCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysCurDSLiteSessCount.setStatus(_B)
_HwLicenseSysTotalDSLiteSessCount_Type=Gauge32
_HwLicenseSysTotalDSLiteSessCount_Object=MibScalar
hwLicenseSysTotalDSLiteSessCount=_HwLicenseSysTotalDSLiteSessCount_Object((1,3,6,1,4,1,2011,6,122,16,4,10),_HwLicenseSysTotalDSLiteSessCount_Type())
hwLicenseSysTotalDSLiteSessCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysTotalDSLiteSessCount.setStatus(_B)
_HwLicenseSysDSLiteSessPercent_Type=Gauge32
_HwLicenseSysDSLiteSessPercent_Object=MibScalar
hwLicenseSysDSLiteSessPercent=_HwLicenseSysDSLiteSessPercent_Object((1,3,6,1,4,1,2011,6,122,16,4,11),_HwLicenseSysDSLiteSessPercent_Type())
hwLicenseSysDSLiteSessPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysDSLiteSessPercent.setStatus(_B)
_HwLicenseSysDSLiteSessThreshold_Type=Gauge32
_HwLicenseSysDSLiteSessThreshold_Object=MibScalar
hwLicenseSysDSLiteSessThreshold=_HwLicenseSysDSLiteSessThreshold_Object((1,3,6,1,4,1,2011,6,122,16,4,12),_HwLicenseSysDSLiteSessThreshold_Type())
hwLicenseSysDSLiteSessThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysDSLiteSessThreshold.setStatus(_B)
_HwLicenseSysUpdateServiceName_Type=OctetString
_HwLicenseSysUpdateServiceName_Object=MibScalar
hwLicenseSysUpdateServiceName=_HwLicenseSysUpdateServiceName_Object((1,3,6,1,4,1,2011,6,122,16,4,13),_HwLicenseSysUpdateServiceName_Type())
hwLicenseSysUpdateServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysUpdateServiceName.setStatus(_B)
class _HwLicenseSysGracePeriodTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_HwLicenseSysGracePeriodTime_Type.__name__=_S
_HwLicenseSysGracePeriodTime_Object=MibScalar
hwLicenseSysGracePeriodTime=_HwLicenseSysGracePeriodTime_Object((1,3,6,1,4,1,2011,6,122,16,4,14),_HwLicenseSysGracePeriodTime_Type())
hwLicenseSysGracePeriodTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysGracePeriodTime.setStatus(_B)
class _HwLicenseSysRemainTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_HwLicenseSysRemainTime_Type.__name__=_S
_HwLicenseSysRemainTime_Object=MibScalar
hwLicenseSysRemainTime=_HwLicenseSysRemainTime_Object((1,3,6,1,4,1,2011,6,122,16,4,15),_HwLicenseSysRemainTime_Type())
hwLicenseSysRemainTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLicenseSysRemainTime.setStatus(_B)
_HwLicenseTraps_ObjectIdentity=ObjectIdentity
hwLicenseTraps=_HwLicenseTraps_ObjectIdentity((1,3,6,1,4,1,2011,6,122,16,5))
hwlicenseMoniGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,16,3,1,1))
hwlicenseMoniGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:hwlicenseMoniGroup.setStatus(_B)
hwlicenseSysObjectGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,16,3,1,2))
hwlicenseSysObjectGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_T)))
if mibBuilder.loadTexts:hwlicenseSysObjectGroup.setStatus(_B)
hwLicense6RDSessOverThreshold=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,1))
hwLicense6RDSessOverThreshold.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:hwLicense6RDSessOverThreshold.setStatus(_B)
hwLicense6RDSessBelowThreshold=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,2))
hwLicense6RDSessBelowThreshold.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:hwLicense6RDSessBelowThreshold.setStatus(_B)
hwLicenseNAT64SessOverThreshold=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,3))
hwLicenseNAT64SessOverThreshold.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hwLicenseNAT64SessOverThreshold.setStatus(_B)
hwLicenseNAT64SessBelowThreshold=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,4))
hwLicenseNAT64SessBelowThreshold.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hwLicenseNAT64SessBelowThreshold.setStatus(_B)
hwLicenseDSLiteSessOverThreshold=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,5))
hwLicenseDSLiteSessOverThreshold.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hwLicenseDSLiteSessOverThreshold.setStatus(_B)
hwLicenseDSLiteSessBelowThreshold=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,6))
hwLicenseDSLiteSessBelowThreshold.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hwLicenseDSLiteSessBelowThreshold.setStatus(_B)
hwLicenseFileExpired=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,7))
hwLicenseFileExpired.setObjects((_A,_R))
if mibBuilder.loadTexts:hwLicenseFileExpired.setStatus(_B)
hwLicenseFileGracePeriodExpired=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,8))
if mibBuilder.loadTexts:hwLicenseFileGracePeriodExpired.setStatus(_B)
hwLicenseFeatureExpired=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,9))
hwLicenseFeatureExpired.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:hwLicenseFeatureExpired.setStatus(_B)
hwLicenseFeatureGracePeriodExpired=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,10))
hwLicenseFeatureGracePeriodExpired.setObjects((_A,_Q))
if mibBuilder.loadTexts:hwLicenseFeatureGracePeriodExpired.setStatus(_B)
hwLicenseFileWillExpired=NotificationType((1,3,6,1,4,1,2011,6,122,16,5,11))
hwLicenseFileWillExpired.setObjects((_A,_T))
if mibBuilder.loadTexts:hwLicenseFileWillExpired.setStatus(_B)
hwlicenseTrapGroup=NotificationGroup((1,3,6,1,4,1,2011,6,122,16,3,1,3))
hwlicenseTrapGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:hwlicenseTrapGroup.setStatus(_B)
licenseModuleCompliance=ModuleCompliance((1,3,6,1,4,1,2011,6,122,16,3,2,1))
licenseModuleCompliance.setObjects(*((_A,_p),(_A,_q)))
if mibBuilder.loadTexts:licenseModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'huawei':huawei,'huaweiUtility':huaweiUtility,'hwSecurity':hwSecurity,'hwLicenseMibObjects':hwLicenseMibObjects,'hwLicenseCfgObjects':hwLicenseCfgObjects,'hwLicenseMonitorObjects':hwLicenseMonitorObjects,_U:hwLicenseTotalVfwNumber,_V:hwLicenseCurVfwNumber,_W:hwLicenseTotalIPsecTunnelNumber,_X:hwLicenseCurIPsecTunnelNumber,_Y:hwLicenseTotal6RDSessCount,_Z:hwLicenseCur6RDSessCount,_a:hwLicenseTotalNAT64SessCount,_b:hwLicenseCurNAT64SessCount,_c:hwLicenseTotalDSLiteSessCount,_d:hwLicenseCurDSLiteSessCount,'hwLicenseConformance':hwLicenseConformance,'hwLicenseGroups':hwLicenseGroups,_p:hwlicenseMoniGroup,'hwlicenseSysObjectGroup':hwlicenseSysObjectGroup,_q:hwlicenseTrapGroup,'hwLicenseCompliances':hwLicenseCompliances,'licenseModuleCompliance':licenseModuleCompliance,'hwLicenseSysObjects':hwLicenseSysObjects,_E:hwLicenseSysCur6RDSessCount,_F:hwLicenseSysTotal6RDSessCount,_G:hwLicenseSys6RDSessPercent,_H:hwLicenseSys6RDSessThreshold,_I:hwLicenseSysCurNAT64SessCount,_J:hwLicenseSysTotalNAT64SessCount,_K:hwLicenseSysNAT64SessPercent,_L:hwLicenseSysNAT64SessThreshold,_M:hwLicenseSysCurDSLiteSessCount,_N:hwLicenseSysTotalDSLiteSessCount,_O:hwLicenseSysDSLiteSessPercent,_P:hwLicenseSysDSLiteSessThreshold,_Q:hwLicenseSysUpdateServiceName,_R:hwLicenseSysGracePeriodTime,_T:hwLicenseSysRemainTime,'hwLicenseTraps':hwLicenseTraps,_e:hwLicense6RDSessOverThreshold,_f:hwLicense6RDSessBelowThreshold,_g:hwLicenseNAT64SessOverThreshold,_h:hwLicenseNAT64SessBelowThreshold,_i:hwLicenseDSLiteSessOverThreshold,_j:hwLicenseDSLiteSessBelowThreshold,_k:hwLicenseFileExpired,_l:hwLicenseFileGracePeriodExpired,_m:hwLicenseFeatureExpired,_n:hwLicenseFeatureGracePeriodExpired,_o:hwLicenseFileWillExpired})