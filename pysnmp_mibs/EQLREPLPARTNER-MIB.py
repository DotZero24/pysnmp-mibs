_G='unknown'
_F='eqliscsiVolumeReplSiteIndex'
_E='EQLVOLUME-MIB'
_D='read-create'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SiteIndex,eqliscsiVolumeReplSiteIndex=mibBuilder.importSymbols(_E,'SiteIndex',_F)
equalLogic,=mibBuilder.importSymbols('EQUALLOGIC-SMI','equalLogic')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
eqlReplPartnerModule=ModuleIdentity((1,3,6,1,4,1,12740,26))
if mibBuilder.loadTexts:eqlReplPartnerModule.setRevisions(('2013-03-28 00:00',))
class EqlReplPartnerTestStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('valid',1),('invalid',2),('remote-partner-not-configured',3)))
_EqlReplPartnerObjects_ObjectIdentity=ObjectIdentity
eqlReplPartnerObjects=_EqlReplPartnerObjects_ObjectIdentity((1,3,6,1,4,1,12740,26,1))
_EqlReplPartnerTestTable_Object=MibTable
eqlReplPartnerTestTable=_EqlReplPartnerTestTable_Object((1,3,6,1,4,1,12740,26,1,1))
if mibBuilder.loadTexts:eqlReplPartnerTestTable.setStatus(_A)
_EqlReplPartnerTestEntry_Object=MibTableRow
eqlReplPartnerTestEntry=_EqlReplPartnerTestEntry_Object((1,3,6,1,4,1,12740,26,1,1,1))
eqlReplPartnerTestEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:eqlReplPartnerTestEntry.setStatus(_A)
_EqlReplPartnerTestRowStatus_Type=RowStatus
_EqlReplPartnerTestRowStatus_Object=MibTableColumn
eqlReplPartnerTestRowStatus=_EqlReplPartnerTestRowStatus_Object((1,3,6,1,4,1,12740,26,1,1,1,1),_EqlReplPartnerTestRowStatus_Type())
eqlReplPartnerTestRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eqlReplPartnerTestRowStatus.setStatus(_A)
_EqlReplPartnerTestIPAddrStatus_Type=EqlReplPartnerTestStatus
_EqlReplPartnerTestIPAddrStatus_Object=MibTableColumn
eqlReplPartnerTestIPAddrStatus=_EqlReplPartnerTestIPAddrStatus_Object((1,3,6,1,4,1,12740,26,1,1,1,2),_EqlReplPartnerTestIPAddrStatus_Type())
eqlReplPartnerTestIPAddrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eqlReplPartnerTestIPAddrStatus.setStatus(_A)
_EqlReplPartnerTestAuthStatus_Type=EqlReplPartnerTestStatus
_EqlReplPartnerTestAuthStatus_Object=MibTableColumn
eqlReplPartnerTestAuthStatus=_EqlReplPartnerTestAuthStatus_Object((1,3,6,1,4,1,12740,26,1,1,1,3),_EqlReplPartnerTestAuthStatus_Type())
eqlReplPartnerTestAuthStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eqlReplPartnerTestAuthStatus.setStatus(_A)
class _EqlReplPartnerTestAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('start',1)))
_EqlReplPartnerTestAction_Type.__name__=_B
_EqlReplPartnerTestAction_Object=MibTableColumn
eqlReplPartnerTestAction=_EqlReplPartnerTestAction_Object((1,3,6,1,4,1,12740,26,1,1,1,4),_EqlReplPartnerTestAction_Type())
eqlReplPartnerTestAction.setMaxAccess(_D)
if mibBuilder.loadTexts:eqlReplPartnerTestAction.setStatus(_A)
class _EqlReplPartnerTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),('in-progress',1),('complete',2),('error',3),('restarted',4)))
_EqlReplPartnerTestState_Type.__name__=_B
_EqlReplPartnerTestState_Object=MibTableColumn
eqlReplPartnerTestState=_EqlReplPartnerTestState_Object((1,3,6,1,4,1,12740,26,1,1,1,5),_EqlReplPartnerTestState_Type())
eqlReplPartnerTestState.setMaxAccess(_D)
if mibBuilder.loadTexts:eqlReplPartnerTestState.setStatus(_A)
class _EqlReplPartnerTestMajorVersion_Type(Integer32):defaultValue=0
_EqlReplPartnerTestMajorVersion_Type.__name__=_B
_EqlReplPartnerTestMajorVersion_Object=MibTableColumn
eqlReplPartnerTestMajorVersion=_EqlReplPartnerTestMajorVersion_Object((1,3,6,1,4,1,12740,26,1,1,1,6),_EqlReplPartnerTestMajorVersion_Type())
eqlReplPartnerTestMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlReplPartnerTestMajorVersion.setStatus(_A)
class _EqlReplPartnerTestMinorVersion_Type(Integer32):defaultValue=0
_EqlReplPartnerTestMinorVersion_Type.__name__=_B
_EqlReplPartnerTestMinorVersion_Object=MibTableColumn
eqlReplPartnerTestMinorVersion=_EqlReplPartnerTestMinorVersion_Object((1,3,6,1,4,1,12740,26,1,1,1,7),_EqlReplPartnerTestMinorVersion_Type())
eqlReplPartnerTestMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlReplPartnerTestMinorVersion.setStatus(_A)
class _EqlReplPartnerTestMaintVersion_Type(Integer32):defaultValue=0
_EqlReplPartnerTestMaintVersion_Type.__name__=_B
_EqlReplPartnerTestMaintVersion_Object=MibTableColumn
eqlReplPartnerTestMaintVersion=_EqlReplPartnerTestMaintVersion_Object((1,3,6,1,4,1,12740,26,1,1,1,8),_EqlReplPartnerTestMaintVersion_Type())
eqlReplPartnerTestMaintVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlReplPartnerTestMaintVersion.setStatus(_A)
_EqlReplPartnerTestDelegatedSpace_Type=Counter64
_EqlReplPartnerTestDelegatedSpace_Object=MibTableColumn
eqlReplPartnerTestDelegatedSpace=_EqlReplPartnerTestDelegatedSpace_Object((1,3,6,1,4,1,12740,26,1,1,1,9),_EqlReplPartnerTestDelegatedSpace_Type())
eqlReplPartnerTestDelegatedSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlReplPartnerTestDelegatedSpace.setStatus(_A)
_EqlReplPartnerTestDelegatedSpaceUsed_Type=Counter64
_EqlReplPartnerTestDelegatedSpaceUsed_Object=MibTableColumn
eqlReplPartnerTestDelegatedSpaceUsed=_EqlReplPartnerTestDelegatedSpaceUsed_Object((1,3,6,1,4,1,12740,26,1,1,1,10),_EqlReplPartnerTestDelegatedSpaceUsed_Type())
eqlReplPartnerTestDelegatedSpaceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlReplPartnerTestDelegatedSpaceUsed.setStatus(_A)
_EqlReplPartnerTestTimestamp_Type=Counter32
_EqlReplPartnerTestTimestamp_Object=MibTableColumn
eqlReplPartnerTestTimestamp=_EqlReplPartnerTestTimestamp_Object((1,3,6,1,4,1,12740,26,1,1,1,11),_EqlReplPartnerTestTimestamp_Type())
eqlReplPartnerTestTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlReplPartnerTestTimestamp.setStatus(_A)
mibBuilder.exportSymbols('EQLREPLPARTNER-MIB',**{'EqlReplPartnerTestStatus':EqlReplPartnerTestStatus,'eqlReplPartnerModule':eqlReplPartnerModule,'eqlReplPartnerObjects':eqlReplPartnerObjects,'eqlReplPartnerTestTable':eqlReplPartnerTestTable,'eqlReplPartnerTestEntry':eqlReplPartnerTestEntry,'eqlReplPartnerTestRowStatus':eqlReplPartnerTestRowStatus,'eqlReplPartnerTestIPAddrStatus':eqlReplPartnerTestIPAddrStatus,'eqlReplPartnerTestAuthStatus':eqlReplPartnerTestAuthStatus,'eqlReplPartnerTestAction':eqlReplPartnerTestAction,'eqlReplPartnerTestState':eqlReplPartnerTestState,'eqlReplPartnerTestMajorVersion':eqlReplPartnerTestMajorVersion,'eqlReplPartnerTestMinorVersion':eqlReplPartnerTestMinorVersion,'eqlReplPartnerTestMaintVersion':eqlReplPartnerTestMaintVersion,'eqlReplPartnerTestDelegatedSpace':eqlReplPartnerTestDelegatedSpace,'eqlReplPartnerTestDelegatedSpaceUsed':eqlReplPartnerTestDelegatedSpaceUsed,'eqlReplPartnerTestTimestamp':eqlReplPartnerTestTimestamp})