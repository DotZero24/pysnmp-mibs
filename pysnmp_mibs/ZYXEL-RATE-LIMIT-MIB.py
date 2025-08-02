_D='dot1dBasePort'
_C='BRIDGE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_C,_D)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelRateLimit=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,72))
_ZyxelRateLimitSetup_ObjectIdentity=ObjectIdentity
zyxelRateLimitSetup=_ZyxelRateLimitSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,72,1))
_ZyRateLimitState_Type=EnabledStatus
_ZyRateLimitState_Object=MibScalar
zyRateLimitState=_ZyRateLimitState_Object((1,3,6,1,4,1,890,1,15,3,72,1,1),_ZyRateLimitState_Type())
zyRateLimitState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRateLimitState.setStatus(_A)
_ZyxelRateLimitPortTable_Object=MibTable
zyxelRateLimitPortTable=_ZyxelRateLimitPortTable_Object((1,3,6,1,4,1,890,1,15,3,72,1,2))
if mibBuilder.loadTexts:zyxelRateLimitPortTable.setStatus(_A)
_ZyxelRateLimitPortEntry_Object=MibTableRow
zyxelRateLimitPortEntry=_ZyxelRateLimitPortEntry_Object((1,3,6,1,4,1,890,1,15,3,72,1,2,1))
zyxelRateLimitPortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelRateLimitPortEntry.setStatus(_A)
_ZyRateLimitPortCommitState_Type=EnabledStatus
_ZyRateLimitPortCommitState_Object=MibTableColumn
zyRateLimitPortCommitState=_ZyRateLimitPortCommitState_Object((1,3,6,1,4,1,890,1,15,3,72,1,2,1,1),_ZyRateLimitPortCommitState_Type())
zyRateLimitPortCommitState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRateLimitPortCommitState.setStatus(_A)
_ZyRateLimitPortCommitRate_Type=Integer32
_ZyRateLimitPortCommitRate_Object=MibTableColumn
zyRateLimitPortCommitRate=_ZyRateLimitPortCommitRate_Object((1,3,6,1,4,1,890,1,15,3,72,1,2,1,2),_ZyRateLimitPortCommitRate_Type())
zyRateLimitPortCommitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRateLimitPortCommitRate.setStatus(_A)
_ZyRateLimitPortPeakState_Type=EnabledStatus
_ZyRateLimitPortPeakState_Object=MibTableColumn
zyRateLimitPortPeakState=_ZyRateLimitPortPeakState_Object((1,3,6,1,4,1,890,1,15,3,72,1,2,1,3),_ZyRateLimitPortPeakState_Type())
zyRateLimitPortPeakState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRateLimitPortPeakState.setStatus(_A)
_ZyRateLimitPortPeakRate_Type=Integer32
_ZyRateLimitPortPeakRate_Object=MibTableColumn
zyRateLimitPortPeakRate=_ZyRateLimitPortPeakRate_Object((1,3,6,1,4,1,890,1,15,3,72,1,2,1,4),_ZyRateLimitPortPeakRate_Type())
zyRateLimitPortPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRateLimitPortPeakRate.setStatus(_A)
_ZyRateLimitPortEgressState_Type=EnabledStatus
_ZyRateLimitPortEgressState_Object=MibTableColumn
zyRateLimitPortEgressState=_ZyRateLimitPortEgressState_Object((1,3,6,1,4,1,890,1,15,3,72,1,2,1,5),_ZyRateLimitPortEgressState_Type())
zyRateLimitPortEgressState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRateLimitPortEgressState.setStatus(_A)
_ZyRateLimitPortEgressRate_Type=Integer32
_ZyRateLimitPortEgressRate_Object=MibTableColumn
zyRateLimitPortEgressRate=_ZyRateLimitPortEgressRate_Object((1,3,6,1,4,1,890,1,15,3,72,1,2,1,6),_ZyRateLimitPortEgressRate_Type())
zyRateLimitPortEgressRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRateLimitPortEgressRate.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-RATE-LIMIT-MIB',**{'zyxelRateLimit':zyxelRateLimit,'zyxelRateLimitSetup':zyxelRateLimitSetup,'zyRateLimitState':zyRateLimitState,'zyxelRateLimitPortTable':zyxelRateLimitPortTable,'zyxelRateLimitPortEntry':zyxelRateLimitPortEntry,'zyRateLimitPortCommitState':zyRateLimitPortCommitState,'zyRateLimitPortCommitRate':zyRateLimitPortCommitRate,'zyRateLimitPortPeakState':zyRateLimitPortPeakState,'zyRateLimitPortPeakRate':zyRateLimitPortPeakRate,'zyRateLimitPortEgressState':zyRateLimitPortEgressState,'zyRateLimitPortEgressRate':zyRateLimitPortEgressRate})