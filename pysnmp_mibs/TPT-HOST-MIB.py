_F='hostIpIndex'
_E='TPT-HOST-MIB'
_D='disabled'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_objs,=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-objs')
tpt_host_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,12))
if mibBuilder.loadTexts:tpt_host_objs.setRevisions(('2016-05-25 18:54',))
class EnabledOrNot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('enabled',1)))
class ActiveOrNot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
class IpAddressType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('iptypeIPv4',1),('iptypeIPv6user',2),('iptypeIPv6local',3),('iptypeIPv6auto',4)))
class FipsMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('crypto',1),('full',2)))
class ActiveCert(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('temporary',1),('authorized',2)))
class InitState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('in-progress',0),('complete',1)))
_HostIpTable_Object=MibTable
hostIpTable=_HostIpTable_Object((1,3,6,1,4,1,10734,3,3,2,12,1))
if mibBuilder.loadTexts:hostIpTable.setStatus(_A)
_HostIpEntry_Object=MibTableRow
hostIpEntry=_HostIpEntry_Object((1,3,6,1,4,1,10734,3,3,2,12,1,1))
hostIpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hostIpEntry.setStatus(_A)
_HostIpIndex_Type=Unsigned32
_HostIpIndex_Object=MibTableColumn
hostIpIndex=_HostIpIndex_Object((1,3,6,1,4,1,10734,3,3,2,12,1,1,1),_HostIpIndex_Type())
hostIpIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hostIpIndex.setStatus(_A)
class _HostIpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HostIpAddress_Type.__name__=_C
_HostIpAddress_Object=MibTableColumn
hostIpAddress=_HostIpAddress_Object((1,3,6,1,4,1,10734,3,3,2,12,1,1,2),_HostIpAddress_Type())
hostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIpAddress.setStatus(_A)
_HostIpType_Type=IpAddressType
_HostIpType_Object=MibTableColumn
hostIpType=_HostIpType_Object((1,3,6,1,4,1,10734,3,3,2,12,1,1,3),_HostIpType_Type())
hostIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIpType.setStatus(_A)
_HostIpActive_Type=ActiveOrNot
_HostIpActive_Object=MibTableColumn
hostIpActive=_HostIpActive_Object((1,3,6,1,4,1,10734,3,3,2,12,1,1,4),_HostIpActive_Type())
hostIpActive.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIpActive.setStatus(_A)
class _HostIPv4Gateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HostIPv4Gateway_Type.__name__=_C
_HostIPv4Gateway_Object=MibScalar
hostIPv4Gateway=_HostIPv4Gateway_Object((1,3,6,1,4,1,10734,3,3,2,12,2),_HostIPv4Gateway_Type())
hostIPv4Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIPv4Gateway.setStatus(_A)
class _HostIPv6Gateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HostIPv6Gateway_Type.__name__=_C
_HostIPv6Gateway_Object=MibScalar
hostIPv6Gateway=_HostIPv6Gateway_Object((1,3,6,1,4,1,10734,3,3,2,12,3),_HostIPv6Gateway_Type())
hostIPv6Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIPv6Gateway.setStatus(_A)
_HostIPv6Enabled_Type=EnabledOrNot
_HostIPv6Enabled_Object=MibScalar
hostIPv6Enabled=_HostIPv6Enabled_Object((1,3,6,1,4,1,10734,3,3,2,12,4),_HostIPv6Enabled_Type())
hostIPv6Enabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIPv6Enabled.setStatus(_A)
_HostIPv6AutoConfig_Type=EnabledOrNot
_HostIPv6AutoConfig_Object=MibScalar
hostIPv6AutoConfig=_HostIPv6AutoConfig_Object((1,3,6,1,4,1,10734,3,3,2,12,5),_HostIPv6AutoConfig_Type())
hostIPv6AutoConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIPv6AutoConfig.setStatus(_A)
_HostFipsCfgMode_Type=FipsMode
_HostFipsCfgMode_Object=MibScalar
hostFipsCfgMode=_HostFipsCfgMode_Object((1,3,6,1,4,1,10734,3,3,2,12,6),_HostFipsCfgMode_Type())
hostFipsCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hostFipsCfgMode.setStatus(_A)
_HostFipsMode_Type=FipsMode
_HostFipsMode_Object=MibScalar
hostFipsMode=_HostFipsMode_Object((1,3,6,1,4,1,10734,3,3,2,12,7),_HostFipsMode_Type())
hostFipsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hostFipsMode.setStatus(_A)
_HostSSLCert_Type=ActiveCert
_HostSSLCert_Object=MibScalar
hostSSLCert=_HostSSLCert_Object((1,3,6,1,4,1,10734,3,3,2,12,8),_HostSSLCert_Type())
hostSSLCert.setMaxAccess(_B)
if mibBuilder.loadTexts:hostSSLCert.setStatus(_A)
_HostInitState_Type=InitState
_HostInitState_Object=MibScalar
hostInitState=_HostInitState_Object((1,3,6,1,4,1,10734,3,3,2,12,9),_HostInitState_Type())
hostInitState.setMaxAccess(_B)
if mibBuilder.loadTexts:hostInitState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'EnabledOrNot':EnabledOrNot,'ActiveOrNot':ActiveOrNot,'IpAddressType':IpAddressType,'FipsMode':FipsMode,'ActiveCert':ActiveCert,'InitState':InitState,'tpt-host-objs':tpt_host_objs,'hostIpTable':hostIpTable,'hostIpEntry':hostIpEntry,_F:hostIpIndex,'hostIpAddress':hostIpAddress,'hostIpType':hostIpType,'hostIpActive':hostIpActive,'hostIPv4Gateway':hostIPv4Gateway,'hostIPv6Gateway':hostIPv6Gateway,'hostIPv6Enabled':hostIPv6Enabled,'hostIPv6AutoConfig':hostIPv6AutoConfig,'hostFipsCfgMode':hostFipsCfgMode,'hostFipsMode':hostFipsMode,'hostSSLCert':hostSSLCert,'hostInitState':hostInitState})