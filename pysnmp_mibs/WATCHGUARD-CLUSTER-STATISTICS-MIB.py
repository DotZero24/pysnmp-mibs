_I='standby'
_H='master'
_G='backup'
_F='worker'
_E='disabled'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
watchguard,=mibBuilder.importSymbols('WATCHGUARD-SMI','watchguard')
wgInfoModule=ModuleIdentity((1,3,6,1,4,1,3097,6))
if mibBuilder.loadTexts:wgInfoModule.setRevisions(('2007-01-25 12:00',))
_WgClusterStatusMIB_ObjectIdentity=ObjectIdentity
wgClusterStatusMIB=_WgClusterStatusMIB_ObjectIdentity((1,3,6,1,4,1,3097,6,6))
if mibBuilder.loadTexts:wgClusterStatusMIB.setStatus(_A)
class _WgClusterEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('enabled',1)))
_WgClusterEnabled_Type.__name__=_C
_WgClusterEnabled_Object=MibScalar
wgClusterEnabled=_WgClusterEnabled_Object((1,3,6,1,4,1,3097,6,6,1),_WgClusterEnabled_Type())
wgClusterEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClusterEnabled.setStatus(_A)
class _WgFirstMemberId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WgFirstMemberId_Type.__name__=_D
_WgFirstMemberId_Object=MibScalar
wgFirstMemberId=_WgFirstMemberId_Object((1,3,6,1,4,1,3097,6,6,2),_WgFirstMemberId_Type())
wgFirstMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgFirstMemberId.setStatus(_A)
class _WgFirstMemberRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),(_H,3),('idle',4),(_I,5)))
_WgFirstMemberRole_Type.__name__=_C
_WgFirstMemberRole_Object=MibScalar
wgFirstMemberRole=_WgFirstMemberRole_Object((1,3,6,1,4,1,3097,6,6,3),_WgFirstMemberRole_Type())
wgFirstMemberRole.setMaxAccess(_B)
if mibBuilder.loadTexts:wgFirstMemberRole.setStatus(_A)
_WgFirstMemberSystemHealth_Type=Integer32
_WgFirstMemberSystemHealth_Object=MibScalar
wgFirstMemberSystemHealth=_WgFirstMemberSystemHealth_Object((1,3,6,1,4,1,3097,6,6,4),_WgFirstMemberSystemHealth_Type())
wgFirstMemberSystemHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:wgFirstMemberSystemHealth.setStatus(_A)
_WgFirstMemberHardwareHealth_Type=Integer32
_WgFirstMemberHardwareHealth_Object=MibScalar
wgFirstMemberHardwareHealth=_WgFirstMemberHardwareHealth_Object((1,3,6,1,4,1,3097,6,6,5),_WgFirstMemberHardwareHealth_Type())
wgFirstMemberHardwareHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:wgFirstMemberHardwareHealth.setStatus(_A)
_WgFirstMemberMonitorPortHealth_Type=Integer32
_WgFirstMemberMonitorPortHealth_Object=MibScalar
wgFirstMemberMonitorPortHealth=_WgFirstMemberMonitorPortHealth_Object((1,3,6,1,4,1,3097,6,6,6),_WgFirstMemberMonitorPortHealth_Type())
wgFirstMemberMonitorPortHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:wgFirstMemberMonitorPortHealth.setStatus(_A)
_WgFirstMemberWeightAvg_Type=Integer32
_WgFirstMemberWeightAvg_Object=MibScalar
wgFirstMemberWeightAvg=_WgFirstMemberWeightAvg_Object((1,3,6,1,4,1,3097,6,6,7),_WgFirstMemberWeightAvg_Type())
wgFirstMemberWeightAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgFirstMemberWeightAvg.setStatus(_A)
class _WgSecondMemberId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WgSecondMemberId_Type.__name__=_D
_WgSecondMemberId_Object=MibScalar
wgSecondMemberId=_WgSecondMemberId_Object((1,3,6,1,4,1,3097,6,6,8),_WgSecondMemberId_Type())
wgSecondMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSecondMemberId.setStatus(_A)
class _WgSecondMemberRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),(_H,3),('idle',4),(_I,5)))
_WgSecondMemberRole_Type.__name__=_C
_WgSecondMemberRole_Object=MibScalar
wgSecondMemberRole=_WgSecondMemberRole_Object((1,3,6,1,4,1,3097,6,6,9),_WgSecondMemberRole_Type())
wgSecondMemberRole.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSecondMemberRole.setStatus(_A)
_WgSecondMemberSystemHealth_Type=Integer32
_WgSecondMemberSystemHealth_Object=MibScalar
wgSecondMemberSystemHealth=_WgSecondMemberSystemHealth_Object((1,3,6,1,4,1,3097,6,6,10),_WgSecondMemberSystemHealth_Type())
wgSecondMemberSystemHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSecondMemberSystemHealth.setStatus(_A)
_WgSecondMemberHardwareHealth_Type=Integer32
_WgSecondMemberHardwareHealth_Object=MibScalar
wgSecondMemberHardwareHealth=_WgSecondMemberHardwareHealth_Object((1,3,6,1,4,1,3097,6,6,11),_WgSecondMemberHardwareHealth_Type())
wgSecondMemberHardwareHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSecondMemberHardwareHealth.setStatus(_A)
_WgSecondMemberMonitorPortHealth_Type=Integer32
_WgSecondMemberMonitorPortHealth_Object=MibScalar
wgSecondMemberMonitorPortHealth=_WgSecondMemberMonitorPortHealth_Object((1,3,6,1,4,1,3097,6,6,12),_WgSecondMemberMonitorPortHealth_Type())
wgSecondMemberMonitorPortHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSecondMemberMonitorPortHealth.setStatus(_A)
_WgSecondMemberWeightAvg_Type=Integer32
_WgSecondMemberWeightAvg_Object=MibScalar
wgSecondMemberWeightAvg=_WgSecondMemberWeightAvg_Object((1,3,6,1,4,1,3097,6,6,13),_WgSecondMemberWeightAvg_Type())
wgSecondMemberWeightAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgSecondMemberWeightAvg.setStatus(_A)
mibBuilder.exportSymbols('WATCHGUARD-CLUSTER-STATISTICS-MIB',**{'wgInfoModule':wgInfoModule,'wgClusterStatusMIB':wgClusterStatusMIB,'wgClusterEnabled':wgClusterEnabled,'wgFirstMemberId':wgFirstMemberId,'wgFirstMemberRole':wgFirstMemberRole,'wgFirstMemberSystemHealth':wgFirstMemberSystemHealth,'wgFirstMemberHardwareHealth':wgFirstMemberHardwareHealth,'wgFirstMemberMonitorPortHealth':wgFirstMemberMonitorPortHealth,'wgFirstMemberWeightAvg':wgFirstMemberWeightAvg,'wgSecondMemberId':wgSecondMemberId,'wgSecondMemberRole':wgSecondMemberRole,'wgSecondMemberSystemHealth':wgSecondMemberSystemHealth,'wgSecondMemberHardwareHealth':wgSecondMemberHardwareHealth,'wgSecondMemberMonitorPortHealth':wgSecondMemberMonitorPortHealth,'wgSecondMemberWeightAvg':wgSecondMemberWeightAvg})