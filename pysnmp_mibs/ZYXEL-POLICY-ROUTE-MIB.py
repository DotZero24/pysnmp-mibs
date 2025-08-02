_J='zyPolicyRouteSequence'
_I='zyPolicyRouteProfile'
_H='read-create'
_G='zyPolicyRouteProfileName'
_F='read-only'
_E='Integer32'
_D='not-accessible'
_C='read-write'
_B='ZYXEL-POLICY-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelPolicyRoute=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,60))
_ZyxelPolicyRouteSetup_ObjectIdentity=ObjectIdentity
zyxelPolicyRouteSetup=_ZyxelPolicyRouteSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,60,1))
_ZyPolicyRouteMaxNumberOfProfiles_Type=Integer32
_ZyPolicyRouteMaxNumberOfProfiles_Object=MibScalar
zyPolicyRouteMaxNumberOfProfiles=_ZyPolicyRouteMaxNumberOfProfiles_Object((1,3,6,1,4,1,890,1,15,3,60,1,1),_ZyPolicyRouteMaxNumberOfProfiles_Type())
zyPolicyRouteMaxNumberOfProfiles.setMaxAccess(_F)
if mibBuilder.loadTexts:zyPolicyRouteMaxNumberOfProfiles.setStatus(_A)
_ZyxelPolicyRouteProfileTable_Object=MibTable
zyxelPolicyRouteProfileTable=_ZyxelPolicyRouteProfileTable_Object((1,3,6,1,4,1,890,1,15,3,60,1,2))
if mibBuilder.loadTexts:zyxelPolicyRouteProfileTable.setStatus(_A)
_ZyxelPolicyRouteProfileEntry_Object=MibTableRow
zyxelPolicyRouteProfileEntry=_ZyxelPolicyRouteProfileEntry_Object((1,3,6,1,4,1,890,1,15,3,60,1,2,1))
zyxelPolicyRouteProfileEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:zyxelPolicyRouteProfileEntry.setStatus(_A)
_ZyPolicyRouteProfileState_Type=EnabledStatus
_ZyPolicyRouteProfileState_Object=MibTableColumn
zyPolicyRouteProfileState=_ZyPolicyRouteProfileState_Object((1,3,6,1,4,1,890,1,15,3,60,1,2,1,1),_ZyPolicyRouteProfileState_Type())
zyPolicyRouteProfileState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPolicyRouteProfileState.setStatus(_A)
_ZyPolicyRouteProfileName_Type=DisplayString
_ZyPolicyRouteProfileName_Object=MibTableColumn
zyPolicyRouteProfileName=_ZyPolicyRouteProfileName_Object((1,3,6,1,4,1,890,1,15,3,60,1,2,1,2),_ZyPolicyRouteProfileName_Type())
zyPolicyRouteProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPolicyRouteProfileName.setStatus(_A)
_ZyPolicyRouteProfileRowStatus_Type=RowStatus
_ZyPolicyRouteProfileRowStatus_Object=MibTableColumn
zyPolicyRouteProfileRowStatus=_ZyPolicyRouteProfileRowStatus_Object((1,3,6,1,4,1,890,1,15,3,60,1,2,1,3),_ZyPolicyRouteProfileRowStatus_Type())
zyPolicyRouteProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zyPolicyRouteProfileRowStatus.setStatus(_A)
_ZyPolicyRouteMaxNumberOfRules_Type=Integer32
_ZyPolicyRouteMaxNumberOfRules_Object=MibScalar
zyPolicyRouteMaxNumberOfRules=_ZyPolicyRouteMaxNumberOfRules_Object((1,3,6,1,4,1,890,1,15,3,60,1,3),_ZyPolicyRouteMaxNumberOfRules_Type())
zyPolicyRouteMaxNumberOfRules.setMaxAccess(_F)
if mibBuilder.loadTexts:zyPolicyRouteMaxNumberOfRules.setStatus(_A)
_ZyxelPolicyRouteTable_Object=MibTable
zyxelPolicyRouteTable=_ZyxelPolicyRouteTable_Object((1,3,6,1,4,1,890,1,15,3,60,1,4))
if mibBuilder.loadTexts:zyxelPolicyRouteTable.setStatus(_A)
_ZyxelPolicyRouteEntry_Object=MibTableRow
zyxelPolicyRouteEntry=_ZyxelPolicyRouteEntry_Object((1,3,6,1,4,1,890,1,15,3,60,1,4,1))
zyxelPolicyRouteEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:zyxelPolicyRouteEntry.setStatus(_A)
_ZyPolicyRouteProfile_Type=DisplayString
_ZyPolicyRouteProfile_Object=MibTableColumn
zyPolicyRouteProfile=_ZyPolicyRouteProfile_Object((1,3,6,1,4,1,890,1,15,3,60,1,4,1,1),_ZyPolicyRouteProfile_Type())
zyPolicyRouteProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPolicyRouteProfile.setStatus(_A)
_ZyPolicyRouteSequence_Type=Integer32
_ZyPolicyRouteSequence_Object=MibTableColumn
zyPolicyRouteSequence=_ZyPolicyRouteSequence_Object((1,3,6,1,4,1,890,1,15,3,60,1,4,1,2),_ZyPolicyRouteSequence_Type())
zyPolicyRouteSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPolicyRouteSequence.setStatus(_A)
class _ZyPolicyRouteStatement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('permit',0),('deny',1)))
_ZyPolicyRouteStatement_Type.__name__=_E
_ZyPolicyRouteStatement_Object=MibTableColumn
zyPolicyRouteStatement=_ZyPolicyRouteStatement_Object((1,3,6,1,4,1,890,1,15,3,60,1,4,1,3),_ZyPolicyRouteStatement_Type())
zyPolicyRouteStatement.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPolicyRouteStatement.setStatus(_A)
_ZyPolicyRouteCalssifier_Type=DisplayString
_ZyPolicyRouteCalssifier_Object=MibTableColumn
zyPolicyRouteCalssifier=_ZyPolicyRouteCalssifier_Object((1,3,6,1,4,1,890,1,15,3,60,1,4,1,4),_ZyPolicyRouteCalssifier_Type())
zyPolicyRouteCalssifier.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPolicyRouteCalssifier.setStatus(_A)
_ZyPolicyRouteNextHop_Type=IpAddress
_ZyPolicyRouteNextHop_Object=MibTableColumn
zyPolicyRouteNextHop=_ZyPolicyRouteNextHop_Object((1,3,6,1,4,1,890,1,15,3,60,1,4,1,5),_ZyPolicyRouteNextHop_Type())
zyPolicyRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPolicyRouteNextHop.setStatus(_A)
_ZyPolicyRouteRowStatus_Type=RowStatus
_ZyPolicyRouteRowStatus_Object=MibTableColumn
zyPolicyRouteRowStatus=_ZyPolicyRouteRowStatus_Object((1,3,6,1,4,1,890,1,15,3,60,1,4,1,6),_ZyPolicyRouteRowStatus_Type())
zyPolicyRouteRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zyPolicyRouteRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelPolicyRoute':zyxelPolicyRoute,'zyxelPolicyRouteSetup':zyxelPolicyRouteSetup,'zyPolicyRouteMaxNumberOfProfiles':zyPolicyRouteMaxNumberOfProfiles,'zyxelPolicyRouteProfileTable':zyxelPolicyRouteProfileTable,'zyxelPolicyRouteProfileEntry':zyxelPolicyRouteProfileEntry,'zyPolicyRouteProfileState':zyPolicyRouteProfileState,_G:zyPolicyRouteProfileName,'zyPolicyRouteProfileRowStatus':zyPolicyRouteProfileRowStatus,'zyPolicyRouteMaxNumberOfRules':zyPolicyRouteMaxNumberOfRules,'zyxelPolicyRouteTable':zyxelPolicyRouteTable,'zyxelPolicyRouteEntry':zyxelPolicyRouteEntry,_I:zyPolicyRouteProfile,_J:zyPolicyRouteSequence,'zyPolicyRouteStatement':zyPolicyRouteStatement,'zyPolicyRouteCalssifier':zyPolicyRouteCalssifier,'zyPolicyRouteNextHop':zyPolicyRouteNextHop,'zyPolicyRouteRowStatus':zyPolicyRouteRowStatus})