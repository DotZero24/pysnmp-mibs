_E='qtechMPLSFecIndex'
_D='QTECH-MPLS-SIGNAL-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType','InetPortNumber')
AreaID,DesignatedRouterPriority,HelloRange,PositiveInteger,RouterID,Status=mibBuilder.importSymbols('OSPF-MIB','AreaID','DesignatedRouterPriority','HelloRange','PositiveInteger','RouterID','Status')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,=mibBuilder.importSymbols('QTECH-TC','ConfigStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
qtechMplsSignalMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,98))
if mibBuilder.loadTexts:qtechMplsSignalMIB.setRevisions(('2011-05-15 00:00',))
_QtechMplsSignalMIBObjects_ObjectIdentity=ObjectIdentity
qtechMplsSignalMIBObjects=_QtechMplsSignalMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,98,1))
_QtechMplsSignalObjects_ObjectIdentity=ObjectIdentity
qtechMplsSignalObjects=_QtechMplsSignalObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,98,1,1))
_QtechMplsSignalmplsGernalMibObjects_ObjectIdentity=ObjectIdentity
qtechMplsSignalmplsGernalMibObjects=_QtechMplsSignalmplsGernalMibObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,1))
_QtechMplsVersion_Type=Unsigned32
_QtechMplsVersion_Object=MibScalar
qtechMplsVersion=_QtechMplsVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,1,1),_QtechMplsVersion_Type())
qtechMplsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVersion.setStatus(_A)
class _QtechMPLSSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ldp',1),('rsvp-te',2),('cr-ldp',3),('other',4)))
_QtechMPLSSignal_Type.__name__=_C
_QtechMPLSSignal_Object=MibScalar
qtechMPLSSignal=_QtechMPLSSignal_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,1,2),_QtechMPLSSignal_Type())
qtechMPLSSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSSignal.setStatus(_A)
_QtechMPLSTESignal_Type=TruthValue
_QtechMPLSTESignal_Object=MibScalar
qtechMPLSTESignal=_QtechMPLSTESignal_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,1,3),_QtechMPLSTESignal_Type())
qtechMPLSTESignal.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSTESignal.setStatus(_A)
_QtechMplsSignalConfigMibObjects_ObjectIdentity=ObjectIdentity
qtechMplsSignalConfigMibObjects=_QtechMplsSignalConfigMibObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,2))
_QtechMPLSConfigLspNum_Type=Unsigned32
_QtechMPLSConfigLspNum_Object=MibScalar
qtechMPLSConfigLspNum=_QtechMPLSConfigLspNum_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,2,1),_QtechMPLSConfigLspNum_Type())
qtechMPLSConfigLspNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSConfigLspNum.setStatus(_A)
_QtechMPLSActiveLspNum_Type=Unsigned32
_QtechMPLSActiveLspNum_Object=MibScalar
qtechMPLSActiveLspNum=_QtechMPLSActiveLspNum_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,2,2),_QtechMPLSActiveLspNum_Type())
qtechMPLSActiveLspNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSActiveLspNum.setStatus(_A)
_QtechMPLSAdministrativeGroupTable_Object=MibTable
qtechMPLSAdministrativeGroupTable=_QtechMPLSAdministrativeGroupTable_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3))
if mibBuilder.loadTexts:qtechMPLSAdministrativeGroupTable.setStatus(_A)
_QtechMPLSAdministrativeGroupEntry_Object=MibTableRow
qtechMPLSAdministrativeGroupEntry=_QtechMPLSAdministrativeGroupEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1))
qtechMPLSAdministrativeGroupEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:qtechMPLSAdministrativeGroupEntry.setStatus(_A)
_QtechMPLSFecIndex_Type=Integer32
_QtechMPLSFecIndex_Object=MibTableColumn
qtechMPLSFecIndex=_QtechMPLSFecIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,1),_QtechMPLSFecIndex_Type())
qtechMPLSFecIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechMPLSFecIndex.setStatus(_A)
_QtechMPLSLSPName_Type=DisplayString
_QtechMPLSLSPName_Object=MibTableColumn
qtechMPLSLSPName=_QtechMPLSLSPName_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,2),_QtechMPLSLSPName_Type())
qtechMPLSLSPName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPName.setStatus(_A)
class _QtechMPLSLSPStates_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_QtechMPLSLSPStates_Type.__name__=_C
_QtechMPLSLSPStates_Object=MibTableColumn
qtechMPLSLSPStates=_QtechMPLSLSPStates_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,3),_QtechMPLSLSPStates_Type())
qtechMPLSLSPStates.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPStates.setStatus(_A)
_QtechMPLSLSPForwardBytes_Type=Integer32
_QtechMPLSLSPForwardBytes_Object=MibTableColumn
qtechMPLSLSPForwardBytes=_QtechMPLSLSPForwardBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,4),_QtechMPLSLSPForwardBytes_Type())
qtechMPLSLSPForwardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPForwardBytes.setStatus(_A)
_QtechMPLSLSPForwardPackets_Type=Integer32
_QtechMPLSLSPForwardPackets_Object=MibTableColumn
qtechMPLSLSPForwardPackets=_QtechMPLSLSPForwardPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,5),_QtechMPLSLSPForwardPackets_Type())
qtechMPLSLSPForwardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPForwardPackets.setStatus(_A)
_QtechMPLSLSPActiveTime_Type=TimeStamp
_QtechMPLSLSPActiveTime_Object=MibTableColumn
qtechMPLSLSPActiveTime=_QtechMPLSLSPActiveTime_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,6),_QtechMPLSLSPActiveTime_Type())
qtechMPLSLSPActiveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPActiveTime.setStatus(_A)
_QtechMPLSLSPCreationTime_Type=TimeStamp
_QtechMPLSLSPCreationTime_Object=MibTableColumn
qtechMPLSLSPCreationTime=_QtechMPLSLSPCreationTime_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,7),_QtechMPLSLSPCreationTime_Type())
qtechMPLSLSPCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPCreationTime.setStatus(_A)
_QtechMPLSLSPPrimaryCreationTime_Type=TimeStamp
_QtechMPLSLSPPrimaryCreationTime_Object=MibTableColumn
qtechMPLSLSPPrimaryCreationTime=_QtechMPLSLSPPrimaryCreationTime_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,8),_QtechMPLSLSPPrimaryCreationTime_Type())
qtechMPLSLSPPrimaryCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPPrimaryCreationTime.setStatus(_A)
_QtechMPLSLSPSwitchTimes_Type=Integer32
_QtechMPLSLSPSwitchTimes_Object=MibTableColumn
qtechMPLSLSPSwitchTimes=_QtechMPLSLSPSwitchTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,9),_QtechMPLSLSPSwitchTimes_Type())
qtechMPLSLSPSwitchTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPSwitchTimes.setStatus(_A)
_QtechMPLSLSPLatestSwitchTime_Type=TimeStamp
_QtechMPLSLSPLatestSwitchTime_Object=MibTableColumn
qtechMPLSLSPLatestSwitchTime=_QtechMPLSLSPLatestSwitchTime_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,10),_QtechMPLSLSPLatestSwitchTime_Type())
qtechMPLSLSPLatestSwitchTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPLatestSwitchTime.setStatus(_A)
_QtechMPLSLSPPathchangeTime_Type=TimeStamp
_QtechMPLSLSPPathchangeTime_Object=MibTableColumn
qtechMPLSLSPPathchangeTime=_QtechMPLSLSPPathchangeTime_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,11),_QtechMPLSLSPPathchangeTime_Type())
qtechMPLSLSPPathchangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPPathchangeTime.setStatus(_A)
_QtechMPLSLSPConfigChangeTime_Type=TimeStamp
_QtechMPLSLSPConfigChangeTime_Object=MibTableColumn
qtechMPLSLSPConfigChangeTime=_QtechMPLSLSPConfigChangeTime_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,12),_QtechMPLSLSPConfigChangeTime_Type())
qtechMPLSLSPConfigChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPConfigChangeTime.setStatus(_A)
_QtechMPLSLSPBackupPath_Type=DisplayString
_QtechMPLSLSPBackupPath_Object=MibTableColumn
qtechMPLSLSPBackupPath=_QtechMPLSLSPBackupPath_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,13),_QtechMPLSLSPBackupPath_Type())
qtechMPLSLSPBackupPath.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPBackupPath.setStatus(_A)
class _QtechMPLSLSPOperationPath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('backup',2),('none',3)))
_QtechMPLSLSPOperationPath_Type.__name__=_C
_QtechMPLSLSPOperationPath_Object=MibTableColumn
qtechMPLSLSPOperationPath=_QtechMPLSLSPOperationPath_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,14),_QtechMPLSLSPOperationPath_Type())
qtechMPLSLSPOperationPath.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPOperationPath.setStatus(_A)
_QtechMPLSLSPIngress_Type=InetAddressType
_QtechMPLSLSPIngress_Object=MibTableColumn
qtechMPLSLSPIngress=_QtechMPLSLSPIngress_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,15),_QtechMPLSLSPIngress_Type())
qtechMPLSLSPIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPIngress.setStatus(_A)
_QtechMPLSLSPDestination_Type=InetAddressType
_QtechMPLSLSPDestination_Object=MibTableColumn
qtechMPLSLSPDestination=_QtechMPLSLSPDestination_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,16),_QtechMPLSLSPDestination_Type())
qtechMPLSLSPDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPDestination.setStatus(_A)
_QtechMPLSLSPAdministrativeGroupName_Type=DisplayString
_QtechMPLSLSPAdministrativeGroupName_Object=MibTableColumn
qtechMPLSLSPAdministrativeGroupName=_QtechMPLSLSPAdministrativeGroupName_Object((1,3,6,1,4,1,27514,1,1,10,2,98,1,1,3,1,17),_QtechMPLSLSPAdministrativeGroupName_Type())
qtechMPLSLSPAdministrativeGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMPLSLSPAdministrativeGroupName.setStatus(_A)
_QtechMplsSignalConformance_ObjectIdentity=ObjectIdentity
qtechMplsSignalConformance=_QtechMplsSignalConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,98,1,2))
mibBuilder.exportSymbols(_D,**{'qtechMplsSignalMIB':qtechMplsSignalMIB,'qtechMplsSignalMIBObjects':qtechMplsSignalMIBObjects,'qtechMplsSignalObjects':qtechMplsSignalObjects,'qtechMplsSignalmplsGernalMibObjects':qtechMplsSignalmplsGernalMibObjects,'qtechMplsVersion':qtechMplsVersion,'qtechMPLSSignal':qtechMPLSSignal,'qtechMPLSTESignal':qtechMPLSTESignal,'qtechMplsSignalConfigMibObjects':qtechMplsSignalConfigMibObjects,'qtechMPLSConfigLspNum':qtechMPLSConfigLspNum,'qtechMPLSActiveLspNum':qtechMPLSActiveLspNum,'qtechMPLSAdministrativeGroupTable':qtechMPLSAdministrativeGroupTable,'qtechMPLSAdministrativeGroupEntry':qtechMPLSAdministrativeGroupEntry,_E:qtechMPLSFecIndex,'qtechMPLSLSPName':qtechMPLSLSPName,'qtechMPLSLSPStates':qtechMPLSLSPStates,'qtechMPLSLSPForwardBytes':qtechMPLSLSPForwardBytes,'qtechMPLSLSPForwardPackets':qtechMPLSLSPForwardPackets,'qtechMPLSLSPActiveTime':qtechMPLSLSPActiveTime,'qtechMPLSLSPCreationTime':qtechMPLSLSPCreationTime,'qtechMPLSLSPPrimaryCreationTime':qtechMPLSLSPPrimaryCreationTime,'qtechMPLSLSPSwitchTimes':qtechMPLSLSPSwitchTimes,'qtechMPLSLSPLatestSwitchTime':qtechMPLSLSPLatestSwitchTime,'qtechMPLSLSPPathchangeTime':qtechMPLSLSPPathchangeTime,'qtechMPLSLSPConfigChangeTime':qtechMPLSLSPConfigChangeTime,'qtechMPLSLSPBackupPath':qtechMPLSLSPBackupPath,'qtechMPLSLSPOperationPath':qtechMPLSLSPOperationPath,'qtechMPLSLSPIngress':qtechMPLSLSPIngress,'qtechMPLSLSPDestination':qtechMPLSLSPDestination,'qtechMPLSLSPAdministrativeGroupName':qtechMPLSLSPAdministrativeGroupName,'qtechMplsSignalConformance':qtechMplsSignalConformance})