_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelLoadSharing=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,44))
_ZyxelLoadSharingSetup_ObjectIdentity=ObjectIdentity
zyxelLoadSharingSetup=_ZyxelLoadSharingSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,44,1))
_ZyLoadSharingState_Type=EnabledStatus
_ZyLoadSharingState_Object=MibScalar
zyLoadSharingState=_ZyLoadSharingState_Object((1,3,6,1,4,1,890,1,15,3,44,1,1),_ZyLoadSharingState_Type())
zyLoadSharingState.setMaxAccess(_A)
if mibBuilder.loadTexts:zyLoadSharingState.setStatus(_B)
class _ZyLoadSharingCriteria_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('srcIp',1),('srcDstIp',2)))
_ZyLoadSharingCriteria_Type.__name__=_C
_ZyLoadSharingCriteria_Object=MibScalar
zyLoadSharingCriteria=_ZyLoadSharingCriteria_Object((1,3,6,1,4,1,890,1,15,3,44,1,2),_ZyLoadSharingCriteria_Type())
zyLoadSharingCriteria.setMaxAccess(_A)
if mibBuilder.loadTexts:zyLoadSharingCriteria.setStatus(_B)
_ZyLoadSharingAgingTime_Type=Integer32
_ZyLoadSharingAgingTime_Object=MibScalar
zyLoadSharingAgingTime=_ZyLoadSharingAgingTime_Object((1,3,6,1,4,1,890,1,15,3,44,1,3),_ZyLoadSharingAgingTime_Type())
zyLoadSharingAgingTime.setMaxAccess(_A)
if mibBuilder.loadTexts:zyLoadSharingAgingTime.setStatus(_B)
_ZyLoadSharingDiscoverTime_Type=Integer32
_ZyLoadSharingDiscoverTime_Object=MibScalar
zyLoadSharingDiscoverTime=_ZyLoadSharingDiscoverTime_Object((1,3,6,1,4,1,890,1,15,3,44,1,4),_ZyLoadSharingDiscoverTime_Type())
zyLoadSharingDiscoverTime.setMaxAccess(_A)
if mibBuilder.loadTexts:zyLoadSharingDiscoverTime.setStatus(_B)
_ZyLoadSharingMaxPaths_Type=Integer32
_ZyLoadSharingMaxPaths_Object=MibScalar
zyLoadSharingMaxPaths=_ZyLoadSharingMaxPaths_Object((1,3,6,1,4,1,890,1,15,3,44,1,5),_ZyLoadSharingMaxPaths_Type())
zyLoadSharingMaxPaths.setMaxAccess(_A)
if mibBuilder.loadTexts:zyLoadSharingMaxPaths.setStatus(_B)
mibBuilder.exportSymbols('ZYXEL-LOAD-SHARING-MIB',**{'zyxelLoadSharing':zyxelLoadSharing,'zyxelLoadSharingSetup':zyxelLoadSharingSetup,'zyLoadSharingState':zyLoadSharingState,'zyLoadSharingCriteria':zyLoadSharingCriteria,'zyLoadSharingAgingTime':zyLoadSharingAgingTime,'zyLoadSharingDiscoverTime':zyLoadSharingDiscoverTime,'zyLoadSharingMaxPaths':zyLoadSharingMaxPaths})