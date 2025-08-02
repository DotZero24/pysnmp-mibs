_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
begemotNtp=ModuleIdentity((1,3,6,1,4,1,12325,1,201))
_BegemotNtpObjects_ObjectIdentity=ObjectIdentity
begemotNtpObjects=_BegemotNtpObjects_ObjectIdentity((1,3,6,1,4,1,12325,1,201,1))
_BegemotNtpHost_Type=OctetString
_BegemotNtpHost_Object=MibScalar
begemotNtpHost=_BegemotNtpHost_Object((1,3,6,1,4,1,12325,1,201,1,1),_BegemotNtpHost_Type())
begemotNtpHost.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNtpHost.setStatus(_A)
_BegemotNtpPort_Type=OctetString
_BegemotNtpPort_Object=MibScalar
begemotNtpPort=_BegemotNtpPort_Object((1,3,6,1,4,1,12325,1,201,1,2),_BegemotNtpPort_Type())
begemotNtpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNtpPort.setStatus(_A)
_BegemotNtpTimeout_Type=TimeTicks
_BegemotNtpTimeout_Object=MibScalar
begemotNtpTimeout=_BegemotNtpTimeout_Object((1,3,6,1,4,1,12325,1,201,1,3),_BegemotNtpTimeout_Type())
begemotNtpTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotNtpTimeout.setStatus(_A)
_BegemotNtpDebug_Type=Unsigned32
_BegemotNtpDebug_Object=MibScalar
begemotNtpDebug=_BegemotNtpDebug_Object((1,3,6,1,4,1,12325,1,201,1,4),_BegemotNtpDebug_Type())
begemotNtpDebug.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotNtpDebug.setStatus(_A)
_BegemotNtpJitter_Type=Counter64
_BegemotNtpJitter_Object=MibScalar
begemotNtpJitter=_BegemotNtpJitter_Object((1,3,6,1,4,1,12325,1,201,1,5),_BegemotNtpJitter_Type())
begemotNtpJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNtpJitter.setStatus(_A)
_BegemotNtpStability_Type=Counter64
_BegemotNtpStability_Object=MibScalar
begemotNtpStability=_BegemotNtpStability_Object((1,3,6,1,4,1,12325,1,201,1,6),_BegemotNtpStability_Type())
begemotNtpStability.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNtpStability.setStatus(_A)
_BegemotNtpJitterThresh_Type=Counter64
_BegemotNtpJitterThresh_Object=MibScalar
begemotNtpJitterThresh=_BegemotNtpJitterThresh_Object((1,3,6,1,4,1,12325,1,201,1,7),_BegemotNtpJitterThresh_Type())
begemotNtpJitterThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNtpJitterThresh.setStatus(_A)
_BegemotNtpStabilityThresh_Type=Counter64
_BegemotNtpStabilityThresh_Object=MibScalar
begemotNtpStabilityThresh=_BegemotNtpStabilityThresh_Object((1,3,6,1,4,1,12325,1,201,1,8),_BegemotNtpStabilityThresh_Type())
begemotNtpStabilityThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNtpStabilityThresh.setStatus(_A)
_BegemotNtpTrapEnable_Type=TruthValue
_BegemotNtpTrapEnable_Object=MibScalar
begemotNtpTrapEnable=_BegemotNtpTrapEnable_Object((1,3,6,1,4,1,12325,1,201,1,9),_BegemotNtpTrapEnable_Type())
begemotNtpTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotNtpTrapEnable.setStatus(_A)
mibBuilder.exportSymbols('BEGEMOT-NTP-MIB',**{'begemotNtp':begemotNtp,'begemotNtpObjects':begemotNtpObjects,'begemotNtpHost':begemotNtpHost,'begemotNtpPort':begemotNtpPort,'begemotNtpTimeout':begemotNtpTimeout,'begemotNtpDebug':begemotNtpDebug,'begemotNtpJitter':begemotNtpJitter,'begemotNtpStability':begemotNtpStability,'begemotNtpJitterThresh':begemotNtpJitterThresh,'begemotNtpStabilityThresh':begemotNtpStabilityThresh,'begemotNtpTrapEnable':begemotNtpTrapEnable})