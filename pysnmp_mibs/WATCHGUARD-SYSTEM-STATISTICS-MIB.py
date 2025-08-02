_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
watchguard,=mibBuilder.importSymbols('WATCHGUARD-SMI','watchguard')
wgInfoModule=ModuleIdentity((1,3,6,1,4,1,3097,6))
if mibBuilder.loadTexts:wgInfoModule.setRevisions(('2007-01-25 12:00',))
_WgSystemStatisticsMIB_ObjectIdentity=ObjectIdentity
wgSystemStatisticsMIB=_WgSystemStatisticsMIB_ObjectIdentity((1,3,6,1,4,1,3097,6,3))
if mibBuilder.loadTexts:wgSystemStatisticsMIB.setStatus(_A)
class _WgSoftwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WgSoftwareVersion_Type.__name__=_C
_WgSoftwareVersion_Object=MibScalar
wgSoftwareVersion=_WgSoftwareVersion_Object((1,3,6,1,4,1,3097,6,3,1),_WgSoftwareVersion_Type())
wgSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSoftwareVersion.setStatus(_A)
_WgSystemCpuUtil_Type=Counter64
_WgSystemCpuUtil_Object=MibScalar
wgSystemCpuUtil=_WgSystemCpuUtil_Object((1,3,6,1,4,1,3097,6,3,4),_WgSystemCpuUtil_Type())
wgSystemCpuUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemCpuUtil.setStatus(_A)
_WgSystemTotalSendBytes_Type=Counter64
_WgSystemTotalSendBytes_Object=MibScalar
wgSystemTotalSendBytes=_WgSystemTotalSendBytes_Object((1,3,6,1,4,1,3097,6,3,8),_WgSystemTotalSendBytes_Type())
wgSystemTotalSendBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemTotalSendBytes.setStatus(_A)
_WgSystemTotalRecvBytes_Type=Counter64
_WgSystemTotalRecvBytes_Object=MibScalar
wgSystemTotalRecvBytes=_WgSystemTotalRecvBytes_Object((1,3,6,1,4,1,3097,6,3,9),_WgSystemTotalRecvBytes_Type())
wgSystemTotalRecvBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemTotalRecvBytes.setStatus(_A)
_WgSystemTotalSendPackets_Type=Counter64
_WgSystemTotalSendPackets_Object=MibScalar
wgSystemTotalSendPackets=_WgSystemTotalSendPackets_Object((1,3,6,1,4,1,3097,6,3,10),_WgSystemTotalSendPackets_Type())
wgSystemTotalSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemTotalSendPackets.setStatus(_A)
_WgSystemTotalRecvPackets_Type=Counter64
_WgSystemTotalRecvPackets_Object=MibScalar
wgSystemTotalRecvPackets=_WgSystemTotalRecvPackets_Object((1,3,6,1,4,1,3097,6,3,11),_WgSystemTotalRecvPackets_Type())
wgSystemTotalRecvPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemTotalRecvPackets.setStatus(_A)
_WgSystemStreamReqTotal_Type=Counter64
_WgSystemStreamReqTotal_Object=MibScalar
wgSystemStreamReqTotal=_WgSystemStreamReqTotal_Object((1,3,6,1,4,1,3097,6,3,30),_WgSystemStreamReqTotal_Type())
wgSystemStreamReqTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemStreamReqTotal.setStatus(_A)
_WgSystemStreamReqDrop_Type=Counter64
_WgSystemStreamReqDrop_Object=MibScalar
wgSystemStreamReqDrop=_WgSystemStreamReqDrop_Object((1,3,6,1,4,1,3097,6,3,34),_WgSystemStreamReqDrop_Type())
wgSystemStreamReqDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemStreamReqDrop.setStatus(_A)
_WgSystemCpuUtil1_Type=Counter64
_WgSystemCpuUtil1_Object=MibScalar
wgSystemCpuUtil1=_WgSystemCpuUtil1_Object((1,3,6,1,4,1,3097,6,3,77),_WgSystemCpuUtil1_Type())
wgSystemCpuUtil1.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemCpuUtil1.setStatus(_A)
_WgSystemCpuUtil5_Type=Counter64
_WgSystemCpuUtil5_Object=MibScalar
wgSystemCpuUtil5=_WgSystemCpuUtil5_Object((1,3,6,1,4,1,3097,6,3,78),_WgSystemCpuUtil5_Type())
wgSystemCpuUtil5.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemCpuUtil5.setStatus(_A)
_WgSystemCpuUtil15_Type=Counter64
_WgSystemCpuUtil15_Object=MibScalar
wgSystemCpuUtil15=_WgSystemCpuUtil15_Object((1,3,6,1,4,1,3097,6,3,79),_WgSystemCpuUtil15_Type())
wgSystemCpuUtil15.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemCpuUtil15.setStatus(_A)
_WgSystemCurrActiveConns_Type=Counter64
_WgSystemCurrActiveConns_Object=MibScalar
wgSystemCurrActiveConns=_WgSystemCurrActiveConns_Object((1,3,6,1,4,1,3097,6,3,80),_WgSystemCurrActiveConns_Type())
wgSystemCurrActiveConns.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSystemCurrActiveConns.setStatus(_A)
mibBuilder.exportSymbols('WATCHGUARD-SYSTEM-STATISTICS-MIB',**{'wgInfoModule':wgInfoModule,'wgSystemStatisticsMIB':wgSystemStatisticsMIB,'wgSoftwareVersion':wgSoftwareVersion,'wgSystemCpuUtil':wgSystemCpuUtil,'wgSystemTotalSendBytes':wgSystemTotalSendBytes,'wgSystemTotalRecvBytes':wgSystemTotalRecvBytes,'wgSystemTotalSendPackets':wgSystemTotalSendPackets,'wgSystemTotalRecvPackets':wgSystemTotalRecvPackets,'wgSystemStreamReqTotal':wgSystemStreamReqTotal,'wgSystemStreamReqDrop':wgSystemStreamReqDrop,'wgSystemCpuUtil1':wgSystemCpuUtil1,'wgSystemCpuUtil5':wgSystemCpuUtil5,'wgSystemCpuUtil15':wgSystemCpuUtil15,'wgSystemCurrActiveConns':wgSystemCurrActiveConns})