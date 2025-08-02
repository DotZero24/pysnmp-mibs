_J='rcPortBindIp'
_I='RAISECOM-IPSOURCEGUARD-MIB'
_H='rcPortIndex'
_G='SWITCH-SYSTEM-MIB'
_F='read-create'
_E='read-only'
_D='read-write'
_C='EnableVar'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
rcPortIndex,=mibBuilder.importSymbols(_G,_H)
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_C)
rcIpSourceGuard=ModuleIdentity((1,3,6,1,4,1,8886,6,1,37))
if mibBuilder.loadTexts:rcIpSourceGuard.setRevisions(('2009-09-09 00:00',))
class _RcIpVerifySource_Type(EnableVar):defaultValue=2
_RcIpVerifySource_Type.__name__=_C
_RcIpVerifySource_Object=MibScalar
rcIpVerifySource=_RcIpVerifySource_Object((1,3,6,1,4,1,8886,6,1,37,1),_RcIpVerifySource_Type())
rcIpVerifySource.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpVerifySource.setStatus(_A)
class _RcIpVerifySourceDhcpsnooping_Type(EnableVar):defaultValue=2
_RcIpVerifySourceDhcpsnooping_Type.__name__=_C
_RcIpVerifySourceDhcpsnooping_Object=MibScalar
rcIpVerifySourceDhcpsnooping=_RcIpVerifySourceDhcpsnooping_Object((1,3,6,1,4,1,8886,6,1,37,2),_RcIpVerifySourceDhcpsnooping_Type())
rcIpVerifySourceDhcpsnooping.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpVerifySourceDhcpsnooping.setStatus(_A)
class _RcIpVerifySourceMaxEntryNum_Type(Integer32):defaultValue=0
_RcIpVerifySourceMaxEntryNum_Type.__name__=_B
_RcIpVerifySourceMaxEntryNum_Object=MibScalar
rcIpVerifySourceMaxEntryNum=_RcIpVerifySourceMaxEntryNum_Object((1,3,6,1,4,1,8886,6,1,37,3),_RcIpVerifySourceMaxEntryNum_Type())
rcIpVerifySourceMaxEntryNum.setMaxAccess(_E)
if mibBuilder.loadTexts:rcIpVerifySourceMaxEntryNum.setStatus(_A)
class _RcIpVerifySourceCurrentEntryNum_Type(Integer32):defaultValue=0
_RcIpVerifySourceCurrentEntryNum_Type.__name__=_B
_RcIpVerifySourceCurrentEntryNum_Object=MibScalar
rcIpVerifySourceCurrentEntryNum=_RcIpVerifySourceCurrentEntryNum_Object((1,3,6,1,4,1,8886,6,1,37,4),_RcIpVerifySourceCurrentEntryNum_Type())
rcIpVerifySourceCurrentEntryNum.setMaxAccess(_E)
if mibBuilder.loadTexts:rcIpVerifySourceCurrentEntryNum.setStatus(_A)
_RcPortTrustTable_Object=MibTable
rcPortTrustTable=_RcPortTrustTable_Object((1,3,6,1,4,1,8886,6,1,37,5))
if mibBuilder.loadTexts:rcPortTrustTable.setStatus(_A)
_RcPortTrustEntry_Object=MibTableRow
rcPortTrustEntry=_RcPortTrustEntry_Object((1,3,6,1,4,1,8886,6,1,37,5,1))
rcPortTrustEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:rcPortTrustEntry.setStatus(_A)
class _RcPortIpVerifySourceTrust_Type(EnableVar):defaultValue=2
_RcPortIpVerifySourceTrust_Type.__name__=_C
_RcPortIpVerifySourceTrust_Object=MibTableColumn
rcPortIpVerifySourceTrust=_RcPortIpVerifySourceTrust_Object((1,3,6,1,4,1,8886,6,1,37,5,1,1),_RcPortIpVerifySourceTrust_Type())
rcPortIpVerifySourceTrust.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortIpVerifySourceTrust.setStatus(_A)
_RcIpSourceGuardTable_Object=MibTable
rcIpSourceGuardTable=_RcIpSourceGuardTable_Object((1,3,6,1,4,1,8886,6,1,37,6))
if mibBuilder.loadTexts:rcIpSourceGuardTable.setStatus(_A)
_RcIpSourceGuardEntry_Object=MibTableRow
rcIpSourceGuardEntry=_RcIpSourceGuardEntry_Object((1,3,6,1,4,1,8886,6,1,37,6,1))
rcIpSourceGuardEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:rcIpSourceGuardEntry.setStatus(_A)
_RcPortBindIp_Type=IpAddress
_RcPortBindIp_Object=MibTableColumn
rcPortBindIp=_RcPortBindIp_Object((1,3,6,1,4,1,8886,6,1,37,6,1,1),_RcPortBindIp_Type())
rcPortBindIp.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcPortBindIp.setStatus(_A)
_RcPortBindPortid_Type=Integer32
_RcPortBindPortid_Object=MibTableColumn
rcPortBindPortid=_RcPortBindPortid_Object((1,3,6,1,4,1,8886,6,1,37,6,1,2),_RcPortBindPortid_Type())
rcPortBindPortid.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPortBindPortid.setStatus(_A)
class _RcPortBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('statis',1),('dynamic',2)))
_RcPortBindType_Type.__name__=_B
_RcPortBindType_Object=MibTableColumn
rcPortBindType=_RcPortBindType_Object((1,3,6,1,4,1,8886,6,1,37,6,1,3),_RcPortBindType_Type())
rcPortBindType.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortBindType.setStatus(_A)
_RcPortBindMac_Type=MacAddress
_RcPortBindMac_Object=MibTableColumn
rcPortBindMac=_RcPortBindMac_Object((1,3,6,1,4,1,8886,6,1,37,6,1,4),_RcPortBindMac_Type())
rcPortBindMac.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPortBindMac.setStatus(_A)
class _RcPortBindVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcPortBindVlan_Type.__name__=_B
_RcPortBindVlan_Object=MibTableColumn
rcPortBindVlan=_RcPortBindVlan_Object((1,3,6,1,4,1,8886,6,1,37,6,1,5),_RcPortBindVlan_Type())
rcPortBindVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPortBindVlan.setStatus(_A)
_RcPortBindHwStatus_Type=EnableVar
_RcPortBindHwStatus_Object=MibTableColumn
rcPortBindHwStatus=_RcPortBindHwStatus_Object((1,3,6,1,4,1,8886,6,1,37,6,1,6),_RcPortBindHwStatus_Type())
rcPortBindHwStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortBindHwStatus.setStatus(_A)
_RcPortBindRowStatus_Type=RowStatus
_RcPortBindRowStatus_Object=MibTableColumn
rcPortBindRowStatus=_RcPortBindRowStatus_Object((1,3,6,1,4,1,8886,6,1,37,6,1,7),_RcPortBindRowStatus_Type())
rcPortBindRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPortBindRowStatus.setStatus(_A)
class _RcIpVerifySourceAutoUpdate_Type(EnableVar):defaultValue=2
_RcIpVerifySourceAutoUpdate_Type.__name__=_C
_RcIpVerifySourceAutoUpdate_Object=MibScalar
rcIpVerifySourceAutoUpdate=_RcIpVerifySourceAutoUpdate_Object((1,3,6,1,4,1,8886,6,1,37,7),_RcIpVerifySourceAutoUpdate_Type())
rcIpVerifySourceAutoUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpVerifySourceAutoUpdate.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'rcIpSourceGuard':rcIpSourceGuard,'rcIpVerifySource':rcIpVerifySource,'rcIpVerifySourceDhcpsnooping':rcIpVerifySourceDhcpsnooping,'rcIpVerifySourceMaxEntryNum':rcIpVerifySourceMaxEntryNum,'rcIpVerifySourceCurrentEntryNum':rcIpVerifySourceCurrentEntryNum,'rcPortTrustTable':rcPortTrustTable,'rcPortTrustEntry':rcPortTrustEntry,'rcPortIpVerifySourceTrust':rcPortIpVerifySourceTrust,'rcIpSourceGuardTable':rcIpSourceGuardTable,'rcIpSourceGuardEntry':rcIpSourceGuardEntry,_J:rcPortBindIp,'rcPortBindPortid':rcPortBindPortid,'rcPortBindType':rcPortBindType,'rcPortBindMac':rcPortBindMac,'rcPortBindVlan':rcPortBindVlan,'rcPortBindHwStatus':rcPortBindHwStatus,'rcPortBindRowStatus':rcPortBindRowStatus,'rcIpVerifySourceAutoUpdate':rcIpVerifySourceAutoUpdate})