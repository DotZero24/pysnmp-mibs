_y='hm2SfpCurrentRxPowerState'
_x='hm2AutoDisableIntfErrorReason'
_w='hm2IfaceOperAdminStatus'
_v='obsolete'
_u='hm2AutoDisableReasons'
_t='loop-protection'
_s='speed-duplex'
_r='overload-detection'
_q='mac-based-port-security'
_p='bpdu-rate'
_o='arp-rate'
_n='dhcp-snooping'
_m='duplex-mismatch'
_l='crc-error'
_k='link-flap'
_j='hm2ExtNvmTableIndex'
_i='compatibility'
_h='normal'
_g='hm2IfaceLayoutIndex'
_f='energy-efficient-ethernet'
_e='auto-power-down'
_d='auto-mdix'
_c='hm2IfacePhysIndex'
_b='hm2DevMgmtTemperatureExtSensorId'
_a='hm2DevMgmtTemperatureExtType'
_Z='hm2DevMgmtLogicIdx'
_Y='hm2DevMgmtSwFileIdx'
_X='hm2DevMgmtSwFileType'
_W='hm2DevMgmtSwFileLocation'
_V='hm2DevMgmtSwVersCertIndex'
_U='TruthValue'
_T='percent'
_S='Hm2DeviceExtNVMType'
_R='accessible-for-notify'
_Q='none'
_P='SnmpAdminString'
_O='hm2ModuleIndex'
_N='unsupported'
_M='Bits'
_L='hm2UnitIndex'
_K='Unsigned32'
_J='ifIndex'
_I='IF-MIB'
_H='not-accessible'
_G='HmEnabledStatus'
_F='other'
_E='HM2-DEVMGMT-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,HmTimeSeconds1970,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_G,'HmTimeSeconds1970','hm2ConfigurationMibs')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndexOrZero',_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_P)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_M,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_U)
hm2DeviceMgmtMib=ModuleIdentity((1,3,6,1,4,1,248,11,10))
if mibBuilder.loadTexts:hm2DeviceMgmtMib.setRevisions(('2012-10-10 00:00','2011-03-16 00:00'))
class Hm2DeviceExtNVMType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),('sd',1),('usb',2),('serial',3)))
_Hm2DeviceMgmtMibNotifications_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtMibNotifications=_Hm2DeviceMgmtMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,10,0))
_Hm2DeviceMgmtMibObjects_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtMibObjects=_Hm2DeviceMgmtMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,10,1))
_Hm2DeviceMgmtGroup_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtGroup=_Hm2DeviceMgmtGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,1))
_Hm2DevMgmtProductId_Type=ObjectIdentifier
_Hm2DevMgmtProductId_Object=MibScalar
hm2DevMgmtProductId=_Hm2DevMgmtProductId_Object((1,3,6,1,4,1,248,11,10,1,1,1),_Hm2DevMgmtProductId_Type())
hm2DevMgmtProductId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtProductId.setStatus(_A)
_Hm2DevMgmtProductDescr_Type=DisplayString
_Hm2DevMgmtProductDescr_Object=MibScalar
hm2DevMgmtProductDescr=_Hm2DevMgmtProductDescr_Object((1,3,6,1,4,1,248,11,10,1,1,2),_Hm2DevMgmtProductDescr_Type())
hm2DevMgmtProductDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtProductDescr.setStatus(_A)
_Hm2DevMgmtSerialNumber_Type=DisplayString
_Hm2DevMgmtSerialNumber_Object=MibScalar
hm2DevMgmtSerialNumber=_Hm2DevMgmtSerialNumber_Object((1,3,6,1,4,1,248,11,10,1,1,3),_Hm2DevMgmtSerialNumber_Type())
hm2DevMgmtSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSerialNumber.setStatus(_A)
_Hm2DeviceMgmtActionGroup_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtActionGroup=_Hm2DeviceMgmtActionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,2))
class _Hm2DevMgmtActionReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('reset',2)))
_Hm2DevMgmtActionReset_Type.__name__=_C
_Hm2DevMgmtActionReset_Object=MibScalar
hm2DevMgmtActionReset=_Hm2DevMgmtActionReset_Object((1,3,6,1,4,1,248,11,10,1,2,1),_Hm2DevMgmtActionReset_Type())
hm2DevMgmtActionReset.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionReset.setStatus(_A)
class _Hm2DevMgmtActionFlushFDB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushFDB',2)))
_Hm2DevMgmtActionFlushFDB_Type.__name__=_C
_Hm2DevMgmtActionFlushFDB_Object=MibScalar
hm2DevMgmtActionFlushFDB=_Hm2DevMgmtActionFlushFDB_Object((1,3,6,1,4,1,248,11,10,1,2,2),_Hm2DevMgmtActionFlushFDB_Type())
hm2DevMgmtActionFlushFDB.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushFDB.setStatus(_A)
class _Hm2DevMgmtActionFlushARP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushARP',2)))
_Hm2DevMgmtActionFlushARP_Type.__name__=_C
_Hm2DevMgmtActionFlushARP_Object=MibScalar
hm2DevMgmtActionFlushARP=_Hm2DevMgmtActionFlushARP_Object((1,3,6,1,4,1,248,11,10,1,2,3),_Hm2DevMgmtActionFlushARP_Type())
hm2DevMgmtActionFlushARP.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushARP.setStatus(_A)
class _Hm2DevMgmtActionFlushIGS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushIGS',2)))
_Hm2DevMgmtActionFlushIGS_Type.__name__=_C
_Hm2DevMgmtActionFlushIGS_Object=MibScalar
hm2DevMgmtActionFlushIGS=_Hm2DevMgmtActionFlushIGS_Object((1,3,6,1,4,1,248,11,10,1,2,4),_Hm2DevMgmtActionFlushIGS_Type())
hm2DevMgmtActionFlushIGS.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushIGS.setStatus(_A)
class _Hm2DevMgmtActionFlushPortStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushPortStats',2)))
_Hm2DevMgmtActionFlushPortStats_Type.__name__=_C
_Hm2DevMgmtActionFlushPortStats_Object=MibScalar
hm2DevMgmtActionFlushPortStats=_Hm2DevMgmtActionFlushPortStats_Object((1,3,6,1,4,1,248,11,10,1,2,5),_Hm2DevMgmtActionFlushPortStats_Type())
hm2DevMgmtActionFlushPortStats.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushPortStats.setStatus(_A)
class _Hm2DevMgmtActionFlushEmailLogStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushEmailLogCounters',2)))
_Hm2DevMgmtActionFlushEmailLogStats_Type.__name__=_C
_Hm2DevMgmtActionFlushEmailLogStats_Object=MibScalar
hm2DevMgmtActionFlushEmailLogStats=_Hm2DevMgmtActionFlushEmailLogStats_Object((1,3,6,1,4,1,248,11,10,1,2,6),_Hm2DevMgmtActionFlushEmailLogStats_Type())
hm2DevMgmtActionFlushEmailLogStats.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushEmailLogStats.setStatus(_A)
class _Hm2DevMgmtActionFlushMMRP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushMMRP',2)))
_Hm2DevMgmtActionFlushMMRP_Type.__name__=_C
_Hm2DevMgmtActionFlushMMRP_Object=MibScalar
hm2DevMgmtActionFlushMMRP=_Hm2DevMgmtActionFlushMMRP_Object((1,3,6,1,4,1,248,11,10,1,2,7),_Hm2DevMgmtActionFlushMMRP_Type())
hm2DevMgmtActionFlushMMRP.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushMMRP.setStatus(_A)
class _Hm2DevMgmtActionFlushMVRP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushMVRP',2)))
_Hm2DevMgmtActionFlushMVRP_Type.__name__=_C
_Hm2DevMgmtActionFlushMVRP_Object=MibScalar
hm2DevMgmtActionFlushMVRP=_Hm2DevMgmtActionFlushMVRP_Object((1,3,6,1,4,1,248,11,10,1,2,8),_Hm2DevMgmtActionFlushMVRP_Type())
hm2DevMgmtActionFlushMVRP.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushMVRP.setStatus(_A)
class _Hm2DevMgmtActionFlushMSRP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushMSRP',2)))
_Hm2DevMgmtActionFlushMSRP_Type.__name__=_C
_Hm2DevMgmtActionFlushMSRP_Object=MibScalar
hm2DevMgmtActionFlushMSRP=_Hm2DevMgmtActionFlushMSRP_Object((1,3,6,1,4,1,248,11,10,1,2,9),_Hm2DevMgmtActionFlushMSRP_Type())
hm2DevMgmtActionFlushMSRP.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushMSRP.setStatus(_A)
class _Hm2DevMgmtActionFlushIeee8021AS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushIeee8021AS',2)))
_Hm2DevMgmtActionFlushIeee8021AS_Type.__name__=_C
_Hm2DevMgmtActionFlushIeee8021AS_Object=MibScalar
hm2DevMgmtActionFlushIeee8021AS=_Hm2DevMgmtActionFlushIeee8021AS_Object((1,3,6,1,4,1,248,11,10,1,2,10),_Hm2DevMgmtActionFlushIeee8021AS_Type())
hm2DevMgmtActionFlushIeee8021AS.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushIeee8021AS.setStatus(_A)
class _Hm2DevMgmtActionFlushDnsClientCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushDnsClientCache',2)))
_Hm2DevMgmtActionFlushDnsClientCache_Type.__name__=_C
_Hm2DevMgmtActionFlushDnsClientCache_Object=MibScalar
hm2DevMgmtActionFlushDnsClientCache=_Hm2DevMgmtActionFlushDnsClientCache_Object((1,3,6,1,4,1,248,11,10,1,2,11),_Hm2DevMgmtActionFlushDnsClientCache_Type())
hm2DevMgmtActionFlushDnsClientCache.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushDnsClientCache.setStatus(_A)
class _Hm2DevMgmtActionFlushDnsCachingServerCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushDnsCachingServerCache',2)))
_Hm2DevMgmtActionFlushDnsCachingServerCache_Type.__name__=_C
_Hm2DevMgmtActionFlushDnsCachingServerCache_Object=MibScalar
hm2DevMgmtActionFlushDnsCachingServerCache=_Hm2DevMgmtActionFlushDnsCachingServerCache_Object((1,3,6,1,4,1,248,11,10,1,2,12),_Hm2DevMgmtActionFlushDnsCachingServerCache_Type())
hm2DevMgmtActionFlushDnsCachingServerCache.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushDnsCachingServerCache.setStatus(_A)
class _Hm2DevMgmtActionFlushIpUdpHelperStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushIpUdpHelperStats',2)))
_Hm2DevMgmtActionFlushIpUdpHelperStats_Type.__name__=_C
_Hm2DevMgmtActionFlushIpUdpHelperStats_Object=MibScalar
hm2DevMgmtActionFlushIpUdpHelperStats=_Hm2DevMgmtActionFlushIpUdpHelperStats_Object((1,3,6,1,4,1,248,11,10,1,2,13),_Hm2DevMgmtActionFlushIpUdpHelperStats_Type())
hm2DevMgmtActionFlushIpUdpHelperStats.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushIpUdpHelperStats.setStatus(_A)
class _Hm2DevMgmtActionFlushAclStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('flushAclStats',2),('flushAclMacStats',3)))
_Hm2DevMgmtActionFlushAclStats_Type.__name__=_C
_Hm2DevMgmtActionFlushAclStats_Object=MibScalar
hm2DevMgmtActionFlushAclStats=_Hm2DevMgmtActionFlushAclStats_Object((1,3,6,1,4,1,248,11,10,1,2,14),_Hm2DevMgmtActionFlushAclStats_Type())
hm2DevMgmtActionFlushAclStats.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushAclStats.setStatus(_A)
class _Hm2DevMgmtActionFlushLdapUserCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushLdapUserCache',2)))
_Hm2DevMgmtActionFlushLdapUserCache_Type.__name__=_C
_Hm2DevMgmtActionFlushLdapUserCache_Object=MibScalar
hm2DevMgmtActionFlushLdapUserCache=_Hm2DevMgmtActionFlushLdapUserCache_Object((1,3,6,1,4,1,248,11,10,1,2,15),_Hm2DevMgmtActionFlushLdapUserCache_Type())
hm2DevMgmtActionFlushLdapUserCache.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushLdapUserCache.setStatus(_A)
class _Hm2DevMgmtActionFlushMgmtAccessStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushMgmtAccessStatistics',2)))
_Hm2DevMgmtActionFlushMgmtAccessStatistics_Type.__name__=_C
_Hm2DevMgmtActionFlushMgmtAccessStatistics_Object=MibScalar
hm2DevMgmtActionFlushMgmtAccessStatistics=_Hm2DevMgmtActionFlushMgmtAccessStatistics_Object((1,3,6,1,4,1,248,11,10,1,2,16),_Hm2DevMgmtActionFlushMgmtAccessStatistics_Type())
hm2DevMgmtActionFlushMgmtAccessStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushMgmtAccessStatistics.setStatus(_A)
class _Hm2DevMgmtActionFlushDiffServ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('flushDiffServ',2)))
_Hm2DevMgmtActionFlushDiffServ_Type.__name__=_C
_Hm2DevMgmtActionFlushDiffServ_Object=MibScalar
hm2DevMgmtActionFlushDiffServ=_Hm2DevMgmtActionFlushDiffServ_Object((1,3,6,1,4,1,248,11,10,1,2,17),_Hm2DevMgmtActionFlushDiffServ_Type())
hm2DevMgmtActionFlushDiffServ.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionFlushDiffServ.setStatus(_A)
class _Hm2DevMgmtActionDelayPreset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483))
_Hm2DevMgmtActionDelayPreset_Type.__name__=_C
_Hm2DevMgmtActionDelayPreset_Object=MibScalar
hm2DevMgmtActionDelayPreset=_Hm2DevMgmtActionDelayPreset_Object((1,3,6,1,4,1,248,11,10,1,2,100),_Hm2DevMgmtActionDelayPreset_Type())
hm2DevMgmtActionDelayPreset.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionDelayPreset.setStatus(_A)
class _Hm2DevMgmtActionDelayCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483))
_Hm2DevMgmtActionDelayCurrent_Type.__name__=_C
_Hm2DevMgmtActionDelayCurrent_Object=MibScalar
hm2DevMgmtActionDelayCurrent=_Hm2DevMgmtActionDelayCurrent_Object((1,3,6,1,4,1,248,11,10,1,2,101),_Hm2DevMgmtActionDelayCurrent_Type())
hm2DevMgmtActionDelayCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtActionDelayCurrent.setStatus(_A)
class _Hm2DevMgmtActionLanBypass_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMgmtActionLanBypass_Type.__name__=_G
_Hm2DevMgmtActionLanBypass_Object=MibScalar
hm2DevMgmtActionLanBypass=_Hm2DevMgmtActionLanBypass_Object((1,3,6,1,4,1,248,11,10,1,2,102),_Hm2DevMgmtActionLanBypass_Type())
hm2DevMgmtActionLanBypass.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionLanBypass.setStatus(_A)
class _Hm2DevMgmtActionSystemoffLanBypass_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMgmtActionSystemoffLanBypass_Type.__name__=_G
_Hm2DevMgmtActionSystemoffLanBypass_Object=MibScalar
hm2DevMgmtActionSystemoffLanBypass=_Hm2DevMgmtActionSystemoffLanBypass_Object((1,3,6,1,4,1,248,11,10,1,2,103),_Hm2DevMgmtActionSystemoffLanBypass_Type())
hm2DevMgmtActionSystemoffLanBypass.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtActionSystemoffLanBypass.setStatus(_A)
_Hm2DeviceMgmtSoftwareGroup_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtSoftwareGroup=_Hm2DeviceMgmtSoftwareGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,3))
_Hm2DeviceMgmtSoftwareVersionGroup_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtSoftwareVersionGroup=_Hm2DeviceMgmtSoftwareVersionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,3,1))
_Hm2DevMgmtSwVersBootcode_Type=DisplayString
_Hm2DevMgmtSwVersBootcode_Object=MibScalar
hm2DevMgmtSwVersBootcode=_Hm2DevMgmtSwVersBootcode_Object((1,3,6,1,4,1,248,11,10,1,3,1,1),_Hm2DevMgmtSwVersBootcode_Type())
hm2DevMgmtSwVersBootcode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwVersBootcode.setStatus(_A)
class _Hm2DevMgmtSwVersAllowUnsigned_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMgmtSwVersAllowUnsigned_Type.__name__=_G
_Hm2DevMgmtSwVersAllowUnsigned_Object=MibScalar
hm2DevMgmtSwVersAllowUnsigned=_Hm2DevMgmtSwVersAllowUnsigned_Object((1,3,6,1,4,1,248,11,10,1,3,1,2),_Hm2DevMgmtSwVersAllowUnsigned_Type())
hm2DevMgmtSwVersAllowUnsigned.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtSwVersAllowUnsigned.setStatus(_A)
_Hm2DevMgmtSwVersCertTable_Object=MibTable
hm2DevMgmtSwVersCertTable=_Hm2DevMgmtSwVersCertTable_Object((1,3,6,1,4,1,248,11,10,1,3,1,7))
if mibBuilder.loadTexts:hm2DevMgmtSwVersCertTable.setStatus(_A)
_Hm2DevMgmtSwVersCertEntry_Object=MibTableRow
hm2DevMgmtSwVersCertEntry=_Hm2DevMgmtSwVersCertEntry_Object((1,3,6,1,4,1,248,11,10,1,3,1,7,1))
hm2DevMgmtSwVersCertEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:hm2DevMgmtSwVersCertEntry.setStatus(_A)
_Hm2DevMgmtSwVersCertIndex_Type=Integer32
_Hm2DevMgmtSwVersCertIndex_Object=MibTableColumn
hm2DevMgmtSwVersCertIndex=_Hm2DevMgmtSwVersCertIndex_Object((1,3,6,1,4,1,248,11,10,1,3,1,7,1,1),_Hm2DevMgmtSwVersCertIndex_Type())
hm2DevMgmtSwVersCertIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DevMgmtSwVersCertIndex.setStatus(_A)
_Hm2DevMgmtSwVersCertSerialNo_Type=OctetString
_Hm2DevMgmtSwVersCertSerialNo_Object=MibTableColumn
hm2DevMgmtSwVersCertSerialNo=_Hm2DevMgmtSwVersCertSerialNo_Object((1,3,6,1,4,1,248,11,10,1,3,1,7,1,2),_Hm2DevMgmtSwVersCertSerialNo_Type())
hm2DevMgmtSwVersCertSerialNo.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwVersCertSerialNo.setStatus(_A)
_Hm2DevMgmtSwVersCertSubject_Type=DisplayString
_Hm2DevMgmtSwVersCertSubject_Object=MibTableColumn
hm2DevMgmtSwVersCertSubject=_Hm2DevMgmtSwVersCertSubject_Object((1,3,6,1,4,1,248,11,10,1,3,1,7,1,3),_Hm2DevMgmtSwVersCertSubject_Type())
hm2DevMgmtSwVersCertSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwVersCertSubject.setStatus(_A)
_Hm2DevMgmtSwVersCertSigAlg_Type=DisplayString
_Hm2DevMgmtSwVersCertSigAlg_Object=MibTableColumn
hm2DevMgmtSwVersCertSigAlg=_Hm2DevMgmtSwVersCertSigAlg_Object((1,3,6,1,4,1,248,11,10,1,3,1,7,1,4),_Hm2DevMgmtSwVersCertSigAlg_Type())
hm2DevMgmtSwVersCertSigAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwVersCertSigAlg.setStatus(_A)
class _Hm2DevMgmtSwVersCertType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('production',1),('development',2)))
_Hm2DevMgmtSwVersCertType_Type.__name__=_C
_Hm2DevMgmtSwVersCertType_Object=MibTableColumn
hm2DevMgmtSwVersCertType=_Hm2DevMgmtSwVersCertType_Object((1,3,6,1,4,1,248,11,10,1,3,1,7,1,5),_Hm2DevMgmtSwVersCertType_Type())
hm2DevMgmtSwVersCertType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwVersCertType.setStatus(_A)
class _Hm2DevMgmtSwVersCertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('revoked',1),('valid',2)))
_Hm2DevMgmtSwVersCertStatus_Type.__name__=_C
_Hm2DevMgmtSwVersCertStatus_Object=MibTableColumn
hm2DevMgmtSwVersCertStatus=_Hm2DevMgmtSwVersCertStatus_Object((1,3,6,1,4,1,248,11,10,1,3,1,7,1,6),_Hm2DevMgmtSwVersCertStatus_Type())
hm2DevMgmtSwVersCertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwVersCertStatus.setStatus(_A)
_Hm2DevMgmtSwVersCertFingerprint_Type=OctetString
_Hm2DevMgmtSwVersCertFingerprint_Object=MibTableColumn
hm2DevMgmtSwVersCertFingerprint=_Hm2DevMgmtSwVersCertFingerprint_Object((1,3,6,1,4,1,248,11,10,1,3,1,7,1,7),_Hm2DevMgmtSwVersCertFingerprint_Type())
hm2DevMgmtSwVersCertFingerprint.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwVersCertFingerprint.setStatus(_A)
_Hm2DevMgmtSwVersTable_Object=MibTable
hm2DevMgmtSwVersTable=_Hm2DevMgmtSwVersTable_Object((1,3,6,1,4,1,248,11,10,1,3,1,10))
if mibBuilder.loadTexts:hm2DevMgmtSwVersTable.setStatus(_A)
_Hm2DevMgmtSwVersEntry_Object=MibTableRow
hm2DevMgmtSwVersEntry=_Hm2DevMgmtSwVersEntry_Object((1,3,6,1,4,1,248,11,10,1,3,1,10,1))
hm2DevMgmtSwVersEntry.setIndexNames((0,_E,_W),(0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:hm2DevMgmtSwVersEntry.setStatus(_A)
class _Hm2DevMgmtSwFileLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ram',1),('flash',2),('sd-card',3),('usb',4)))
_Hm2DevMgmtSwFileLocation_Type.__name__=_C
_Hm2DevMgmtSwFileLocation_Object=MibTableColumn
hm2DevMgmtSwFileLocation=_Hm2DevMgmtSwFileLocation_Object((1,3,6,1,4,1,248,11,10,1,3,1,10,1,1),_Hm2DevMgmtSwFileLocation_Type())
hm2DevMgmtSwFileLocation.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DevMgmtSwFileLocation.setStatus(_A)
class _Hm2DevMgmtSwFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('firmware',1),('applet',2),('logic',3)))
_Hm2DevMgmtSwFileType_Type.__name__=_C
_Hm2DevMgmtSwFileType_Object=MibTableColumn
hm2DevMgmtSwFileType=_Hm2DevMgmtSwFileType_Object((1,3,6,1,4,1,248,11,10,1,3,1,10,1,2),_Hm2DevMgmtSwFileType_Type())
hm2DevMgmtSwFileType.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DevMgmtSwFileType.setStatus(_A)
class _Hm2DevMgmtSwFileIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_Hm2DevMgmtSwFileIdx_Type.__name__=_C
_Hm2DevMgmtSwFileIdx_Object=MibTableColumn
hm2DevMgmtSwFileIdx=_Hm2DevMgmtSwFileIdx_Object((1,3,6,1,4,1,248,11,10,1,3,1,10,1,3),_Hm2DevMgmtSwFileIdx_Type())
hm2DevMgmtSwFileIdx.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DevMgmtSwFileIdx.setStatus(_A)
_Hm2DevMgmtSwFileName_Type=DisplayString
_Hm2DevMgmtSwFileName_Object=MibTableColumn
hm2DevMgmtSwFileName=_Hm2DevMgmtSwFileName_Object((1,3,6,1,4,1,248,11,10,1,3,1,10,1,4),_Hm2DevMgmtSwFileName_Type())
hm2DevMgmtSwFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwFileName.setStatus(_A)
_Hm2DevMgmtSwVersion_Type=DisplayString
_Hm2DevMgmtSwVersion_Object=MibTableColumn
hm2DevMgmtSwVersion=_Hm2DevMgmtSwVersion_Object((1,3,6,1,4,1,248,11,10,1,3,1,10,1,5),_Hm2DevMgmtSwVersion_Type())
hm2DevMgmtSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwVersion.setStatus(_A)
_Hm2DevMgmtSwMajorRelNum_Type=Integer32
_Hm2DevMgmtSwMajorRelNum_Object=MibTableColumn
hm2DevMgmtSwMajorRelNum=_Hm2DevMgmtSwMajorRelNum_Object((1,3,6,1,4,1,248,11,10,1,3,1,10,1,6),_Hm2DevMgmtSwMajorRelNum_Type())
hm2DevMgmtSwMajorRelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwMajorRelNum.setStatus(_A)
_Hm2DevMgmtSwMinorRelNum_Type=Integer32
_Hm2DevMgmtSwMinorRelNum_Object=MibTableColumn
hm2DevMgmtSwMinorRelNum=_Hm2DevMgmtSwMinorRelNum_Object((1,3,6,1,4,1,248,11,10,1,3,1,10,1,7),_Hm2DevMgmtSwMinorRelNum_Type())
hm2DevMgmtSwMinorRelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwMinorRelNum.setStatus(_A)
_Hm2DevMgmtSwBugfixRelNum_Type=Integer32
_Hm2DevMgmtSwBugfixRelNum_Object=MibTableColumn
hm2DevMgmtSwBugfixRelNum=_Hm2DevMgmtSwBugfixRelNum_Object((1,3,6,1,4,1,248,11,10,1,3,1,10,1,8),_Hm2DevMgmtSwBugfixRelNum_Type())
hm2DevMgmtSwBugfixRelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwBugfixRelNum.setStatus(_A)
_Hm2DeviceMgmtHardwareGroup_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtHardwareGroup=_Hm2DeviceMgmtHardwareGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,4))
_Hm2DevMgmtHwVersion_Type=DisplayString
_Hm2DevMgmtHwVersion_Object=MibScalar
hm2DevMgmtHwVersion=_Hm2DevMgmtHwVersion_Object((1,3,6,1,4,1,248,11,10,1,4,1),_Hm2DevMgmtHwVersion_Type())
hm2DevMgmtHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtHwVersion.setStatus(_A)
_Hm2DevMgmtSwitchingCoreVersion_Type=DisplayString
_Hm2DevMgmtSwitchingCoreVersion_Object=MibScalar
hm2DevMgmtSwitchingCoreVersion=_Hm2DevMgmtSwitchingCoreVersion_Object((1,3,6,1,4,1,248,11,10,1,4,2),_Hm2DevMgmtSwitchingCoreVersion_Type())
hm2DevMgmtSwitchingCoreVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtSwitchingCoreVersion.setStatus(_A)
_Hm2DeviceMgmtLogicVersionGroup_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtLogicVersionGroup=_Hm2DeviceMgmtLogicVersionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,4,5))
_Hm2DevMgmtLogicVersTable_Object=MibTable
hm2DevMgmtLogicVersTable=_Hm2DevMgmtLogicVersTable_Object((1,3,6,1,4,1,248,11,10,1,4,5,1))
if mibBuilder.loadTexts:hm2DevMgmtLogicVersTable.setStatus(_A)
_Hm2DevMgmtLogicVersEntry_Object=MibTableRow
hm2DevMgmtLogicVersEntry=_Hm2DevMgmtLogicVersEntry_Object((1,3,6,1,4,1,248,11,10,1,4,5,1,1))
hm2DevMgmtLogicVersEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:hm2DevMgmtLogicVersEntry.setStatus(_A)
class _Hm2DevMgmtLogicIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Hm2DevMgmtLogicIdx_Type.__name__=_C
_Hm2DevMgmtLogicIdx_Object=MibTableColumn
hm2DevMgmtLogicIdx=_Hm2DevMgmtLogicIdx_Object((1,3,6,1,4,1,248,11,10,1,4,5,1,1,1),_Hm2DevMgmtLogicIdx_Type())
hm2DevMgmtLogicIdx.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DevMgmtLogicIdx.setStatus(_A)
_Hm2DevMgmtLogicAddress_Type=DisplayString
_Hm2DevMgmtLogicAddress_Object=MibTableColumn
hm2DevMgmtLogicAddress=_Hm2DevMgmtLogicAddress_Object((1,3,6,1,4,1,248,11,10,1,4,5,1,1,2),_Hm2DevMgmtLogicAddress_Type())
hm2DevMgmtLogicAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtLogicAddress.setStatus(_A)
_Hm2DevMgmtLogicVersion_Type=DisplayString
_Hm2DevMgmtLogicVersion_Object=MibTableColumn
hm2DevMgmtLogicVersion=_Hm2DevMgmtLogicVersion_Object((1,3,6,1,4,1,248,11,10,1,4,5,1,1,3),_Hm2DevMgmtLogicVersion_Type())
hm2DevMgmtLogicVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtLogicVersion.setStatus(_A)
_Hm2DeviceMgmtTemperatureGroup_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtTemperatureGroup=_Hm2DeviceMgmtTemperatureGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,5))
_Hm2DevMgmtTemperature_Type=Integer32
_Hm2DevMgmtTemperature_Object=MibScalar
hm2DevMgmtTemperature=_Hm2DevMgmtTemperature_Object((1,3,6,1,4,1,248,11,10,1,5,1),_Hm2DevMgmtTemperature_Type())
hm2DevMgmtTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtTemperature.setStatus(_A)
class _Hm2DevMgmtTemperatureUpperLimit_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,99))
_Hm2DevMgmtTemperatureUpperLimit_Type.__name__=_C
_Hm2DevMgmtTemperatureUpperLimit_Object=MibScalar
hm2DevMgmtTemperatureUpperLimit=_Hm2DevMgmtTemperatureUpperLimit_Object((1,3,6,1,4,1,248,11,10,1,5,2),_Hm2DevMgmtTemperatureUpperLimit_Type())
hm2DevMgmtTemperatureUpperLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtTemperatureUpperLimit.setStatus(_A)
class _Hm2DevMgmtTemperatureLowerLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,99))
_Hm2DevMgmtTemperatureLowerLimit_Type.__name__=_C
_Hm2DevMgmtTemperatureLowerLimit_Object=MibScalar
hm2DevMgmtTemperatureLowerLimit=_Hm2DevMgmtTemperatureLowerLimit_Object((1,3,6,1,4,1,248,11,10,1,5,3),_Hm2DevMgmtTemperatureLowerLimit_Type())
hm2DevMgmtTemperatureLowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtTemperatureLowerLimit.setStatus(_A)
_Hm2DevMgmtTemperatureExtTable_Object=MibTable
hm2DevMgmtTemperatureExtTable=_Hm2DevMgmtTemperatureExtTable_Object((1,3,6,1,4,1,248,11,10,1,5,10))
if mibBuilder.loadTexts:hm2DevMgmtTemperatureExtTable.setStatus(_A)
_Hm2DevMgmtTemperatureExtEntry_Object=MibTableRow
hm2DevMgmtTemperatureExtEntry=_Hm2DevMgmtTemperatureExtEntry_Object((1,3,6,1,4,1,248,11,10,1,5,10,1))
hm2DevMgmtTemperatureExtEntry.setIndexNames((0,_E,_L),(0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:hm2DevMgmtTemperatureExtEntry.setStatus(_A)
class _Hm2DevMgmtTemperatureExtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,10)));namedValues=NamedValues(*(('mainboard',1),('module',2),('switch',3),('cpu',4),('phy',5),(_F,10)))
_Hm2DevMgmtTemperatureExtType_Type.__name__=_C
_Hm2DevMgmtTemperatureExtType_Object=MibTableColumn
hm2DevMgmtTemperatureExtType=_Hm2DevMgmtTemperatureExtType_Object((1,3,6,1,4,1,248,11,10,1,5,10,1,1),_Hm2DevMgmtTemperatureExtType_Type())
hm2DevMgmtTemperatureExtType.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DevMgmtTemperatureExtType.setStatus(_A)
class _Hm2DevMgmtTemperatureExtSensorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Hm2DevMgmtTemperatureExtSensorId_Type.__name__=_C
_Hm2DevMgmtTemperatureExtSensorId_Object=MibTableColumn
hm2DevMgmtTemperatureExtSensorId=_Hm2DevMgmtTemperatureExtSensorId_Object((1,3,6,1,4,1,248,11,10,1,5,10,1,2),_Hm2DevMgmtTemperatureExtSensorId_Type())
hm2DevMgmtTemperatureExtSensorId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtTemperatureExtSensorId.setStatus(_A)
_Hm2DevMgmtTemperatureExt_Type=Integer32
_Hm2DevMgmtTemperatureExt_Object=MibTableColumn
hm2DevMgmtTemperatureExt=_Hm2DevMgmtTemperatureExt_Object((1,3,6,1,4,1,248,11,10,1,5,10,1,3),_Hm2DevMgmtTemperatureExt_Type())
hm2DevMgmtTemperatureExt.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtTemperatureExt.setStatus(_A)
class _Hm2DevMgmtTemperatureExtUpperLimit_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,99))
_Hm2DevMgmtTemperatureExtUpperLimit_Type.__name__=_C
_Hm2DevMgmtTemperatureExtUpperLimit_Object=MibTableColumn
hm2DevMgmtTemperatureExtUpperLimit=_Hm2DevMgmtTemperatureExtUpperLimit_Object((1,3,6,1,4,1,248,11,10,1,5,10,1,4),_Hm2DevMgmtTemperatureExtUpperLimit_Type())
hm2DevMgmtTemperatureExtUpperLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtTemperatureExtUpperLimit.setStatus(_A)
class _Hm2DevMgmtTemperatureExtLowerLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,99))
_Hm2DevMgmtTemperatureExtLowerLimit_Type.__name__=_C
_Hm2DevMgmtTemperatureExtLowerLimit_Object=MibTableColumn
hm2DevMgmtTemperatureExtLowerLimit=_Hm2DevMgmtTemperatureExtLowerLimit_Object((1,3,6,1,4,1,248,11,10,1,5,10,1,5),_Hm2DevMgmtTemperatureExtLowerLimit_Type())
hm2DevMgmtTemperatureExtLowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtTemperatureExtLowerLimit.setStatus(_A)
_Hm2IfaceGroup_ObjectIdentity=ObjectIdentity
hm2IfaceGroup=_Hm2IfaceGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,6))
_Hm2IfaceTable_Object=MibTable
hm2IfaceTable=_Hm2IfaceTable_Object((1,3,6,1,4,1,248,11,10,1,6,1))
if mibBuilder.loadTexts:hm2IfaceTable.setStatus(_A)
_Hm2IfaceEntry_Object=MibTableRow
hm2IfaceEntry=_Hm2IfaceEntry_Object((1,3,6,1,4,1,248,11,10,1,6,1,1))
hm2IfaceEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:hm2IfaceEntry.setStatus(_A)
_Hm2IfacePhysIndex_Type=Integer32
_Hm2IfacePhysIndex_Object=MibTableColumn
hm2IfacePhysIndex=_Hm2IfacePhysIndex_Object((1,3,6,1,4,1,248,11,10,1,6,1,1,1),_Hm2IfacePhysIndex_Type())
hm2IfacePhysIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:hm2IfacePhysIndex.setStatus(_A)
class _Hm2IfacePortCapabilityBits_Type(Bits):namedValues=NamedValues(*(('manual-mdix',0),(_d,1),(_e,2),(_f,3),('cable-test',4),('poe',5),('poe-plus',6),('poe-ext',7)))
_Hm2IfacePortCapabilityBits_Type.__name__=_M
_Hm2IfacePortCapabilityBits_Object=MibTableColumn
hm2IfacePortCapabilityBits=_Hm2IfacePortCapabilityBits_Object((1,3,6,1,4,1,248,11,10,1,6,1,1,2),_Hm2IfacePortCapabilityBits_Type())
hm2IfacePortCapabilityBits.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IfacePortCapabilityBits.setStatus(_A)
class _Hm2IfaceCableCrossing_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mdi',1),('mdix',2),(_d,3),(_N,4)))
_Hm2IfaceCableCrossing_Type.__name__=_C
_Hm2IfaceCableCrossing_Object=MibTableColumn
hm2IfaceCableCrossing=_Hm2IfaceCableCrossing_Object((1,3,6,1,4,1,248,11,10,1,6,1,1,3),_Hm2IfaceCableCrossing_Type())
hm2IfaceCableCrossing.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2IfaceCableCrossing.setStatus(_A)
class _Hm2IfacePowerState_Type(HmEnabledStatus):defaultValue=2
_Hm2IfacePowerState_Type.__name__=_G
_Hm2IfacePowerState_Object=MibTableColumn
hm2IfacePowerState=_Hm2IfacePowerState_Object((1,3,6,1,4,1,248,11,10,1,6,1,1,4),_Hm2IfacePowerState_Type())
hm2IfacePowerState.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2IfacePowerState.setStatus(_A)
class _Hm2IfaceAutoPowerDown_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),('no-power-save',2),(_f,3),(_N,4)))
_Hm2IfaceAutoPowerDown_Type.__name__=_C
_Hm2IfaceAutoPowerDown_Object=MibTableColumn
hm2IfaceAutoPowerDown=_Hm2IfaceAutoPowerDown_Object((1,3,6,1,4,1,248,11,10,1,6,1,1,5),_Hm2IfaceAutoPowerDown_Type())
hm2IfaceAutoPowerDown.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2IfaceAutoPowerDown.setStatus(_A)
class _Hm2IfaceOperAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_Hm2IfaceOperAdminStatus_Type.__name__=_C
_Hm2IfaceOperAdminStatus_Object=MibTableColumn
hm2IfaceOperAdminStatus=_Hm2IfaceOperAdminStatus_Object((1,3,6,1,4,1,248,11,10,1,6,1,1,6),_Hm2IfaceOperAdminStatus_Type())
hm2IfaceOperAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IfaceOperAdminStatus.setStatus(_A)
_Hm2IfaceLayoutTable_Object=MibTable
hm2IfaceLayoutTable=_Hm2IfaceLayoutTable_Object((1,3,6,1,4,1,248,11,10,1,6,2))
if mibBuilder.loadTexts:hm2IfaceLayoutTable.setStatus(_A)
_Hm2IfaceLayoutEntry_Object=MibTableRow
hm2IfaceLayoutEntry=_Hm2IfaceLayoutEntry_Object((1,3,6,1,4,1,248,11,10,1,6,2,1))
hm2IfaceLayoutEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:hm2IfaceLayoutEntry.setStatus(_A)
_Hm2IfaceLayoutIndex_Type=Integer32
_Hm2IfaceLayoutIndex_Object=MibTableColumn
hm2IfaceLayoutIndex=_Hm2IfaceLayoutIndex_Object((1,3,6,1,4,1,248,11,10,1,6,2,1,1),_Hm2IfaceLayoutIndex_Type())
hm2IfaceLayoutIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2IfaceLayoutIndex.setStatus(_A)
_Hm2IfaceLayoutStartIfIndex_Type=InterfaceIndexOrZero
_Hm2IfaceLayoutStartIfIndex_Object=MibTableColumn
hm2IfaceLayoutStartIfIndex=_Hm2IfaceLayoutStartIfIndex_Object((1,3,6,1,4,1,248,11,10,1,6,2,1,2),_Hm2IfaceLayoutStartIfIndex_Type())
hm2IfaceLayoutStartIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IfaceLayoutStartIfIndex.setStatus(_A)
_Hm2IfaceLayoutEndIfIndex_Type=InterfaceIndexOrZero
_Hm2IfaceLayoutEndIfIndex_Object=MibTableColumn
hm2IfaceLayoutEndIfIndex=_Hm2IfaceLayoutEndIfIndex_Object((1,3,6,1,4,1,248,11,10,1,6,2,1,3),_Hm2IfaceLayoutEndIfIndex_Type())
hm2IfaceLayoutEndIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IfaceLayoutEndIfIndex.setStatus(_A)
_Hm2IfaceLayoutModuleCapacity_Type=Unsigned32
_Hm2IfaceLayoutModuleCapacity_Object=MibTableColumn
hm2IfaceLayoutModuleCapacity=_Hm2IfaceLayoutModuleCapacity_Object((1,3,6,1,4,1,248,11,10,1,6,2,1,4),_Hm2IfaceLayoutModuleCapacity_Type())
hm2IfaceLayoutModuleCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IfaceLayoutModuleCapacity.setStatus(_A)
_Hm2IfaceLayoutModulePortCapacity_Type=Unsigned32
_Hm2IfaceLayoutModulePortCapacity_Object=MibTableColumn
hm2IfaceLayoutModulePortCapacity=_Hm2IfaceLayoutModulePortCapacity_Object((1,3,6,1,4,1,248,11,10,1,6,2,1,5),_Hm2IfaceLayoutModulePortCapacity_Type())
hm2IfaceLayoutModulePortCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IfaceLayoutModulePortCapacity.setStatus(_A)
_Hm2IfaceLayoutFormat_Type=SnmpAdminString
_Hm2IfaceLayoutFormat_Object=MibTableColumn
hm2IfaceLayoutFormat=_Hm2IfaceLayoutFormat_Object((1,3,6,1,4,1,248,11,10,1,6,2,1,6),_Hm2IfaceLayoutFormat_Type())
hm2IfaceLayoutFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IfaceLayoutFormat.setStatus(_A)
_Hm2IfaceLayoutIfIndexType_Type=IANAifType
_Hm2IfaceLayoutIfIndexType_Object=MibTableColumn
hm2IfaceLayoutIfIndexType=_Hm2IfaceLayoutIfIndexType_Object((1,3,6,1,4,1,248,11,10,1,6,2,1,7),_Hm2IfaceLayoutIfIndexType_Type())
hm2IfaceLayoutIfIndexType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IfaceLayoutIfIndexType.setStatus(_A)
_Hm2IfaceExtTable_Object=MibTable
hm2IfaceExtTable=_Hm2IfaceExtTable_Object((1,3,6,1,4,1,248,11,10,1,6,3))
if mibBuilder.loadTexts:hm2IfaceExtTable.setStatus(_A)
_Hm2IfaceExtEntry_Object=MibTableRow
hm2IfaceExtEntry=_Hm2IfaceExtEntry_Object((1,3,6,1,4,1,248,11,10,1,6,3,1))
hm2IfaceExtEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hm2IfaceExtEntry.setStatus(_A)
class _Hm2IfaceExtIfRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,24,136,161,169,1001,1002,1003,1004,1005,1006,1007,1008,1101,1102,1201,1202)));namedValues=NamedValues(*(('ethernetCsmacd',6),('softwareLoopback',24),('l3ipvlan',136),('ieee8023adLag',161),('shdsl',169),('ringPort',1001),('subringPort',1002),('couplingPort',1003),('routerPort',1004),('probePort',1005),('cpuPort',1006),('servicePort',1007),('outOfBandMgmtPort',1008),('lagMember',1101),('lreMember',1102),('lreInterface',1201),('ringLagInterface',1202)))
_Hm2IfaceExtIfRole_Type.__name__=_C
_Hm2IfaceExtIfRole_Object=MibTableColumn
hm2IfaceExtIfRole=_Hm2IfaceExtIfRole_Object((1,3,6,1,4,1,248,11,10,1,6,3,1,1),_Hm2IfaceExtIfRole_Type())
hm2IfaceExtIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IfaceExtIfRole.setStatus(_A)
_Hm2SfpGroup_ObjectIdentity=ObjectIdentity
hm2SfpGroup=_Hm2SfpGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,7))
_Hm2SfpInfoTable_Object=MibTable
hm2SfpInfoTable=_Hm2SfpInfoTable_Object((1,3,6,1,4,1,248,11,10,1,7,1))
if mibBuilder.loadTexts:hm2SfpInfoTable.setStatus(_A)
_Hm2SfpInfoEntry_Object=MibTableRow
hm2SfpInfoEntry=_Hm2SfpInfoEntry_Object((1,3,6,1,4,1,248,11,10,1,7,1,1))
hm2SfpInfoEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hm2SfpInfoEntry.setStatus(_A)
class _Hm2SfpModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,6)));namedValues=NamedValues(*(('sfp',3),('xfp',6)))
_Hm2SfpModuleType_Type.__name__=_C
_Hm2SfpModuleType_Object=MibTableColumn
hm2SfpModuleType=_Hm2SfpModuleType_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,1),_Hm2SfpModuleType_Type())
hm2SfpModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpModuleType.setStatus(_A)
class _Hm2SfpMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6,8,9,10,11,12,13,14,15,16,17,18,30,31,32,40,41,50)));namedValues=NamedValues(*(('ge-1000-base-sx',1),('ge-1000-base-lx',2),('ge-1000-base-cx',4),('fe-100base-lx',5),('fe-100base-fx',6),('ge-1000-base-t',8),(_N,9),('oc3-mm-sr',10),('oc3-sm-ir',11),('oc3-sm-lr',12),('oc12-mm-sr',13),('oc12-sm-ir',14),('oc12-sm-lr',15),('oc48-sr',16),('oc48-ir',17),('oc48-lr',18),('xfp-10gbase-sr',30),('xfp-10gbase-lr',31),('xfp-10gbase-er',32),('microfx',40),('pof',41),('m-sfp-2500',50)))
_Hm2SfpMediaType_Type.__name__=_C
_Hm2SfpMediaType_Object=MibTableColumn
hm2SfpMediaType=_Hm2SfpMediaType_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,2),_Hm2SfpMediaType_Type())
hm2SfpMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpMediaType.setStatus(_A)
class _Hm2SfpConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,7,8,11,33,34,128)));namedValues=NamedValues(*(('nonSfp',1),('fiberjack',6),('lc',7),('mtrj',8),('opticalPigtail',11),('copperPigtail',33),('rj45',34),('vendorSpecific',128)))
_Hm2SfpConnector_Type.__name__=_C
_Hm2SfpConnector_Object=MibTableColumn
hm2SfpConnector=_Hm2SfpConnector_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,3),_Hm2SfpConnector_Type())
hm2SfpConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpConnector.setStatus(_A)
_Hm2SfpVendorName_Type=SnmpAdminString
_Hm2SfpVendorName_Object=MibTableColumn
hm2SfpVendorName=_Hm2SfpVendorName_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,4),_Hm2SfpVendorName_Type())
hm2SfpVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpVendorName.setStatus(_A)
_Hm2SfpVendorOUI_Type=OctetString
_Hm2SfpVendorOUI_Object=MibTableColumn
hm2SfpVendorOUI=_Hm2SfpVendorOUI_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,5),_Hm2SfpVendorOUI_Type())
hm2SfpVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpVendorOUI.setStatus(_A)
_Hm2SfpPartNumber_Type=SnmpAdminString
_Hm2SfpPartNumber_Object=MibTableColumn
hm2SfpPartNumber=_Hm2SfpPartNumber_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,6),_Hm2SfpPartNumber_Type())
hm2SfpPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpPartNumber.setStatus(_A)
_Hm2SfpPartRev_Type=SnmpAdminString
_Hm2SfpPartRev_Object=MibTableColumn
hm2SfpPartRev=_Hm2SfpPartRev_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,7),_Hm2SfpPartRev_Type())
hm2SfpPartRev.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpPartRev.setStatus(_A)
_Hm2SfpSerialNum_Type=SnmpAdminString
_Hm2SfpSerialNum_Object=MibTableColumn
hm2SfpSerialNum=_Hm2SfpSerialNum_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,8),_Hm2SfpSerialNum_Type())
hm2SfpSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpSerialNum.setStatus(_A)
_Hm2SfpDateCode_Type=SnmpAdminString
_Hm2SfpDateCode_Object=MibTableColumn
hm2SfpDateCode=_Hm2SfpDateCode_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,9),_Hm2SfpDateCode_Type())
hm2SfpDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpDateCode.setStatus(_A)
_Hm2SfpInfoVersion_Type=Integer32
_Hm2SfpInfoVersion_Object=MibTableColumn
hm2SfpInfoVersion=_Hm2SfpInfoVersion_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,10),_Hm2SfpInfoVersion_Type())
hm2SfpInfoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpInfoVersion.setStatus(_A)
class _Hm2SfpInfoPartNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Hm2SfpInfoPartNumber_Type.__name__=_P
_Hm2SfpInfoPartNumber_Object=MibTableColumn
hm2SfpInfoPartNumber=_Hm2SfpInfoPartNumber_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,11),_Hm2SfpInfoPartNumber_Type())
hm2SfpInfoPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpInfoPartNumber.setStatus(_A)
class _Hm2SfpInfoPartId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Hm2SfpInfoPartId_Type.__name__=_P
_Hm2SfpInfoPartId_Object=MibTableColumn
hm2SfpInfoPartId=_Hm2SfpInfoPartId_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,12),_Hm2SfpInfoPartId_Type())
hm2SfpInfoPartId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpInfoPartId.setStatus(_A)
_Hm2SfpBitRateNominal_Type=Integer32
_Hm2SfpBitRateNominal_Object=MibTableColumn
hm2SfpBitRateNominal=_Hm2SfpBitRateNominal_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,13),_Hm2SfpBitRateNominal_Type())
hm2SfpBitRateNominal.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpBitRateNominal.setStatus(_A)
_Hm2SfpBitRateMin_Type=Integer32
_Hm2SfpBitRateMin_Object=MibTableColumn
hm2SfpBitRateMin=_Hm2SfpBitRateMin_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,14),_Hm2SfpBitRateMin_Type())
hm2SfpBitRateMin.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpBitRateMin.setStatus(_A)
_Hm2SfpBitRateMax_Type=Integer32
_Hm2SfpBitRateMax_Object=MibTableColumn
hm2SfpBitRateMax=_Hm2SfpBitRateMax_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,15),_Hm2SfpBitRateMax_Type())
hm2SfpBitRateMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpBitRateMax.setStatus(_A)
_Hm2SfpMaxLength_fiber_9_Type=Integer32
_Hm2SfpMaxLength_fiber_9_Object=MibTableColumn
hm2SfpMaxLength_fiber_9=_Hm2SfpMaxLength_fiber_9_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,16),_Hm2SfpMaxLength_fiber_9_Type())
hm2SfpMaxLength_fiber_9.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpMaxLength_fiber_9.setStatus(_A)
_Hm2SfpMaxLength_fiber_50_Type=Integer32
_Hm2SfpMaxLength_fiber_50_Object=MibTableColumn
hm2SfpMaxLength_fiber_50=_Hm2SfpMaxLength_fiber_50_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,17),_Hm2SfpMaxLength_fiber_50_Type())
hm2SfpMaxLength_fiber_50.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpMaxLength_fiber_50.setStatus(_A)
_Hm2SfpMaxLength_fiber_e50_Type=Integer32
_Hm2SfpMaxLength_fiber_e50_Object=MibTableColumn
hm2SfpMaxLength_fiber_e50=_Hm2SfpMaxLength_fiber_e50_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,18),_Hm2SfpMaxLength_fiber_e50_Type())
hm2SfpMaxLength_fiber_e50.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpMaxLength_fiber_e50.setStatus(_A)
_Hm2SfpMaxLength_fiber_62_5_Type=Integer32
_Hm2SfpMaxLength_fiber_62_5_Object=MibTableColumn
hm2SfpMaxLength_fiber_62_5=_Hm2SfpMaxLength_fiber_62_5_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,19),_Hm2SfpMaxLength_fiber_62_5_Type())
hm2SfpMaxLength_fiber_62_5.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpMaxLength_fiber_62_5.setStatus(_A)
_Hm2SfpMaxLength_copper_Type=Integer32
_Hm2SfpMaxLength_copper_Object=MibTableColumn
hm2SfpMaxLength_copper=_Hm2SfpMaxLength_copper_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,20),_Hm2SfpMaxLength_copper_Type())
hm2SfpMaxLength_copper.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpMaxLength_copper.setStatus(_A)
_Hm2SfpWaveLength_Type=Integer32
_Hm2SfpWaveLength_Object=MibTableColumn
hm2SfpWaveLength=_Hm2SfpWaveLength_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,21),_Hm2SfpWaveLength_Type())
hm2SfpWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpWaveLength.setStatus(_A)
_Hm2SfpWaveLengthTolerance_Type=Integer32
_Hm2SfpWaveLengthTolerance_Object=MibTableColumn
hm2SfpWaveLengthTolerance=_Hm2SfpWaveLengthTolerance_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,22),_Hm2SfpWaveLengthTolerance_Type())
hm2SfpWaveLengthTolerance.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpWaveLengthTolerance.setStatus(_A)
class _Hm2SfpEnhancedOptions_Type(Bits):namedValues=NamedValues((_Q,0))
_Hm2SfpEnhancedOptions_Type.__name__=_M
_Hm2SfpEnhancedOptions_Object=MibTableColumn
hm2SfpEnhancedOptions=_Hm2SfpEnhancedOptions_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,23),_Hm2SfpEnhancedOptions_Type())
hm2SfpEnhancedOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpEnhancedOptions.setStatus(_A)
_Hm2SfpSupported_Type=TruthValue
_Hm2SfpSupported_Object=MibTableColumn
hm2SfpSupported=_Hm2SfpSupported_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,24),_Hm2SfpSupported_Type())
hm2SfpSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpSupported.setStatus(_A)
class _Hm2SfpSupportedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('hirschmannID',1),('whiteList',2),('wrongSpeed',3),('noneEthernet',4),('tpSfpNotSupported',5),('otnID',6)))
_Hm2SfpSupportedReason_Type.__name__=_C
_Hm2SfpSupportedReason_Object=MibTableColumn
hm2SfpSupportedReason=_Hm2SfpSupportedReason_Object((1,3,6,1,4,1,248,11,10,1,7,1,1,25),_Hm2SfpSupportedReason_Type())
hm2SfpSupportedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpSupportedReason.setStatus(_A)
_Hm2SfpDiagTable_Object=MibTable
hm2SfpDiagTable=_Hm2SfpDiagTable_Object((1,3,6,1,4,1,248,11,10,1,7,2))
if mibBuilder.loadTexts:hm2SfpDiagTable.setStatus(_A)
_Hm2SfpDiagEntry_Object=MibTableRow
hm2SfpDiagEntry=_Hm2SfpDiagEntry_Object((1,3,6,1,4,1,248,11,10,1,7,2,1))
hm2SfpDiagEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hm2SfpDiagEntry.setStatus(_A)
_Hm2SfpCurrentBitRate_Type=Integer32
_Hm2SfpCurrentBitRate_Object=MibTableColumn
hm2SfpCurrentBitRate=_Hm2SfpCurrentBitRate_Object((1,3,6,1,4,1,248,11,10,1,7,2,1,1),_Hm2SfpCurrentBitRate_Type())
hm2SfpCurrentBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpCurrentBitRate.setStatus(_A)
_Hm2SfpCurrentTemperature_Type=Integer32
_Hm2SfpCurrentTemperature_Object=MibTableColumn
hm2SfpCurrentTemperature=_Hm2SfpCurrentTemperature_Object((1,3,6,1,4,1,248,11,10,1,7,2,1,2),_Hm2SfpCurrentTemperature_Type())
hm2SfpCurrentTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpCurrentTemperature.setStatus(_A)
_Hm2SfpCurrentTxPower_Type=Integer32
_Hm2SfpCurrentTxPower_Object=MibTableColumn
hm2SfpCurrentTxPower=_Hm2SfpCurrentTxPower_Object((1,3,6,1,4,1,248,11,10,1,7,2,1,3),_Hm2SfpCurrentTxPower_Type())
hm2SfpCurrentTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpCurrentTxPower.setStatus(_A)
_Hm2SfpCurrentRxPower_Type=Integer32
_Hm2SfpCurrentRxPower_Object=MibTableColumn
hm2SfpCurrentRxPower=_Hm2SfpCurrentRxPower_Object((1,3,6,1,4,1,248,11,10,1,7,2,1,4),_Hm2SfpCurrentRxPower_Type())
hm2SfpCurrentRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpCurrentRxPower.setStatus(_A)
_Hm2SfpCurrentTxPowerdBm_Type=SnmpAdminString
_Hm2SfpCurrentTxPowerdBm_Object=MibTableColumn
hm2SfpCurrentTxPowerdBm=_Hm2SfpCurrentTxPowerdBm_Object((1,3,6,1,4,1,248,11,10,1,7,2,1,5),_Hm2SfpCurrentTxPowerdBm_Type())
hm2SfpCurrentTxPowerdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpCurrentTxPowerdBm.setStatus(_A)
_Hm2SfpCurrentRxPowerdBm_Type=SnmpAdminString
_Hm2SfpCurrentRxPowerdBm_Object=MibTableColumn
hm2SfpCurrentRxPowerdBm=_Hm2SfpCurrentRxPowerdBm_Object((1,3,6,1,4,1,248,11,10,1,7,2,1,6),_Hm2SfpCurrentRxPowerdBm_Type())
hm2SfpCurrentRxPowerdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpCurrentRxPowerdBm.setStatus(_A)
class _Hm2SfpCurrentRxPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('warning',2),('alarm',3),(_N,4)))
_Hm2SfpCurrentRxPowerState_Type.__name__=_C
_Hm2SfpCurrentRxPowerState_Object=MibTableColumn
hm2SfpCurrentRxPowerState=_Hm2SfpCurrentRxPowerState_Object((1,3,6,1,4,1,248,11,10,1,7,2,1,7),_Hm2SfpCurrentRxPowerState_Type())
hm2SfpCurrentRxPowerState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpCurrentRxPowerState.setStatus(_A)
_Hm2SfpWLGroup_ObjectIdentity=ObjectIdentity
hm2SfpWLGroup=_Hm2SfpWLGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,7,3))
class _Hm2SfpWLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('present',1),('absent',2),('not-supported',3)))
_Hm2SfpWLStatus_Type.__name__=_C
_Hm2SfpWLStatus_Object=MibScalar
hm2SfpWLStatus=_Hm2SfpWLStatus_Object((1,3,6,1,4,1,248,11,10,1,7,3,1),_Hm2SfpWLStatus_Type())
hm2SfpWLStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpWLStatus.setStatus(_A)
_Hm2SfpThresholdTable_Object=MibTable
hm2SfpThresholdTable=_Hm2SfpThresholdTable_Object((1,3,6,1,4,1,248,11,10,1,7,4))
if mibBuilder.loadTexts:hm2SfpThresholdTable.setStatus(_A)
_Hm2SfpThresholdEntry_Object=MibTableRow
hm2SfpThresholdEntry=_Hm2SfpThresholdEntry_Object((1,3,6,1,4,1,248,11,10,1,7,4,1))
hm2SfpThresholdEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hm2SfpThresholdEntry.setStatus(_A)
_Hm2SfpTemperatureHighAlarm_Type=Integer32
_Hm2SfpTemperatureHighAlarm_Object=MibTableColumn
hm2SfpTemperatureHighAlarm=_Hm2SfpTemperatureHighAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,1),_Hm2SfpTemperatureHighAlarm_Type())
hm2SfpTemperatureHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTemperatureHighAlarm.setStatus(_A)
_Hm2SfpTemperatureHighWarning_Type=Integer32
_Hm2SfpTemperatureHighWarning_Object=MibTableColumn
hm2SfpTemperatureHighWarning=_Hm2SfpTemperatureHighWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,2),_Hm2SfpTemperatureHighWarning_Type())
hm2SfpTemperatureHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTemperatureHighWarning.setStatus(_A)
_Hm2SfpTemperatureLowAlarm_Type=Integer32
_Hm2SfpTemperatureLowAlarm_Object=MibTableColumn
hm2SfpTemperatureLowAlarm=_Hm2SfpTemperatureLowAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,3),_Hm2SfpTemperatureLowAlarm_Type())
hm2SfpTemperatureLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTemperatureLowAlarm.setStatus(_A)
_Hm2SfpTemperatureLowWarning_Type=Integer32
_Hm2SfpTemperatureLowWarning_Object=MibTableColumn
hm2SfpTemperatureLowWarning=_Hm2SfpTemperatureLowWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,4),_Hm2SfpTemperatureLowWarning_Type())
hm2SfpTemperatureLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTemperatureLowWarning.setStatus(_A)
_Hm2SfpTxPowerHighAlarm_Type=Integer32
_Hm2SfpTxPowerHighAlarm_Object=MibTableColumn
hm2SfpTxPowerHighAlarm=_Hm2SfpTxPowerHighAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,5),_Hm2SfpTxPowerHighAlarm_Type())
hm2SfpTxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTxPowerHighAlarm.setStatus(_A)
_Hm2SfpTxPowerHighWarning_Type=Integer32
_Hm2SfpTxPowerHighWarning_Object=MibTableColumn
hm2SfpTxPowerHighWarning=_Hm2SfpTxPowerHighWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,6),_Hm2SfpTxPowerHighWarning_Type())
hm2SfpTxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTxPowerHighWarning.setStatus(_A)
_Hm2SfpTxPowerLowAlarm_Type=Integer32
_Hm2SfpTxPowerLowAlarm_Object=MibTableColumn
hm2SfpTxPowerLowAlarm=_Hm2SfpTxPowerLowAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,7),_Hm2SfpTxPowerLowAlarm_Type())
hm2SfpTxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTxPowerLowAlarm.setStatus(_A)
_Hm2SfpTxPowerLowWarning_Type=Integer32
_Hm2SfpTxPowerLowWarning_Object=MibTableColumn
hm2SfpTxPowerLowWarning=_Hm2SfpTxPowerLowWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,8),_Hm2SfpTxPowerLowWarning_Type())
hm2SfpTxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTxPowerLowWarning.setStatus(_A)
_Hm2SfpRxPowerHighAlarm_Type=Integer32
_Hm2SfpRxPowerHighAlarm_Object=MibTableColumn
hm2SfpRxPowerHighAlarm=_Hm2SfpRxPowerHighAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,9),_Hm2SfpRxPowerHighAlarm_Type())
hm2SfpRxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpRxPowerHighAlarm.setStatus(_A)
_Hm2SfpRxPowerHighWarning_Type=Integer32
_Hm2SfpRxPowerHighWarning_Object=MibTableColumn
hm2SfpRxPowerHighWarning=_Hm2SfpRxPowerHighWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,10),_Hm2SfpRxPowerHighWarning_Type())
hm2SfpRxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpRxPowerHighWarning.setStatus(_A)
_Hm2SfpRxPowerLowAlarm_Type=Integer32
_Hm2SfpRxPowerLowAlarm_Object=MibTableColumn
hm2SfpRxPowerLowAlarm=_Hm2SfpRxPowerLowAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,11),_Hm2SfpRxPowerLowAlarm_Type())
hm2SfpRxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpRxPowerLowAlarm.setStatus(_A)
_Hm2SfpRxPowerLowWarning_Type=Integer32
_Hm2SfpRxPowerLowWarning_Object=MibTableColumn
hm2SfpRxPowerLowWarning=_Hm2SfpRxPowerLowWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,12),_Hm2SfpRxPowerLowWarning_Type())
hm2SfpRxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpRxPowerLowWarning.setStatus(_A)
_Hm2SfpTxPowerdBmHighAlarm_Type=SnmpAdminString
_Hm2SfpTxPowerdBmHighAlarm_Object=MibTableColumn
hm2SfpTxPowerdBmHighAlarm=_Hm2SfpTxPowerdBmHighAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,13),_Hm2SfpTxPowerdBmHighAlarm_Type())
hm2SfpTxPowerdBmHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTxPowerdBmHighAlarm.setStatus(_A)
_Hm2SfpTxPowerdBmHighWarning_Type=SnmpAdminString
_Hm2SfpTxPowerdBmHighWarning_Object=MibTableColumn
hm2SfpTxPowerdBmHighWarning=_Hm2SfpTxPowerdBmHighWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,14),_Hm2SfpTxPowerdBmHighWarning_Type())
hm2SfpTxPowerdBmHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTxPowerdBmHighWarning.setStatus(_A)
_Hm2SfpTxPowerdBmLowAlarm_Type=SnmpAdminString
_Hm2SfpTxPowerdBmLowAlarm_Object=MibTableColumn
hm2SfpTxPowerdBmLowAlarm=_Hm2SfpTxPowerdBmLowAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,15),_Hm2SfpTxPowerdBmLowAlarm_Type())
hm2SfpTxPowerdBmLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTxPowerdBmLowAlarm.setStatus(_A)
_Hm2SfpTxPowerdBmLowWarning_Type=SnmpAdminString
_Hm2SfpTxPowerdBmLowWarning_Object=MibTableColumn
hm2SfpTxPowerdBmLowWarning=_Hm2SfpTxPowerdBmLowWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,16),_Hm2SfpTxPowerdBmLowWarning_Type())
hm2SfpTxPowerdBmLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpTxPowerdBmLowWarning.setStatus(_A)
_Hm2SfpRxPowerdBmHighAlarm_Type=SnmpAdminString
_Hm2SfpRxPowerdBmHighAlarm_Object=MibTableColumn
hm2SfpRxPowerdBmHighAlarm=_Hm2SfpRxPowerdBmHighAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,17),_Hm2SfpRxPowerdBmHighAlarm_Type())
hm2SfpRxPowerdBmHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpRxPowerdBmHighAlarm.setStatus(_A)
_Hm2SfpRxPowerdBmHighWarning_Type=SnmpAdminString
_Hm2SfpRxPowerdBmHighWarning_Object=MibTableColumn
hm2SfpRxPowerdBmHighWarning=_Hm2SfpRxPowerdBmHighWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,18),_Hm2SfpRxPowerdBmHighWarning_Type())
hm2SfpRxPowerdBmHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpRxPowerdBmHighWarning.setStatus(_A)
_Hm2SfpRxPowerdBmLowAlarm_Type=SnmpAdminString
_Hm2SfpRxPowerdBmLowAlarm_Object=MibTableColumn
hm2SfpRxPowerdBmLowAlarm=_Hm2SfpRxPowerdBmLowAlarm_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,19),_Hm2SfpRxPowerdBmLowAlarm_Type())
hm2SfpRxPowerdBmLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpRxPowerdBmLowAlarm.setStatus(_A)
_Hm2SfpRxPowerdBmLowWarning_Type=SnmpAdminString
_Hm2SfpRxPowerdBmLowWarning_Object=MibTableColumn
hm2SfpRxPowerdBmLowWarning=_Hm2SfpRxPowerdBmLowWarning_Object((1,3,6,1,4,1,248,11,10,1,7,4,1,20),_Hm2SfpRxPowerdBmLowWarning_Type())
hm2SfpRxPowerdBmLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SfpRxPowerdBmLowWarning.setStatus(_A)
_Hm2ExtNvmGroup_ObjectIdentity=ObjectIdentity
hm2ExtNvmGroup=_Hm2ExtNvmGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,8))
_Hm2ExtNvmGeneralGroup_ObjectIdentity=ObjectIdentity
hm2ExtNvmGeneralGroup=_Hm2ExtNvmGeneralGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,8,1))
class _Hm2ExtNvmChooseActive_Type(Hm2DeviceExtNVMType):defaultValue=1
_Hm2ExtNvmChooseActive_Type.__name__=_S
_Hm2ExtNvmChooseActive_Object=MibScalar
hm2ExtNvmChooseActive=_Hm2ExtNvmChooseActive_Object((1,3,6,1,4,1,248,11,10,1,8,1,1),_Hm2ExtNvmChooseActive_Type())
hm2ExtNvmChooseActive.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ExtNvmChooseActive.setStatus(_A)
class _Hm2ExtNvmLogDevice_Type(Hm2DeviceExtNVMType):defaultValue=1
_Hm2ExtNvmLogDevice_Type.__name__=_S
_Hm2ExtNvmLogDevice_Object=MibScalar
hm2ExtNvmLogDevice=_Hm2ExtNvmLogDevice_Object((1,3,6,1,4,1,248,11,10,1,8,1,2),_Hm2ExtNvmLogDevice_Type())
hm2ExtNvmLogDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ExtNvmLogDevice.setStatus(_A)
class _Hm2ExtNvmAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_Hm2ExtNvmAdminMode_Type.__name__=_C
_Hm2ExtNvmAdminMode_Object=MibScalar
hm2ExtNvmAdminMode=_Hm2ExtNvmAdminMode_Object((1,3,6,1,4,1,248,11,10,1,8,1,3),_Hm2ExtNvmAdminMode_Type())
hm2ExtNvmAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ExtNvmAdminMode.setStatus(_A)
class _Hm2ExtNvmOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_Hm2ExtNvmOperMode_Type.__name__=_C
_Hm2ExtNvmOperMode_Object=MibScalar
hm2ExtNvmOperMode=_Hm2ExtNvmOperMode_Object((1,3,6,1,4,1,248,11,10,1,8,1,4),_Hm2ExtNvmOperMode_Type())
hm2ExtNvmOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ExtNvmOperMode.setStatus(_A)
_Hm2ExtNvmTable_Object=MibTable
hm2ExtNvmTable=_Hm2ExtNvmTable_Object((1,3,6,1,4,1,248,11,10,1,8,2))
if mibBuilder.loadTexts:hm2ExtNvmTable.setStatus(_A)
_Hm2ExtNvmEntry_Object=MibTableRow
hm2ExtNvmEntry=_Hm2ExtNvmEntry_Object((1,3,6,1,4,1,248,11,10,1,8,2,1))
hm2ExtNvmEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:hm2ExtNvmEntry.setStatus(_A)
_Hm2ExtNvmTableIndex_Type=Hm2DeviceExtNVMType
_Hm2ExtNvmTableIndex_Object=MibTableColumn
hm2ExtNvmTableIndex=_Hm2ExtNvmTableIndex_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,1),_Hm2ExtNvmTableIndex_Type())
hm2ExtNvmTableIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2ExtNvmTableIndex.setStatus(_A)
class _Hm2ExtNvmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notPresent',1),('removed',2),('ok',3),('outOfMemory',4),('genericErr',5)))
_Hm2ExtNvmStatus_Type.__name__=_C
_Hm2ExtNvmStatus_Object=MibTableColumn
hm2ExtNvmStatus=_Hm2ExtNvmStatus_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,2),_Hm2ExtNvmStatus_Type())
hm2ExtNvmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ExtNvmStatus.setStatus(_A)
_Hm2ExtNvmManufacturerId_Type=DisplayString
_Hm2ExtNvmManufacturerId_Object=MibTableColumn
hm2ExtNvmManufacturerId=_Hm2ExtNvmManufacturerId_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,3),_Hm2ExtNvmManufacturerId_Type())
hm2ExtNvmManufacturerId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ExtNvmManufacturerId.setStatus(_A)
_Hm2ExtNvmHWRevision_Type=DisplayString
_Hm2ExtNvmHWRevision_Object=MibTableColumn
hm2ExtNvmHWRevision=_Hm2ExtNvmHWRevision_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,4),_Hm2ExtNvmHWRevision_Type())
hm2ExtNvmHWRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ExtNvmHWRevision.setStatus(_A)
_Hm2ExtNvmProductName_Type=DisplayString
_Hm2ExtNvmProductName_Object=MibTableColumn
hm2ExtNvmProductName=_Hm2ExtNvmProductName_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,5),_Hm2ExtNvmProductName_Type())
hm2ExtNvmProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ExtNvmProductName.setStatus(_A)
_Hm2ExtNvmVersion_Type=DisplayString
_Hm2ExtNvmVersion_Object=MibTableColumn
hm2ExtNvmVersion=_Hm2ExtNvmVersion_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,6),_Hm2ExtNvmVersion_Type())
hm2ExtNvmVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ExtNvmVersion.setStatus(_A)
_Hm2ExtNvmSerialNum_Type=DisplayString
_Hm2ExtNvmSerialNum_Object=MibTableColumn
hm2ExtNvmSerialNum=_Hm2ExtNvmSerialNum_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,7),_Hm2ExtNvmSerialNum_Type())
hm2ExtNvmSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ExtNvmSerialNum.setStatus(_A)
class _Hm2ExtNvmAutomaticSoftwareLoad_Type(HmEnabledStatus):defaultValue=1
_Hm2ExtNvmAutomaticSoftwareLoad_Type.__name__=_G
_Hm2ExtNvmAutomaticSoftwareLoad_Object=MibTableColumn
hm2ExtNvmAutomaticSoftwareLoad=_Hm2ExtNvmAutomaticSoftwareLoad_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,8),_Hm2ExtNvmAutomaticSoftwareLoad_Type())
hm2ExtNvmAutomaticSoftwareLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ExtNvmAutomaticSoftwareLoad.setStatus(_A)
class _Hm2ExtNvmConfigLoadPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disable',0),('first',1),('second',2),('third',3)))
_Hm2ExtNvmConfigLoadPriority_Type.__name__=_C
_Hm2ExtNvmConfigLoadPriority_Object=MibTableColumn
hm2ExtNvmConfigLoadPriority=_Hm2ExtNvmConfigLoadPriority_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,9),_Hm2ExtNvmConfigLoadPriority_Type())
hm2ExtNvmConfigLoadPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ExtNvmConfigLoadPriority.setStatus(_A)
class _Hm2ExtNvmConfigSave_Type(HmEnabledStatus):defaultValue=1
_Hm2ExtNvmConfigSave_Type.__name__=_G
_Hm2ExtNvmConfigSave_Object=MibTableColumn
hm2ExtNvmConfigSave=_Hm2ExtNvmConfigSave_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,10),_Hm2ExtNvmConfigSave_Type())
hm2ExtNvmConfigSave.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ExtNvmConfigSave.setStatus(_A)
_Hm2ExtNvmWritable_Type=HmEnabledStatus
_Hm2ExtNvmWritable_Object=MibTableColumn
hm2ExtNvmWritable=_Hm2ExtNvmWritable_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,11),_Hm2ExtNvmWritable_Type())
hm2ExtNvmWritable.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ExtNvmWritable.setStatus(_A)
class _Hm2ExtNvmAutomaticSshKeyLoad_Type(HmEnabledStatus):defaultValue=1
_Hm2ExtNvmAutomaticSshKeyLoad_Type.__name__=_G
_Hm2ExtNvmAutomaticSshKeyLoad_Object=MibTableColumn
hm2ExtNvmAutomaticSshKeyLoad=_Hm2ExtNvmAutomaticSshKeyLoad_Object((1,3,6,1,4,1,248,11,10,1,8,2,1,12),_Hm2ExtNvmAutomaticSshKeyLoad_Type())
hm2ExtNvmAutomaticSshKeyLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ExtNvmAutomaticSshKeyLoad.setStatus(_A)
_Hm2AutoDisableGroup_ObjectIdentity=ObjectIdentity
hm2AutoDisableGroup=_Hm2AutoDisableGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,9))
_Hm2AutoDisableIntfTable_Object=MibTable
hm2AutoDisableIntfTable=_Hm2AutoDisableIntfTable_Object((1,3,6,1,4,1,248,11,10,1,9,1))
if mibBuilder.loadTexts:hm2AutoDisableIntfTable.setStatus(_A)
_Hm2AutoDisableIntfEntry_Object=MibTableRow
hm2AutoDisableIntfEntry=_Hm2AutoDisableIntfEntry_Object((1,3,6,1,4,1,248,11,10,1,9,1,1))
hm2AutoDisableIntfEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hm2AutoDisableIntfEntry.setStatus(_A)
class _Hm2AutoDisableIntfRemainingTime_Type(Unsigned32):defaultValue=0
_Hm2AutoDisableIntfRemainingTime_Type.__name__=_K
_Hm2AutoDisableIntfRemainingTime_Object=MibTableColumn
hm2AutoDisableIntfRemainingTime=_Hm2AutoDisableIntfRemainingTime_Object((1,3,6,1,4,1,248,11,10,1,9,1,1,1),_Hm2AutoDisableIntfRemainingTime_Type())
hm2AutoDisableIntfRemainingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AutoDisableIntfRemainingTime.setStatus(_A)
_Hm2AutoDisableIntfComponentName_Type=SnmpAdminString
_Hm2AutoDisableIntfComponentName_Object=MibTableColumn
hm2AutoDisableIntfComponentName=_Hm2AutoDisableIntfComponentName_Object((1,3,6,1,4,1,248,11,10,1,9,1,1,2),_Hm2AutoDisableIntfComponentName_Type())
hm2AutoDisableIntfComponentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AutoDisableIntfComponentName.setStatus(_A)
class _Hm2AutoDisableIntfErrorReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_Q,0),(_k,1),(_l,2),(_m,3),(_n,4),(_o,5),(_p,6),(_q,7),(_r,8),(_s,9),(_t,10)))
_Hm2AutoDisableIntfErrorReason_Type.__name__=_C
_Hm2AutoDisableIntfErrorReason_Object=MibTableColumn
hm2AutoDisableIntfErrorReason=_Hm2AutoDisableIntfErrorReason_Object((1,3,6,1,4,1,248,11,10,1,9,1,1,3),_Hm2AutoDisableIntfErrorReason_Type())
hm2AutoDisableIntfErrorReason.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AutoDisableIntfErrorReason.setStatus(_A)
class _Hm2AutoDisableIntfTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(30,4294967295))
_Hm2AutoDisableIntfTimer_Type.__name__=_K
_Hm2AutoDisableIntfTimer_Object=MibTableColumn
hm2AutoDisableIntfTimer=_Hm2AutoDisableIntfTimer_Object((1,3,6,1,4,1,248,11,10,1,9,1,1,4),_Hm2AutoDisableIntfTimer_Type())
hm2AutoDisableIntfTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AutoDisableIntfTimer.setStatus(_A)
class _Hm2AutoDisableIntfReset_Type(TruthValue):defaultValue=2
_Hm2AutoDisableIntfReset_Type.__name__=_U
_Hm2AutoDisableIntfReset_Object=MibTableColumn
hm2AutoDisableIntfReset=_Hm2AutoDisableIntfReset_Object((1,3,6,1,4,1,248,11,10,1,9,1,1,5),_Hm2AutoDisableIntfReset_Type())
hm2AutoDisableIntfReset.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AutoDisableIntfReset.setStatus(_A)
class _Hm2AutoDisableIntfOperState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_Hm2AutoDisableIntfOperState_Type.__name__=_C
_Hm2AutoDisableIntfOperState_Object=MibTableColumn
hm2AutoDisableIntfOperState=_Hm2AutoDisableIntfOperState_Object((1,3,6,1,4,1,248,11,10,1,9,1,1,6),_Hm2AutoDisableIntfOperState_Type())
hm2AutoDisableIntfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AutoDisableIntfOperState.setStatus(_A)
_Hm2AutoDisableIntfErrorTime_Type=HmTimeSeconds1970
_Hm2AutoDisableIntfErrorTime_Object=MibTableColumn
hm2AutoDisableIntfErrorTime=_Hm2AutoDisableIntfErrorTime_Object((1,3,6,1,4,1,248,11,10,1,9,1,1,7),_Hm2AutoDisableIntfErrorTime_Type())
hm2AutoDisableIntfErrorTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AutoDisableIntfErrorTime.setStatus(_A)
_Hm2AutoDisableReasonTable_Object=MibTable
hm2AutoDisableReasonTable=_Hm2AutoDisableReasonTable_Object((1,3,6,1,4,1,248,11,10,1,9,2))
if mibBuilder.loadTexts:hm2AutoDisableReasonTable.setStatus(_A)
_Hm2AutoDisableReasonEntry_Object=MibTableRow
hm2AutoDisableReasonEntry=_Hm2AutoDisableReasonEntry_Object((1,3,6,1,4,1,248,11,10,1,9,2,1))
hm2AutoDisableReasonEntry.setIndexNames((0,_E,_u))
if mibBuilder.loadTexts:hm2AutoDisableReasonEntry.setStatus(_A)
class _Hm2AutoDisableReasons_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3),(_n,4),(_o,5),(_p,6),(_q,7),(_r,8),(_s,9),(_t,10)))
_Hm2AutoDisableReasons_Type.__name__=_C
_Hm2AutoDisableReasons_Object=MibTableColumn
hm2AutoDisableReasons=_Hm2AutoDisableReasons_Object((1,3,6,1,4,1,248,11,10,1,9,2,1,1),_Hm2AutoDisableReasons_Type())
hm2AutoDisableReasons.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AutoDisableReasons.setStatus(_A)
class _Hm2AutoDisableReasonOperation_Type(HmEnabledStatus):defaultValue=2
_Hm2AutoDisableReasonOperation_Type.__name__=_G
_Hm2AutoDisableReasonOperation_Object=MibTableColumn
hm2AutoDisableReasonOperation=_Hm2AutoDisableReasonOperation_Object((1,3,6,1,4,1,248,11,10,1,9,2,1,2),_Hm2AutoDisableReasonOperation_Type())
hm2AutoDisableReasonOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2AutoDisableReasonOperation.setStatus(_A)
class _Hm2AutoDisableReasonCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('port-monitor',2),('network-security',3),('l2-redundancy',4)))
_Hm2AutoDisableReasonCategory_Type.__name__=_C
_Hm2AutoDisableReasonCategory_Object=MibTableColumn
hm2AutoDisableReasonCategory=_Hm2AutoDisableReasonCategory_Object((1,3,6,1,4,1,248,11,10,1,9,2,1,3),_Hm2AutoDisableReasonCategory_Type())
hm2AutoDisableReasonCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AutoDisableReasonCategory.setStatus(_A)
_Hm2UnitGroup_ObjectIdentity=ObjectIdentity
hm2UnitGroup=_Hm2UnitGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,10))
_Hm2UnitTable_Object=MibTable
hm2UnitTable=_Hm2UnitTable_Object((1,3,6,1,4,1,248,11,10,1,10,100))
if mibBuilder.loadTexts:hm2UnitTable.setStatus(_A)
_Hm2UnitEntry_Object=MibTableRow
hm2UnitEntry=_Hm2UnitEntry_Object((1,3,6,1,4,1,248,11,10,1,10,100,1))
hm2UnitEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hm2UnitEntry.setStatus(_A)
_Hm2UnitIndex_Type=Integer32
_Hm2UnitIndex_Object=MibTableColumn
hm2UnitIndex=_Hm2UnitIndex_Object((1,3,6,1,4,1,248,11,10,1,10,100,1,1),_Hm2UnitIndex_Type())
hm2UnitIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:hm2UnitIndex.setStatus(_A)
_Hm2UnitMaxModuleCapacity_Type=Integer32
_Hm2UnitMaxModuleCapacity_Object=MibTableColumn
hm2UnitMaxModuleCapacity=_Hm2UnitMaxModuleCapacity_Object((1,3,6,1,4,1,248,11,10,1,10,100,1,2),_Hm2UnitMaxModuleCapacity_Type())
hm2UnitMaxModuleCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2UnitMaxModuleCapacity.setStatus(_A)
_Hm2UnitMaxModulePortCapacity_Type=Integer32
_Hm2UnitMaxModulePortCapacity_Object=MibTableColumn
hm2UnitMaxModulePortCapacity=_Hm2UnitMaxModulePortCapacity_Object((1,3,6,1,4,1,248,11,10,1,10,100,1,3),_Hm2UnitMaxModulePortCapacity_Type())
hm2UnitMaxModulePortCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2UnitMaxModulePortCapacity.setStatus(_A)
_Hm2ModuleGroup_ObjectIdentity=ObjectIdentity
hm2ModuleGroup=_Hm2ModuleGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,11))
_Hm2ModuleTable_Object=MibTable
hm2ModuleTable=_Hm2ModuleTable_Object((1,3,6,1,4,1,248,11,10,1,11,100))
if mibBuilder.loadTexts:hm2ModuleTable.setStatus(_A)
_Hm2ModuleEntry_Object=MibTableRow
hm2ModuleEntry=_Hm2ModuleEntry_Object((1,3,6,1,4,1,248,11,10,1,11,100,1))
hm2ModuleEntry.setIndexNames((0,_E,_L),(0,_E,_O))
if mibBuilder.loadTexts:hm2ModuleEntry.setStatus(_A)
_Hm2ModuleIndex_Type=Integer32
_Hm2ModuleIndex_Object=MibTableColumn
hm2ModuleIndex=_Hm2ModuleIndex_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,1),_Hm2ModuleIndex_Type())
hm2ModuleIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:hm2ModuleIndex.setStatus(_A)
_Hm2ModuleId_Type=ObjectIdentifier
_Hm2ModuleId_Object=MibTableColumn
hm2ModuleId=_Hm2ModuleId_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,2),_Hm2ModuleId_Type())
hm2ModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ModuleId.setStatus(_A)
_Hm2ModuleDescription_Type=SnmpAdminString
_Hm2ModuleDescription_Object=MibTableColumn
hm2ModuleDescription=_Hm2ModuleDescription_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,3),_Hm2ModuleDescription_Type())
hm2ModuleDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ModuleDescription.setStatus(_A)
_Hm2ModuleProductCode_Type=SnmpAdminString
_Hm2ModuleProductCode_Object=MibTableColumn
hm2ModuleProductCode=_Hm2ModuleProductCode_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,4),_Hm2ModuleProductCode_Type())
hm2ModuleProductCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ModuleProductCode.setStatus(_A)
_Hm2ModuleVersion_Type=SnmpAdminString
_Hm2ModuleVersion_Object=MibTableColumn
hm2ModuleVersion=_Hm2ModuleVersion_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,5),_Hm2ModuleVersion_Type())
hm2ModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ModuleVersion.setStatus(_A)
_Hm2ModuleNumOfPorts_Type=Integer32
_Hm2ModuleNumOfPorts_Object=MibTableColumn
hm2ModuleNumOfPorts=_Hm2ModuleNumOfPorts_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,6),_Hm2ModuleNumOfPorts_Type())
hm2ModuleNumOfPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ModuleNumOfPorts.setStatus(_A)
_Hm2ModuleFirstMauIndex_Type=Integer32
_Hm2ModuleFirstMauIndex_Object=MibTableColumn
hm2ModuleFirstMauIndex=_Hm2ModuleFirstMauIndex_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,7),_Hm2ModuleFirstMauIndex_Type())
hm2ModuleFirstMauIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ModuleFirstMauIndex.setStatus(_v)
class _Hm2ModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('physical',1),('configurable',2),('remove',3),('fix',4)))
_Hm2ModuleStatus_Type.__name__=_C
_Hm2ModuleStatus_Object=MibTableColumn
hm2ModuleStatus=_Hm2ModuleStatus_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,8),_Hm2ModuleStatus_Type())
hm2ModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ModuleStatus.setStatus(_A)
_Hm2ModuleSerialNum_Type=SnmpAdminString
_Hm2ModuleSerialNum_Object=MibTableColumn
hm2ModuleSerialNum=_Hm2ModuleSerialNum_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,9),_Hm2ModuleSerialNum_Type())
hm2ModuleSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ModuleSerialNum.setStatus(_A)
_Hm2ModuleMinSWVersion_Type=Integer32
_Hm2ModuleMinSWVersion_Object=MibTableColumn
hm2ModuleMinSWVersion=_Hm2ModuleMinSWVersion_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,10),_Hm2ModuleMinSWVersion_Type())
hm2ModuleMinSWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ModuleMinSWVersion.setStatus(_A)
class _Hm2ModuleCapability_Type(Bits):namedValues=NamedValues(*(('poe',0),('fpga',1),('ptp',2),('io-module',3)))
_Hm2ModuleCapability_Type.__name__=_M
_Hm2ModuleCapability_Object=MibTableColumn
hm2ModuleCapability=_Hm2ModuleCapability_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,11),_Hm2ModuleCapability_Type())
hm2ModuleCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ModuleCapability.setStatus(_A)
class _Hm2ModuleInternalID_Type(Integer32):defaultValue=0
_Hm2ModuleInternalID_Type.__name__=_C
_Hm2ModuleInternalID_Object=MibTableColumn
hm2ModuleInternalID=_Hm2ModuleInternalID_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,12),_Hm2ModuleInternalID_Type())
hm2ModuleInternalID.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ModuleInternalID.setStatus(_A)
class _Hm2ModuleInternalIDVariant_Type(Integer32):defaultValue=0
_Hm2ModuleInternalIDVariant_Type.__name__=_C
_Hm2ModuleInternalIDVariant_Object=MibTableColumn
hm2ModuleInternalIDVariant=_Hm2ModuleInternalIDVariant_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,13),_Hm2ModuleInternalIDVariant_Type())
hm2ModuleInternalIDVariant.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ModuleInternalIDVariant.setStatus(_v)
_Hm2ModuleFirstIfIndex_Type=Integer32
_Hm2ModuleFirstIfIndex_Object=MibTableColumn
hm2ModuleFirstIfIndex=_Hm2ModuleFirstIfIndex_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,14),_Hm2ModuleFirstIfIndex_Type())
hm2ModuleFirstIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ModuleFirstIfIndex.setStatus(_A)
class _Hm2ModuleAdminState_Type(HmEnabledStatus):defaultValue=1
_Hm2ModuleAdminState_Type.__name__=_G
_Hm2ModuleAdminState_Object=MibTableColumn
hm2ModuleAdminState=_Hm2ModuleAdminState_Object((1,3,6,1,4,1,248,11,10,1,11,100,1,15),_Hm2ModuleAdminState_Type())
hm2ModuleAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ModuleAdminState.setStatus(_A)
_Hm2DeviceMgmtHumidityGroup_ObjectIdentity=ObjectIdentity
hm2DeviceMgmtHumidityGroup=_Hm2DeviceMgmtHumidityGroup_ObjectIdentity((1,3,6,1,4,1,248,11,10,1,12))
class _Hm2DevMgmtHumidity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2DevMgmtHumidity_Type.__name__=_K
_Hm2DevMgmtHumidity_Object=MibScalar
hm2DevMgmtHumidity=_Hm2DevMgmtHumidity_Object((1,3,6,1,4,1,248,11,10,1,12,1),_Hm2DevMgmtHumidity_Type())
hm2DevMgmtHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMgmtHumidity.setStatus(_A)
if mibBuilder.loadTexts:hm2DevMgmtHumidity.setUnits(_T)
class _Hm2DevMgmtHumidityUpperLimit_Type(Unsigned32):defaultValue=95;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2DevMgmtHumidityUpperLimit_Type.__name__=_K
_Hm2DevMgmtHumidityUpperLimit_Object=MibScalar
hm2DevMgmtHumidityUpperLimit=_Hm2DevMgmtHumidityUpperLimit_Object((1,3,6,1,4,1,248,11,10,1,12,2),_Hm2DevMgmtHumidityUpperLimit_Type())
hm2DevMgmtHumidityUpperLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtHumidityUpperLimit.setStatus(_A)
if mibBuilder.loadTexts:hm2DevMgmtHumidityUpperLimit.setUnits(_T)
class _Hm2DevMgmtHumidityLowerLimit_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2DevMgmtHumidityLowerLimit_Type.__name__=_K
_Hm2DevMgmtHumidityLowerLimit_Object=MibScalar
hm2DevMgmtHumidityLowerLimit=_Hm2DevMgmtHumidityLowerLimit_Object((1,3,6,1,4,1,248,11,10,1,12,3),_Hm2DevMgmtHumidityLowerLimit_Type())
hm2DevMgmtHumidityLowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2DevMgmtHumidityLowerLimit.setStatus(_A)
if mibBuilder.loadTexts:hm2DevMgmtHumidityLowerLimit.setUnits(_T)
hm2SfpChangeTrap=NotificationType((1,3,6,1,4,1,248,11,10,0,1))
hm2SfpChangeTrap.setObjects((_I,_J))
if mibBuilder.loadTexts:hm2SfpChangeTrap.setStatus(_A)
hm2AutoDisablePortTrap=NotificationType((1,3,6,1,4,1,248,11,10,0,2))
hm2AutoDisablePortTrap.setObjects(*((_I,_J),(_E,_w),(_E,_x)))
if mibBuilder.loadTexts:hm2AutoDisablePortTrap.setStatus(_A)
hm2ModulePluggedTrap=NotificationType((1,3,6,1,4,1,248,11,10,0,3))
hm2ModulePluggedTrap.setObjects(*((_E,_L),(_E,_O)))
if mibBuilder.loadTexts:hm2ModulePluggedTrap.setStatus(_A)
hm2ModuleRemovedTrap=NotificationType((1,3,6,1,4,1,248,11,10,0,4))
hm2ModuleRemovedTrap.setObjects(*((_E,_L),(_E,_O)))
if mibBuilder.loadTexts:hm2ModuleRemovedTrap.setStatus(_A)
hm2SFPRxPowerChangeTrap=NotificationType((1,3,6,1,4,1,248,11,10,0,5))
hm2SFPRxPowerChangeTrap.setObjects((_E,_y))
if mibBuilder.loadTexts:hm2SFPRxPowerChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_S:Hm2DeviceExtNVMType,'hm2DeviceMgmtMib':hm2DeviceMgmtMib,'hm2DeviceMgmtMibNotifications':hm2DeviceMgmtMibNotifications,'hm2SfpChangeTrap':hm2SfpChangeTrap,'hm2AutoDisablePortTrap':hm2AutoDisablePortTrap,'hm2ModulePluggedTrap':hm2ModulePluggedTrap,'hm2ModuleRemovedTrap':hm2ModuleRemovedTrap,'hm2SFPRxPowerChangeTrap':hm2SFPRxPowerChangeTrap,'hm2DeviceMgmtMibObjects':hm2DeviceMgmtMibObjects,'hm2DeviceMgmtGroup':hm2DeviceMgmtGroup,'hm2DevMgmtProductId':hm2DevMgmtProductId,'hm2DevMgmtProductDescr':hm2DevMgmtProductDescr,'hm2DevMgmtSerialNumber':hm2DevMgmtSerialNumber,'hm2DeviceMgmtActionGroup':hm2DeviceMgmtActionGroup,'hm2DevMgmtActionReset':hm2DevMgmtActionReset,'hm2DevMgmtActionFlushFDB':hm2DevMgmtActionFlushFDB,'hm2DevMgmtActionFlushARP':hm2DevMgmtActionFlushARP,'hm2DevMgmtActionFlushIGS':hm2DevMgmtActionFlushIGS,'hm2DevMgmtActionFlushPortStats':hm2DevMgmtActionFlushPortStats,'hm2DevMgmtActionFlushEmailLogStats':hm2DevMgmtActionFlushEmailLogStats,'hm2DevMgmtActionFlushMMRP':hm2DevMgmtActionFlushMMRP,'hm2DevMgmtActionFlushMVRP':hm2DevMgmtActionFlushMVRP,'hm2DevMgmtActionFlushMSRP':hm2DevMgmtActionFlushMSRP,'hm2DevMgmtActionFlushIeee8021AS':hm2DevMgmtActionFlushIeee8021AS,'hm2DevMgmtActionFlushDnsClientCache':hm2DevMgmtActionFlushDnsClientCache,'hm2DevMgmtActionFlushDnsCachingServerCache':hm2DevMgmtActionFlushDnsCachingServerCache,'hm2DevMgmtActionFlushIpUdpHelperStats':hm2DevMgmtActionFlushIpUdpHelperStats,'hm2DevMgmtActionFlushAclStats':hm2DevMgmtActionFlushAclStats,'hm2DevMgmtActionFlushLdapUserCache':hm2DevMgmtActionFlushLdapUserCache,'hm2DevMgmtActionFlushMgmtAccessStatistics':hm2DevMgmtActionFlushMgmtAccessStatistics,'hm2DevMgmtActionFlushDiffServ':hm2DevMgmtActionFlushDiffServ,'hm2DevMgmtActionDelayPreset':hm2DevMgmtActionDelayPreset,'hm2DevMgmtActionDelayCurrent':hm2DevMgmtActionDelayCurrent,'hm2DevMgmtActionLanBypass':hm2DevMgmtActionLanBypass,'hm2DevMgmtActionSystemoffLanBypass':hm2DevMgmtActionSystemoffLanBypass,'hm2DeviceMgmtSoftwareGroup':hm2DeviceMgmtSoftwareGroup,'hm2DeviceMgmtSoftwareVersionGroup':hm2DeviceMgmtSoftwareVersionGroup,'hm2DevMgmtSwVersBootcode':hm2DevMgmtSwVersBootcode,'hm2DevMgmtSwVersAllowUnsigned':hm2DevMgmtSwVersAllowUnsigned,'hm2DevMgmtSwVersCertTable':hm2DevMgmtSwVersCertTable,'hm2DevMgmtSwVersCertEntry':hm2DevMgmtSwVersCertEntry,_V:hm2DevMgmtSwVersCertIndex,'hm2DevMgmtSwVersCertSerialNo':hm2DevMgmtSwVersCertSerialNo,'hm2DevMgmtSwVersCertSubject':hm2DevMgmtSwVersCertSubject,'hm2DevMgmtSwVersCertSigAlg':hm2DevMgmtSwVersCertSigAlg,'hm2DevMgmtSwVersCertType':hm2DevMgmtSwVersCertType,'hm2DevMgmtSwVersCertStatus':hm2DevMgmtSwVersCertStatus,'hm2DevMgmtSwVersCertFingerprint':hm2DevMgmtSwVersCertFingerprint,'hm2DevMgmtSwVersTable':hm2DevMgmtSwVersTable,'hm2DevMgmtSwVersEntry':hm2DevMgmtSwVersEntry,_W:hm2DevMgmtSwFileLocation,_X:hm2DevMgmtSwFileType,_Y:hm2DevMgmtSwFileIdx,'hm2DevMgmtSwFileName':hm2DevMgmtSwFileName,'hm2DevMgmtSwVersion':hm2DevMgmtSwVersion,'hm2DevMgmtSwMajorRelNum':hm2DevMgmtSwMajorRelNum,'hm2DevMgmtSwMinorRelNum':hm2DevMgmtSwMinorRelNum,'hm2DevMgmtSwBugfixRelNum':hm2DevMgmtSwBugfixRelNum,'hm2DeviceMgmtHardwareGroup':hm2DeviceMgmtHardwareGroup,'hm2DevMgmtHwVersion':hm2DevMgmtHwVersion,'hm2DevMgmtSwitchingCoreVersion':hm2DevMgmtSwitchingCoreVersion,'hm2DeviceMgmtLogicVersionGroup':hm2DeviceMgmtLogicVersionGroup,'hm2DevMgmtLogicVersTable':hm2DevMgmtLogicVersTable,'hm2DevMgmtLogicVersEntry':hm2DevMgmtLogicVersEntry,_Z:hm2DevMgmtLogicIdx,'hm2DevMgmtLogicAddress':hm2DevMgmtLogicAddress,'hm2DevMgmtLogicVersion':hm2DevMgmtLogicVersion,'hm2DeviceMgmtTemperatureGroup':hm2DeviceMgmtTemperatureGroup,'hm2DevMgmtTemperature':hm2DevMgmtTemperature,'hm2DevMgmtTemperatureUpperLimit':hm2DevMgmtTemperatureUpperLimit,'hm2DevMgmtTemperatureLowerLimit':hm2DevMgmtTemperatureLowerLimit,'hm2DevMgmtTemperatureExtTable':hm2DevMgmtTemperatureExtTable,'hm2DevMgmtTemperatureExtEntry':hm2DevMgmtTemperatureExtEntry,_a:hm2DevMgmtTemperatureExtType,_b:hm2DevMgmtTemperatureExtSensorId,'hm2DevMgmtTemperatureExt':hm2DevMgmtTemperatureExt,'hm2DevMgmtTemperatureExtUpperLimit':hm2DevMgmtTemperatureExtUpperLimit,'hm2DevMgmtTemperatureExtLowerLimit':hm2DevMgmtTemperatureExtLowerLimit,'hm2IfaceGroup':hm2IfaceGroup,'hm2IfaceTable':hm2IfaceTable,'hm2IfaceEntry':hm2IfaceEntry,_c:hm2IfacePhysIndex,'hm2IfacePortCapabilityBits':hm2IfacePortCapabilityBits,'hm2IfaceCableCrossing':hm2IfaceCableCrossing,'hm2IfacePowerState':hm2IfacePowerState,'hm2IfaceAutoPowerDown':hm2IfaceAutoPowerDown,_w:hm2IfaceOperAdminStatus,'hm2IfaceLayoutTable':hm2IfaceLayoutTable,'hm2IfaceLayoutEntry':hm2IfaceLayoutEntry,_g:hm2IfaceLayoutIndex,'hm2IfaceLayoutStartIfIndex':hm2IfaceLayoutStartIfIndex,'hm2IfaceLayoutEndIfIndex':hm2IfaceLayoutEndIfIndex,'hm2IfaceLayoutModuleCapacity':hm2IfaceLayoutModuleCapacity,'hm2IfaceLayoutModulePortCapacity':hm2IfaceLayoutModulePortCapacity,'hm2IfaceLayoutFormat':hm2IfaceLayoutFormat,'hm2IfaceLayoutIfIndexType':hm2IfaceLayoutIfIndexType,'hm2IfaceExtTable':hm2IfaceExtTable,'hm2IfaceExtEntry':hm2IfaceExtEntry,'hm2IfaceExtIfRole':hm2IfaceExtIfRole,'hm2SfpGroup':hm2SfpGroup,'hm2SfpInfoTable':hm2SfpInfoTable,'hm2SfpInfoEntry':hm2SfpInfoEntry,'hm2SfpModuleType':hm2SfpModuleType,'hm2SfpMediaType':hm2SfpMediaType,'hm2SfpConnector':hm2SfpConnector,'hm2SfpVendorName':hm2SfpVendorName,'hm2SfpVendorOUI':hm2SfpVendorOUI,'hm2SfpPartNumber':hm2SfpPartNumber,'hm2SfpPartRev':hm2SfpPartRev,'hm2SfpSerialNum':hm2SfpSerialNum,'hm2SfpDateCode':hm2SfpDateCode,'hm2SfpInfoVersion':hm2SfpInfoVersion,'hm2SfpInfoPartNumber':hm2SfpInfoPartNumber,'hm2SfpInfoPartId':hm2SfpInfoPartId,'hm2SfpBitRateNominal':hm2SfpBitRateNominal,'hm2SfpBitRateMin':hm2SfpBitRateMin,'hm2SfpBitRateMax':hm2SfpBitRateMax,'hm2SfpMaxLength-fiber-9':hm2SfpMaxLength_fiber_9,'hm2SfpMaxLength-fiber-50':hm2SfpMaxLength_fiber_50,'hm2SfpMaxLength-fiber-e50':hm2SfpMaxLength_fiber_e50,'hm2SfpMaxLength-fiber-62-5':hm2SfpMaxLength_fiber_62_5,'hm2SfpMaxLength-copper':hm2SfpMaxLength_copper,'hm2SfpWaveLength':hm2SfpWaveLength,'hm2SfpWaveLengthTolerance':hm2SfpWaveLengthTolerance,'hm2SfpEnhancedOptions':hm2SfpEnhancedOptions,'hm2SfpSupported':hm2SfpSupported,'hm2SfpSupportedReason':hm2SfpSupportedReason,'hm2SfpDiagTable':hm2SfpDiagTable,'hm2SfpDiagEntry':hm2SfpDiagEntry,'hm2SfpCurrentBitRate':hm2SfpCurrentBitRate,'hm2SfpCurrentTemperature':hm2SfpCurrentTemperature,'hm2SfpCurrentTxPower':hm2SfpCurrentTxPower,'hm2SfpCurrentRxPower':hm2SfpCurrentRxPower,'hm2SfpCurrentTxPowerdBm':hm2SfpCurrentTxPowerdBm,'hm2SfpCurrentRxPowerdBm':hm2SfpCurrentRxPowerdBm,_y:hm2SfpCurrentRxPowerState,'hm2SfpWLGroup':hm2SfpWLGroup,'hm2SfpWLStatus':hm2SfpWLStatus,'hm2SfpThresholdTable':hm2SfpThresholdTable,'hm2SfpThresholdEntry':hm2SfpThresholdEntry,'hm2SfpTemperatureHighAlarm':hm2SfpTemperatureHighAlarm,'hm2SfpTemperatureHighWarning':hm2SfpTemperatureHighWarning,'hm2SfpTemperatureLowAlarm':hm2SfpTemperatureLowAlarm,'hm2SfpTemperatureLowWarning':hm2SfpTemperatureLowWarning,'hm2SfpTxPowerHighAlarm':hm2SfpTxPowerHighAlarm,'hm2SfpTxPowerHighWarning':hm2SfpTxPowerHighWarning,'hm2SfpTxPowerLowAlarm':hm2SfpTxPowerLowAlarm,'hm2SfpTxPowerLowWarning':hm2SfpTxPowerLowWarning,'hm2SfpRxPowerHighAlarm':hm2SfpRxPowerHighAlarm,'hm2SfpRxPowerHighWarning':hm2SfpRxPowerHighWarning,'hm2SfpRxPowerLowAlarm':hm2SfpRxPowerLowAlarm,'hm2SfpRxPowerLowWarning':hm2SfpRxPowerLowWarning,'hm2SfpTxPowerdBmHighAlarm':hm2SfpTxPowerdBmHighAlarm,'hm2SfpTxPowerdBmHighWarning':hm2SfpTxPowerdBmHighWarning,'hm2SfpTxPowerdBmLowAlarm':hm2SfpTxPowerdBmLowAlarm,'hm2SfpTxPowerdBmLowWarning':hm2SfpTxPowerdBmLowWarning,'hm2SfpRxPowerdBmHighAlarm':hm2SfpRxPowerdBmHighAlarm,'hm2SfpRxPowerdBmHighWarning':hm2SfpRxPowerdBmHighWarning,'hm2SfpRxPowerdBmLowAlarm':hm2SfpRxPowerdBmLowAlarm,'hm2SfpRxPowerdBmLowWarning':hm2SfpRxPowerdBmLowWarning,'hm2ExtNvmGroup':hm2ExtNvmGroup,'hm2ExtNvmGeneralGroup':hm2ExtNvmGeneralGroup,'hm2ExtNvmChooseActive':hm2ExtNvmChooseActive,'hm2ExtNvmLogDevice':hm2ExtNvmLogDevice,'hm2ExtNvmAdminMode':hm2ExtNvmAdminMode,'hm2ExtNvmOperMode':hm2ExtNvmOperMode,'hm2ExtNvmTable':hm2ExtNvmTable,'hm2ExtNvmEntry':hm2ExtNvmEntry,_j:hm2ExtNvmTableIndex,'hm2ExtNvmStatus':hm2ExtNvmStatus,'hm2ExtNvmManufacturerId':hm2ExtNvmManufacturerId,'hm2ExtNvmHWRevision':hm2ExtNvmHWRevision,'hm2ExtNvmProductName':hm2ExtNvmProductName,'hm2ExtNvmVersion':hm2ExtNvmVersion,'hm2ExtNvmSerialNum':hm2ExtNvmSerialNum,'hm2ExtNvmAutomaticSoftwareLoad':hm2ExtNvmAutomaticSoftwareLoad,'hm2ExtNvmConfigLoadPriority':hm2ExtNvmConfigLoadPriority,'hm2ExtNvmConfigSave':hm2ExtNvmConfigSave,'hm2ExtNvmWritable':hm2ExtNvmWritable,'hm2ExtNvmAutomaticSshKeyLoad':hm2ExtNvmAutomaticSshKeyLoad,'hm2AutoDisableGroup':hm2AutoDisableGroup,'hm2AutoDisableIntfTable':hm2AutoDisableIntfTable,'hm2AutoDisableIntfEntry':hm2AutoDisableIntfEntry,'hm2AutoDisableIntfRemainingTime':hm2AutoDisableIntfRemainingTime,'hm2AutoDisableIntfComponentName':hm2AutoDisableIntfComponentName,_x:hm2AutoDisableIntfErrorReason,'hm2AutoDisableIntfTimer':hm2AutoDisableIntfTimer,'hm2AutoDisableIntfReset':hm2AutoDisableIntfReset,'hm2AutoDisableIntfOperState':hm2AutoDisableIntfOperState,'hm2AutoDisableIntfErrorTime':hm2AutoDisableIntfErrorTime,'hm2AutoDisableReasonTable':hm2AutoDisableReasonTable,'hm2AutoDisableReasonEntry':hm2AutoDisableReasonEntry,_u:hm2AutoDisableReasons,'hm2AutoDisableReasonOperation':hm2AutoDisableReasonOperation,'hm2AutoDisableReasonCategory':hm2AutoDisableReasonCategory,'hm2UnitGroup':hm2UnitGroup,'hm2UnitTable':hm2UnitTable,'hm2UnitEntry':hm2UnitEntry,_L:hm2UnitIndex,'hm2UnitMaxModuleCapacity':hm2UnitMaxModuleCapacity,'hm2UnitMaxModulePortCapacity':hm2UnitMaxModulePortCapacity,'hm2ModuleGroup':hm2ModuleGroup,'hm2ModuleTable':hm2ModuleTable,'hm2ModuleEntry':hm2ModuleEntry,_O:hm2ModuleIndex,'hm2ModuleId':hm2ModuleId,'hm2ModuleDescription':hm2ModuleDescription,'hm2ModuleProductCode':hm2ModuleProductCode,'hm2ModuleVersion':hm2ModuleVersion,'hm2ModuleNumOfPorts':hm2ModuleNumOfPorts,'hm2ModuleFirstMauIndex':hm2ModuleFirstMauIndex,'hm2ModuleStatus':hm2ModuleStatus,'hm2ModuleSerialNum':hm2ModuleSerialNum,'hm2ModuleMinSWVersion':hm2ModuleMinSWVersion,'hm2ModuleCapability':hm2ModuleCapability,'hm2ModuleInternalID':hm2ModuleInternalID,'hm2ModuleInternalIDVariant':hm2ModuleInternalIDVariant,'hm2ModuleFirstIfIndex':hm2ModuleFirstIfIndex,'hm2ModuleAdminState':hm2ModuleAdminState,'hm2DeviceMgmtHumidityGroup':hm2DeviceMgmtHumidityGroup,'hm2DevMgmtHumidity':hm2DevMgmtHumidity,'hm2DevMgmtHumidityUpperLimit':hm2DevMgmtHumidityUpperLimit,'hm2DevMgmtHumidityLowerLimit':hm2DevMgmtHumidityLowerLimit})