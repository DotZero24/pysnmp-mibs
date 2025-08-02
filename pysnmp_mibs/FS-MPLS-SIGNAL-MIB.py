_E='fsMPLSFecIndex'
_D='FS-MPLS-SIGNAL-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,=mibBuilder.importSymbols('FS-TC','ConfigStatus')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType','InetPortNumber')
AreaID,DesignatedRouterPriority,HelloRange,PositiveInteger,RouterID,Status=mibBuilder.importSymbols('OSPF-MIB','AreaID','DesignatedRouterPriority','HelloRange','PositiveInteger','RouterID','Status')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
fsMplsSignalMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,98))
if mibBuilder.loadTexts:fsMplsSignalMIB.setRevisions(('2011-05-15 00:00',))
_FsMplsSignalMIBObjects_ObjectIdentity=ObjectIdentity
fsMplsSignalMIBObjects=_FsMplsSignalMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,98,1))
_FsMplsSignalObjects_ObjectIdentity=ObjectIdentity
fsMplsSignalObjects=_FsMplsSignalObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,98,1,1))
_FsMplsSignalmplsGernalMibObjects_ObjectIdentity=ObjectIdentity
fsMplsSignalmplsGernalMibObjects=_FsMplsSignalmplsGernalMibObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,1))
_FsMplsVersion_Type=Unsigned32
_FsMplsVersion_Object=MibScalar
fsMplsVersion=_FsMplsVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,1,1),_FsMplsVersion_Type())
fsMplsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVersion.setStatus(_A)
class _FsMPLSSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ldp',1),('rsvp-te',2),('cr-ldp',3),('other',4)))
_FsMPLSSignal_Type.__name__=_C
_FsMPLSSignal_Object=MibScalar
fsMPLSSignal=_FsMPLSSignal_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,1,2),_FsMPLSSignal_Type())
fsMPLSSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSSignal.setStatus(_A)
_FsMPLSTESignal_Type=TruthValue
_FsMPLSTESignal_Object=MibScalar
fsMPLSTESignal=_FsMPLSTESignal_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,1,3),_FsMPLSTESignal_Type())
fsMPLSTESignal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSTESignal.setStatus(_A)
_FsMplsSignalConfigMibObjects_ObjectIdentity=ObjectIdentity
fsMplsSignalConfigMibObjects=_FsMplsSignalConfigMibObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,2))
_FsMPLSConfigLspNum_Type=Unsigned32
_FsMPLSConfigLspNum_Object=MibScalar
fsMPLSConfigLspNum=_FsMPLSConfigLspNum_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,2,1),_FsMPLSConfigLspNum_Type())
fsMPLSConfigLspNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSConfigLspNum.setStatus(_A)
_FsMPLSActiveLspNum_Type=Unsigned32
_FsMPLSActiveLspNum_Object=MibScalar
fsMPLSActiveLspNum=_FsMPLSActiveLspNum_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,2,2),_FsMPLSActiveLspNum_Type())
fsMPLSActiveLspNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSActiveLspNum.setStatus(_A)
_FsMPLSAdministrativeGroupTable_Object=MibTable
fsMPLSAdministrativeGroupTable=_FsMPLSAdministrativeGroupTable_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3))
if mibBuilder.loadTexts:fsMPLSAdministrativeGroupTable.setStatus(_A)
_FsMPLSAdministrativeGroupEntry_Object=MibTableRow
fsMPLSAdministrativeGroupEntry=_FsMPLSAdministrativeGroupEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1))
fsMPLSAdministrativeGroupEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fsMPLSAdministrativeGroupEntry.setStatus(_A)
_FsMPLSFecIndex_Type=Integer32
_FsMPLSFecIndex_Object=MibTableColumn
fsMPLSFecIndex=_FsMPLSFecIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,1),_FsMPLSFecIndex_Type())
fsMPLSFecIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsMPLSFecIndex.setStatus(_A)
_FsMPLSLSPName_Type=DisplayString
_FsMPLSLSPName_Object=MibTableColumn
fsMPLSLSPName=_FsMPLSLSPName_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,2),_FsMPLSLSPName_Type())
fsMPLSLSPName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPName.setStatus(_A)
class _FsMPLSLSPStates_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_FsMPLSLSPStates_Type.__name__=_C
_FsMPLSLSPStates_Object=MibTableColumn
fsMPLSLSPStates=_FsMPLSLSPStates_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,3),_FsMPLSLSPStates_Type())
fsMPLSLSPStates.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPStates.setStatus(_A)
_FsMPLSLSPForwardBytes_Type=Integer32
_FsMPLSLSPForwardBytes_Object=MibTableColumn
fsMPLSLSPForwardBytes=_FsMPLSLSPForwardBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,4),_FsMPLSLSPForwardBytes_Type())
fsMPLSLSPForwardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPForwardBytes.setStatus(_A)
_FsMPLSLSPForwardPackets_Type=Integer32
_FsMPLSLSPForwardPackets_Object=MibTableColumn
fsMPLSLSPForwardPackets=_FsMPLSLSPForwardPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,5),_FsMPLSLSPForwardPackets_Type())
fsMPLSLSPForwardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPForwardPackets.setStatus(_A)
_FsMPLSLSPActiveTime_Type=TimeStamp
_FsMPLSLSPActiveTime_Object=MibTableColumn
fsMPLSLSPActiveTime=_FsMPLSLSPActiveTime_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,6),_FsMPLSLSPActiveTime_Type())
fsMPLSLSPActiveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPActiveTime.setStatus(_A)
_FsMPLSLSPCreationTime_Type=TimeStamp
_FsMPLSLSPCreationTime_Object=MibTableColumn
fsMPLSLSPCreationTime=_FsMPLSLSPCreationTime_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,7),_FsMPLSLSPCreationTime_Type())
fsMPLSLSPCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPCreationTime.setStatus(_A)
_FsMPLSLSPPrimaryCreationTime_Type=TimeStamp
_FsMPLSLSPPrimaryCreationTime_Object=MibTableColumn
fsMPLSLSPPrimaryCreationTime=_FsMPLSLSPPrimaryCreationTime_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,8),_FsMPLSLSPPrimaryCreationTime_Type())
fsMPLSLSPPrimaryCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPPrimaryCreationTime.setStatus(_A)
_FsMPLSLSPSwitchTimes_Type=Integer32
_FsMPLSLSPSwitchTimes_Object=MibTableColumn
fsMPLSLSPSwitchTimes=_FsMPLSLSPSwitchTimes_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,9),_FsMPLSLSPSwitchTimes_Type())
fsMPLSLSPSwitchTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPSwitchTimes.setStatus(_A)
_FsMPLSLSPLatestSwitchTime_Type=TimeStamp
_FsMPLSLSPLatestSwitchTime_Object=MibTableColumn
fsMPLSLSPLatestSwitchTime=_FsMPLSLSPLatestSwitchTime_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,10),_FsMPLSLSPLatestSwitchTime_Type())
fsMPLSLSPLatestSwitchTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPLatestSwitchTime.setStatus(_A)
_FsMPLSLSPPathchangeTime_Type=TimeStamp
_FsMPLSLSPPathchangeTime_Object=MibTableColumn
fsMPLSLSPPathchangeTime=_FsMPLSLSPPathchangeTime_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,11),_FsMPLSLSPPathchangeTime_Type())
fsMPLSLSPPathchangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPPathchangeTime.setStatus(_A)
_FsMPLSLSPConfigChangeTime_Type=TimeStamp
_FsMPLSLSPConfigChangeTime_Object=MibTableColumn
fsMPLSLSPConfigChangeTime=_FsMPLSLSPConfigChangeTime_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,12),_FsMPLSLSPConfigChangeTime_Type())
fsMPLSLSPConfigChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPConfigChangeTime.setStatus(_A)
_FsMPLSLSPBackupPath_Type=DisplayString
_FsMPLSLSPBackupPath_Object=MibTableColumn
fsMPLSLSPBackupPath=_FsMPLSLSPBackupPath_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,13),_FsMPLSLSPBackupPath_Type())
fsMPLSLSPBackupPath.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPBackupPath.setStatus(_A)
class _FsMPLSLSPOperationPath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('backup',2),('none',3)))
_FsMPLSLSPOperationPath_Type.__name__=_C
_FsMPLSLSPOperationPath_Object=MibTableColumn
fsMPLSLSPOperationPath=_FsMPLSLSPOperationPath_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,14),_FsMPLSLSPOperationPath_Type())
fsMPLSLSPOperationPath.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPOperationPath.setStatus(_A)
_FsMPLSLSPIngress_Type=InetAddressType
_FsMPLSLSPIngress_Object=MibTableColumn
fsMPLSLSPIngress=_FsMPLSLSPIngress_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,15),_FsMPLSLSPIngress_Type())
fsMPLSLSPIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPIngress.setStatus(_A)
_FsMPLSLSPDestination_Type=InetAddressType
_FsMPLSLSPDestination_Object=MibTableColumn
fsMPLSLSPDestination=_FsMPLSLSPDestination_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,16),_FsMPLSLSPDestination_Type())
fsMPLSLSPDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPDestination.setStatus(_A)
_FsMPLSLSPAdministrativeGroupName_Type=DisplayString
_FsMPLSLSPAdministrativeGroupName_Object=MibTableColumn
fsMPLSLSPAdministrativeGroupName=_FsMPLSLSPAdministrativeGroupName_Object((1,3,6,1,4,1,52642,1,1,10,2,98,1,1,3,1,17),_FsMPLSLSPAdministrativeGroupName_Type())
fsMPLSLSPAdministrativeGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMPLSLSPAdministrativeGroupName.setStatus(_A)
_FsMplsSignalConformance_ObjectIdentity=ObjectIdentity
fsMplsSignalConformance=_FsMplsSignalConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,98,1,2))
mibBuilder.exportSymbols(_D,**{'fsMplsSignalMIB':fsMplsSignalMIB,'fsMplsSignalMIBObjects':fsMplsSignalMIBObjects,'fsMplsSignalObjects':fsMplsSignalObjects,'fsMplsSignalmplsGernalMibObjects':fsMplsSignalmplsGernalMibObjects,'fsMplsVersion':fsMplsVersion,'fsMPLSSignal':fsMPLSSignal,'fsMPLSTESignal':fsMPLSTESignal,'fsMplsSignalConfigMibObjects':fsMplsSignalConfigMibObjects,'fsMPLSConfigLspNum':fsMPLSConfigLspNum,'fsMPLSActiveLspNum':fsMPLSActiveLspNum,'fsMPLSAdministrativeGroupTable':fsMPLSAdministrativeGroupTable,'fsMPLSAdministrativeGroupEntry':fsMPLSAdministrativeGroupEntry,_E:fsMPLSFecIndex,'fsMPLSLSPName':fsMPLSLSPName,'fsMPLSLSPStates':fsMPLSLSPStates,'fsMPLSLSPForwardBytes':fsMPLSLSPForwardBytes,'fsMPLSLSPForwardPackets':fsMPLSLSPForwardPackets,'fsMPLSLSPActiveTime':fsMPLSLSPActiveTime,'fsMPLSLSPCreationTime':fsMPLSLSPCreationTime,'fsMPLSLSPPrimaryCreationTime':fsMPLSLSPPrimaryCreationTime,'fsMPLSLSPSwitchTimes':fsMPLSLSPSwitchTimes,'fsMPLSLSPLatestSwitchTime':fsMPLSLSPLatestSwitchTime,'fsMPLSLSPPathchangeTime':fsMPLSLSPPathchangeTime,'fsMPLSLSPConfigChangeTime':fsMPLSLSPConfigChangeTime,'fsMPLSLSPBackupPath':fsMPLSLSPBackupPath,'fsMPLSLSPOperationPath':fsMPLSLSPOperationPath,'fsMPLSLSPIngress':fsMPLSLSPIngress,'fsMPLSLSPDestination':fsMPLSLSPDestination,'fsMPLSLSPAdministrativeGroupName':fsMPLSLSPAdministrativeGroupName,'fsMplsSignalConformance':fsMplsSignalConformance})