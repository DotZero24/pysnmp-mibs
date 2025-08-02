_F='read-write'
_E='read-only'
_D='linkBandwidthControlLinkName'
_C='MX-NTC-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap','MxEnableState','MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,3700))
_NtcMIBObjects_ObjectIdentity=ObjectIdentity
ntcMIBObjects=_NtcMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,3700,1))
_LinkBandwidthControlTable_Object=MibTable
linkBandwidthControlTable=_LinkBandwidthControlTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,3700,1,100))
if mibBuilder.loadTexts:linkBandwidthControlTable.setStatus(_A)
_LinkBandwidthControlEntry_Object=MibTableRow
linkBandwidthControlEntry=_LinkBandwidthControlEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,3700,1,100,1))
linkBandwidthControlEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:linkBandwidthControlEntry.setStatus(_A)
_LinkBandwidthControlLinkName_Type=OctetString
_LinkBandwidthControlLinkName_Object=MibTableColumn
linkBandwidthControlLinkName=_LinkBandwidthControlLinkName_Object((1,3,6,1,4,1,4935,1000,100,200,100,3700,1,100,1,100),_LinkBandwidthControlLinkName_Type())
linkBandwidthControlLinkName.setMaxAccess(_E)
if mibBuilder.loadTexts:linkBandwidthControlLinkName.setStatus(_A)
class _LinkBandwidthControlEgressLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,1000000))
_LinkBandwidthControlEgressLimit_Type.__name__=_B
_LinkBandwidthControlEgressLimit_Object=MibTableColumn
linkBandwidthControlEgressLimit=_LinkBandwidthControlEgressLimit_Object((1,3,6,1,4,1,4935,1000,100,200,100,3700,1,100,1,200),_LinkBandwidthControlEgressLimit_Type())
linkBandwidthControlEgressLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:linkBandwidthControlEgressLimit.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,3700,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_B
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,3700,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_F)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,3700,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_B
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,3700,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ntcMIB':ntcMIB,'ntcMIBObjects':ntcMIBObjects,'linkBandwidthControlTable':linkBandwidthControlTable,'linkBandwidthControlEntry':linkBandwidthControlEntry,_D:linkBandwidthControlLinkName,'linkBandwidthControlEgressLimit':linkBandwidthControlEgressLimit,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})