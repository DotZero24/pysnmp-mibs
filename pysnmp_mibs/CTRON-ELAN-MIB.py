_P='ctElanSFDSPeerIP'
_O='destroy'
_N='createAndWait'
_M='createAndGo'
_L='notReady'
_K='notInService'
_J='ctElanConfIndex'
_I='DisplayString'
_H='unknown'
_G='active'
_F='CTRON-ELAN-MIB'
_E='CtLaneDebugLevel'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctAtmfLanEmulation,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctAtmfLanEmulation')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
class CtLaneDebugLevel(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('user',1),('all',2),('error',3),('warning',4),('informational',5),('detailed',6),('trace',7)))
class ElanLocalIndex(Integer32):0
_CtLeClient_ObjectIdentity=ObjectIdentity
ctLeClient=_CtLeClient_ObjectIdentity((1,3,6,1,4,1,52,4,3,5,1))
_CtElan_ObjectIdentity=ObjectIdentity
ctElan=_CtElan_ObjectIdentity((1,3,6,1,4,1,52,4,3,5,2))
_CtElanConfGroup_ObjectIdentity=ObjectIdentity
ctElanConfGroup=_CtElanConfGroup_ObjectIdentity((1,3,6,1,4,1,52,4,3,5,2,1))
_CtElanConfTable_Object=MibTable
ctElanConfTable=_CtElanConfTable_Object((1,3,6,1,4,1,52,4,3,5,2,1,1))
if mibBuilder.loadTexts:ctElanConfTable.setStatus(_A)
_CtElanConfEntry_Object=MibTableRow
ctElanConfEntry=_CtElanConfEntry_Object((1,3,6,1,4,1,52,4,3,5,2,1,1,1))
ctElanConfEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:ctElanConfEntry.setStatus(_A)
_CtElanConfIndex_Type=ElanLocalIndex
_CtElanConfIndex_Object=MibTableColumn
ctElanConfIndex=_CtElanConfIndex_Object((1,3,6,1,4,1,52,4,3,5,2,1,1,1,1),_CtElanConfIndex_Type())
ctElanConfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ctElanConfIndex.setStatus(_A)
class _CtElanConfUnitNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_CtElanConfUnitNumber_Type.__name__=_C
_CtElanConfUnitNumber_Object=MibTableColumn
ctElanConfUnitNumber=_CtElanConfUnitNumber_Object((1,3,6,1,4,1,52,4,3,5,2,1,1,1,2),_CtElanConfUnitNumber_Type())
ctElanConfUnitNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ctElanConfUnitNumber.setStatus(_A)
class _CtElanConfPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('secure',1),('nonsecure',2)))
_CtElanConfPolicy_Type.__name__=_C
_CtElanConfPolicy_Object=MibTableColumn
ctElanConfPolicy=_CtElanConfPolicy_Object((1,3,6,1,4,1,52,4,3,5,2,1,1,1,3),_CtElanConfPolicy_Type())
ctElanConfPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanConfPolicy.setStatus(_A)
class _CtElanConfDelPolicyWithElan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_CtElanConfDelPolicyWithElan_Type.__name__=_C
_CtElanConfDelPolicyWithElan_Object=MibTableColumn
ctElanConfDelPolicyWithElan=_CtElanConfDelPolicyWithElan_Object((1,3,6,1,4,1,52,4,3,5,2,1,1,1,4),_CtElanConfDelPolicyWithElan_Type())
ctElanConfDelPolicyWithElan.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanConfDelPolicyWithElan.setStatus(_A)
class _CtElanConfRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6)))
_CtElanConfRowStatus_Type.__name__=_C
_CtElanConfRowStatus_Object=MibTableColumn
ctElanConfRowStatus=_CtElanConfRowStatus_Object((1,3,6,1,4,1,52,4,3,5,2,1,1,1,5),_CtElanConfRowStatus_Type())
ctElanConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanConfRowStatus.setStatus(_A)
_CtElanSFDSPeerTable_Object=MibTable
ctElanSFDSPeerTable=_CtElanSFDSPeerTable_Object((1,3,6,1,4,1,52,4,3,5,2,1,2))
if mibBuilder.loadTexts:ctElanSFDSPeerTable.setStatus(_A)
_CtElanSFDSPeerEntry_Object=MibTableRow
ctElanSFDSPeerEntry=_CtElanSFDSPeerEntry_Object((1,3,6,1,4,1,52,4,3,5,2,1,2,1))
ctElanSFDSPeerEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:ctElanSFDSPeerEntry.setStatus(_A)
_CtElanSFDSPeerIP_Type=IpAddress
_CtElanSFDSPeerIP_Object=MibTableColumn
ctElanSFDSPeerIP=_CtElanSFDSPeerIP_Object((1,3,6,1,4,1,52,4,3,5,2,1,2,1,1),_CtElanSFDSPeerIP_Type())
ctElanSFDSPeerIP.setMaxAccess(_D)
if mibBuilder.loadTexts:ctElanSFDSPeerIP.setStatus(_A)
class _CtElanSFDSPeerRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6)))
_CtElanSFDSPeerRowStatus_Type.__name__=_C
_CtElanSFDSPeerRowStatus_Object=MibTableColumn
ctElanSFDSPeerRowStatus=_CtElanSFDSPeerRowStatus_Object((1,3,6,1,4,1,52,4,3,5,2,1,2,1,2),_CtElanSFDSPeerRowStatus_Type())
ctElanSFDSPeerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanSFDSPeerRowStatus.setStatus(_A)
_CtElanConfDirectoryServicesIP_Type=IpAddress
_CtElanConfDirectoryServicesIP_Object=MibScalar
ctElanConfDirectoryServicesIP=_CtElanConfDirectoryServicesIP_Object((1,3,6,1,4,1,52,4,3,5,2,1,3),_CtElanConfDirectoryServicesIP_Type())
ctElanConfDirectoryServicesIP.setMaxAccess(_D)
if mibBuilder.loadTexts:ctElanConfDirectoryServicesIP.setStatus(_A)
class _CtElanDSStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('connected',1),('connectionLost',2),(_H,3)))
_CtElanDSStatus_Type.__name__=_C
_CtElanDSStatus_Object=MibScalar
ctElanDSStatus=_CtElanDSStatus_Object((1,3,6,1,4,1,52,4,3,5,2,1,4),_CtElanDSStatus_Type())
ctElanDSStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctElanDSStatus.setStatus(_A)
class _CtElanUNIVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('uni30',2),('uni31',3),('uni40',4)))
_CtElanUNIVersion_Type.__name__=_C
_CtElanUNIVersion_Object=MibScalar
ctElanUNIVersion=_CtElanUNIVersion_Object((1,3,6,1,4,1,52,4,3,5,2,1,5),_CtElanUNIVersion_Type())
ctElanUNIVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:ctElanUNIVersion.setStatus(_A)
class _CtElanLaneDbgOutputFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtElanLaneDbgOutputFile_Type.__name__=_I
_CtElanLaneDbgOutputFile_Object=MibScalar
ctElanLaneDbgOutputFile=_CtElanLaneDbgOutputFile_Object((1,3,6,1,4,1,52,4,3,5,2,1,6),_CtElanLaneDbgOutputFile_Type())
ctElanLaneDbgOutputFile.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanLaneDbgOutputFile.setStatus(_A)
class _CtElanLaneDbgConnectionServices_Type(CtLaneDebugLevel):defaultValue=1
_CtElanLaneDbgConnectionServices_Type.__name__=_E
_CtElanLaneDbgConnectionServices_Object=MibScalar
ctElanLaneDbgConnectionServices=_CtElanLaneDbgConnectionServices_Object((1,3,6,1,4,1,52,4,3,5,2,1,7),_CtElanLaneDbgConnectionServices_Type())
ctElanLaneDbgConnectionServices.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanLaneDbgConnectionServices.setStatus(_A)
class _CtElanLaneDbgDatabaseManagement_Type(CtLaneDebugLevel):defaultValue=1
_CtElanLaneDbgDatabaseManagement_Type.__name__=_E
_CtElanLaneDbgDatabaseManagement_Object=MibScalar
ctElanLaneDbgDatabaseManagement=_CtElanLaneDbgDatabaseManagement_Object((1,3,6,1,4,1,52,4,3,5,2,1,8),_CtElanLaneDbgDatabaseManagement_Type())
ctElanLaneDbgDatabaseManagement.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanLaneDbgDatabaseManagement.setStatus(_A)
class _CtElanCtLaneDbgSNMP_Type(CtLaneDebugLevel):defaultValue=1
_CtElanCtLaneDbgSNMP_Type.__name__=_E
_CtElanCtLaneDbgSNMP_Object=MibScalar
ctElanCtLaneDbgSNMP=_CtElanCtLaneDbgSNMP_Object((1,3,6,1,4,1,52,4,3,5,2,1,9),_CtElanCtLaneDbgSNMP_Type())
ctElanCtLaneDbgSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanCtLaneDbgSNMP.setStatus(_A)
class _CtElanLaneDbgLECS_Type(CtLaneDebugLevel):defaultValue=1
_CtElanLaneDbgLECS_Type.__name__=_E
_CtElanLaneDbgLECS_Object=MibScalar
ctElanLaneDbgLECS=_CtElanLaneDbgLECS_Object((1,3,6,1,4,1,52,4,3,5,2,1,10),_CtElanLaneDbgLECS_Type())
ctElanLaneDbgLECS.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanLaneDbgLECS.setStatus(_A)
class _CtElanCtLaneDbgLES_Type(CtLaneDebugLevel):defaultValue=1
_CtElanCtLaneDbgLES_Type.__name__=_E
_CtElanCtLaneDbgLES_Object=MibScalar
ctElanCtLaneDbgLES=_CtElanCtLaneDbgLES_Object((1,3,6,1,4,1,52,4,3,5,2,1,11),_CtElanCtLaneDbgLES_Type())
ctElanCtLaneDbgLES.setMaxAccess(_B)
if mibBuilder.loadTexts:ctElanCtLaneDbgLES.setStatus(_A)
class _CtElanHotStandbyStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initial',1),(_G,2),('standby',3),(_H,4)))
_CtElanHotStandbyStatus_Type.__name__=_C
_CtElanHotStandbyStatus_Object=MibScalar
ctElanHotStandbyStatus=_CtElanHotStandbyStatus_Object((1,3,6,1,4,1,52,4,3,5,2,1,12),_CtElanHotStandbyStatus_Type())
ctElanHotStandbyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctElanHotStandbyStatus.setStatus(_A)
_CtElanConfHotStandbyIP_Type=IpAddress
_CtElanConfHotStandbyIP_Object=MibScalar
ctElanConfHotStandbyIP=_CtElanConfHotStandbyIP_Object((1,3,6,1,4,1,52,4,3,5,2,1,13),_CtElanConfHotStandbyIP_Type())
ctElanConfHotStandbyIP.setMaxAccess(_D)
if mibBuilder.loadTexts:ctElanConfHotStandbyIP.setStatus(_A)
_CtLes_ObjectIdentity=ObjectIdentity
ctLes=_CtLes_ObjectIdentity((1,3,6,1,4,1,52,4,3,5,3))
_CtBus_ObjectIdentity=ObjectIdentity
ctBus=_CtBus_ObjectIdentity((1,3,6,1,4,1,52,4,3,5,4))
mibBuilder.exportSymbols(_F,**{_E:CtLaneDebugLevel,'ElanLocalIndex':ElanLocalIndex,'ctLeClient':ctLeClient,'ctElan':ctElan,'ctElanConfGroup':ctElanConfGroup,'ctElanConfTable':ctElanConfTable,'ctElanConfEntry':ctElanConfEntry,_J:ctElanConfIndex,'ctElanConfUnitNumber':ctElanConfUnitNumber,'ctElanConfPolicy':ctElanConfPolicy,'ctElanConfDelPolicyWithElan':ctElanConfDelPolicyWithElan,'ctElanConfRowStatus':ctElanConfRowStatus,'ctElanSFDSPeerTable':ctElanSFDSPeerTable,'ctElanSFDSPeerEntry':ctElanSFDSPeerEntry,_P:ctElanSFDSPeerIP,'ctElanSFDSPeerRowStatus':ctElanSFDSPeerRowStatus,'ctElanConfDirectoryServicesIP':ctElanConfDirectoryServicesIP,'ctElanDSStatus':ctElanDSStatus,'ctElanUNIVersion':ctElanUNIVersion,'ctElanLaneDbgOutputFile':ctElanLaneDbgOutputFile,'ctElanLaneDbgConnectionServices':ctElanLaneDbgConnectionServices,'ctElanLaneDbgDatabaseManagement':ctElanLaneDbgDatabaseManagement,'ctElanCtLaneDbgSNMP':ctElanCtLaneDbgSNMP,'ctElanLaneDbgLECS':ctElanLaneDbgLECS,'ctElanCtLaneDbgLES':ctElanCtLaneDbgLES,'ctElanHotStandbyStatus':ctElanHotStandbyStatus,'ctElanConfHotStandbyIP':ctElanConfHotStandbyIP,'ctLes':ctLes,'ctBus':ctBus})