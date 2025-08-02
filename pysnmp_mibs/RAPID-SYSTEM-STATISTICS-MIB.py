_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rapidstream,=mibBuilder.importSymbols('RAPID-MIB','rapidstream')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rsInfoModule=ModuleIdentity((1,3,6,1,4,1,4355,6))
if mibBuilder.loadTexts:rsInfoModule.setRevisions(('2001-05-16 12:00','2002-11-01 12:00'))
_RsSystemStatisticsMIB_ObjectIdentity=ObjectIdentity
rsSystemStatisticsMIB=_RsSystemStatisticsMIB_ObjectIdentity((1,3,6,1,4,1,4355,6,3))
if mibBuilder.loadTexts:rsSystemStatisticsMIB.setStatus(_A)
_RsSystemCpuUtil_Type=Counter64
_RsSystemCpuUtil_Object=MibScalar
rsSystemCpuUtil=_RsSystemCpuUtil_Object((1,3,6,1,4,1,4355,6,3,4),_RsSystemCpuUtil_Type())
rsSystemCpuUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemCpuUtil.setStatus(_A)
_RsSystemTotalSendBytes_Type=Counter64
_RsSystemTotalSendBytes_Object=MibScalar
rsSystemTotalSendBytes=_RsSystemTotalSendBytes_Object((1,3,6,1,4,1,4355,6,3,8),_RsSystemTotalSendBytes_Type())
rsSystemTotalSendBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemTotalSendBytes.setStatus(_A)
_RsSystemTotalRecvBytes_Type=Counter64
_RsSystemTotalRecvBytes_Object=MibScalar
rsSystemTotalRecvBytes=_RsSystemTotalRecvBytes_Object((1,3,6,1,4,1,4355,6,3,9),_RsSystemTotalRecvBytes_Type())
rsSystemTotalRecvBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemTotalRecvBytes.setStatus(_A)
_RsSystemTotalSendPackets_Type=Counter64
_RsSystemTotalSendPackets_Object=MibScalar
rsSystemTotalSendPackets=_RsSystemTotalSendPackets_Object((1,3,6,1,4,1,4355,6,3,10),_RsSystemTotalSendPackets_Type())
rsSystemTotalSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemTotalSendPackets.setStatus(_A)
_RsSystemTotalRecvPackets_Type=Counter64
_RsSystemTotalRecvPackets_Object=MibScalar
rsSystemTotalRecvPackets=_RsSystemTotalRecvPackets_Object((1,3,6,1,4,1,4355,6,3,11),_RsSystemTotalRecvPackets_Type())
rsSystemTotalRecvPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemTotalRecvPackets.setStatus(_A)
_RsSystemStreamReqTotal_Type=Counter64
_RsSystemStreamReqTotal_Object=MibScalar
rsSystemStreamReqTotal=_RsSystemStreamReqTotal_Object((1,3,6,1,4,1,4355,6,3,30),_RsSystemStreamReqTotal_Type())
rsSystemStreamReqTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemStreamReqTotal.setStatus(_A)
_RsSystemStreamReqDrop_Type=Counter64
_RsSystemStreamReqDrop_Object=MibScalar
rsSystemStreamReqDrop=_RsSystemStreamReqDrop_Object((1,3,6,1,4,1,4355,6,3,34),_RsSystemStreamReqDrop_Type())
rsSystemStreamReqDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemStreamReqDrop.setStatus(_A)
_RsSystemCpuUtil1_Type=Counter64
_RsSystemCpuUtil1_Object=MibScalar
rsSystemCpuUtil1=_RsSystemCpuUtil1_Object((1,3,6,1,4,1,4355,6,3,77),_RsSystemCpuUtil1_Type())
rsSystemCpuUtil1.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemCpuUtil1.setStatus(_A)
_RsSystemCpuUtil5_Type=Counter64
_RsSystemCpuUtil5_Object=MibScalar
rsSystemCpuUtil5=_RsSystemCpuUtil5_Object((1,3,6,1,4,1,4355,6,3,78),_RsSystemCpuUtil5_Type())
rsSystemCpuUtil5.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemCpuUtil5.setStatus(_A)
_RsSystemCpuUtil15_Type=Counter64
_RsSystemCpuUtil15_Object=MibScalar
rsSystemCpuUtil15=_RsSystemCpuUtil15_Object((1,3,6,1,4,1,4355,6,3,79),_RsSystemCpuUtil15_Type())
rsSystemCpuUtil15.setMaxAccess(_B)
if mibBuilder.loadTexts:rsSystemCpuUtil15.setStatus(_A)
mibBuilder.exportSymbols('RAPID-SYSTEM-STATISTICS-MIB',**{'rsInfoModule':rsInfoModule,'rsSystemStatisticsMIB':rsSystemStatisticsMIB,'rsSystemCpuUtil':rsSystemCpuUtil,'rsSystemTotalSendBytes':rsSystemTotalSendBytes,'rsSystemTotalRecvBytes':rsSystemTotalRecvBytes,'rsSystemTotalSendPackets':rsSystemTotalSendPackets,'rsSystemTotalRecvPackets':rsSystemTotalRecvPackets,'rsSystemStreamReqTotal':rsSystemStreamReqTotal,'rsSystemStreamReqDrop':rsSystemStreamReqDrop,'rsSystemCpuUtil1':rsSystemCpuUtil1,'rsSystemCpuUtil5':rsSystemCpuUtil5,'rsSystemCpuUtil15':rsSystemCpuUtil15})