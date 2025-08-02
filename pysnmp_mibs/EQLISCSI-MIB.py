_J='eqliscsiSessionAttributesEntry'
_I='eqliscsiSessionStatsEntry'
_H='deprecated'
_G='Unsigned32'
_F='Integer32'
_E='OctetString'
_D='EQLISCSI-MIB'
_C='Opaque'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
equalLogic,=mibBuilder.importSymbols('EQUALLOGIC-SMI','equalLogic')
iscsiSessionAttributesEntry,iscsiSessionStatsEntry=mibBuilder.importSymbols('ISCSI-MIB','iscsiSessionAttributesEntry','iscsiSessionStatsEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_C,'TimeTicks',_G,'enterprises','experimental','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
eqliscsiExtModule=ModuleIdentity((1,3,6,1,4,1,12740,11))
if mibBuilder.loadTexts:eqliscsiExtModule.setRevisions(('2002-06-26 00:00',))
_EqliscsiExtObjects_ObjectIdentity=ObjectIdentity
eqliscsiExtObjects=_EqliscsiExtObjects_ObjectIdentity((1,3,6,1,4,1,12740,11,1))
_EqliscsiSessionStatsTable_Object=MibTable
eqliscsiSessionStatsTable=_EqliscsiSessionStatsTable_Object((1,3,6,1,4,1,12740,11,1,1))
if mibBuilder.loadTexts:eqliscsiSessionStatsTable.setStatus(_A)
_EqliscsiSessionStatsEntry_Object=MibTableRow
eqliscsiSessionStatsEntry=_EqliscsiSessionStatsEntry_Object((1,3,6,1,4,1,12740,11,1,1,1))
if mibBuilder.loadTexts:eqliscsiSessionStatsEntry.setStatus(_A)
_EqliscsiSsnErrorCount_Type=Counter32
_EqliscsiSsnErrorCount_Object=MibTableColumn
eqliscsiSsnErrorCount=_EqliscsiSsnErrorCount_Object((1,3,6,1,4,1,12740,11,1,1,1,1),_EqliscsiSsnErrorCount_Type())
eqliscsiSsnErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eqliscsiSsnErrorCount.setStatus(_A)
_EqliscsiSsnTimeUp_Type=Counter32
_EqliscsiSsnTimeUp_Object=MibTableColumn
eqliscsiSsnTimeUp=_EqliscsiSsnTimeUp_Object((1,3,6,1,4,1,12740,11,1,1,1,2),_EqliscsiSsnTimeUp_Type())
eqliscsiSsnTimeUp.setMaxAccess(_B)
if mibBuilder.loadTexts:eqliscsiSsnTimeUp.setStatus(_A)
_EqliscsiSsnTotalDataTrnsfrd_Type=Counter32
_EqliscsiSsnTotalDataTrnsfrd_Object=MibTableColumn
eqliscsiSsnTotalDataTrnsfrd=_EqliscsiSsnTotalDataTrnsfrd_Object((1,3,6,1,4,1,12740,11,1,1,1,3),_EqliscsiSsnTotalDataTrnsfrd_Type())
eqliscsiSsnTotalDataTrnsfrd.setMaxAccess(_B)
if mibBuilder.loadTexts:eqliscsiSsnTotalDataTrnsfrd.setStatus(_H)
if mibBuilder.loadTexts:eqliscsiSsnTotalDataTrnsfrd.setUnits('KB')
class _EqliscsiNodeUuid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_EqliscsiNodeUuid_Type.__name__=_E
_EqliscsiNodeUuid_Object=MibTableColumn
eqliscsiNodeUuid=_EqliscsiNodeUuid_Object((1,3,6,1,4,1,12740,11,1,1,1,4),_EqliscsiNodeUuid_Type())
eqliscsiNodeUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:eqliscsiNodeUuid.setStatus(_A)
_EqliscsiSsnTotalDataTrnsfrd64_Type=Counter64
_EqliscsiSsnTotalDataTrnsfrd64_Object=MibTableColumn
eqliscsiSsnTotalDataTrnsfrd64=_EqliscsiSsnTotalDataTrnsfrd64_Object((1,3,6,1,4,1,12740,11,1,1,1,5),_EqliscsiSsnTotalDataTrnsfrd64_Type())
eqliscsiSsnTotalDataTrnsfrd64.setMaxAccess(_B)
if mibBuilder.loadTexts:eqliscsiSsnTotalDataTrnsfrd64.setStatus(_H)
if mibBuilder.loadTexts:eqliscsiSsnTotalDataTrnsfrd64.setUnits('KB')
class _EqliscsiSsnMembers_Type(Opaque):subtypeSpec=Opaque.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_EqliscsiSsnMembers_Type.__name__=_C
_EqliscsiSsnMembers_Object=MibTableColumn
eqliscsiSsnMembers=_EqliscsiSsnMembers_Object((1,3,6,1,4,1,12740,11,1,1,1,6),_EqliscsiSsnMembers_Type())
eqliscsiSsnMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:eqliscsiSsnMembers.setStatus(_A)
class _EqliscsiSsnRouteStats_Type(Opaque):subtypeSpec=Opaque.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_EqliscsiSsnRouteStats_Type.__name__=_C
_EqliscsiSsnRouteStats_Object=MibTableColumn
eqliscsiSsnRouteStats=_EqliscsiSsnRouteStats_Object((1,3,6,1,4,1,12740,11,1,1,1,7),_EqliscsiSsnRouteStats_Type())
eqliscsiSsnRouteStats.setMaxAccess(_B)
if mibBuilder.loadTexts:eqliscsiSsnRouteStats.setStatus(_A)
class _EqliscsiSsnLoadValue_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EqliscsiSsnLoadValue_Type.__name__=_G
_EqliscsiSsnLoadValue_Object=MibTableColumn
eqliscsiSsnLoadValue=_EqliscsiSsnLoadValue_Object((1,3,6,1,4,1,12740,11,1,1,1,8),_EqliscsiSsnLoadValue_Type())
eqliscsiSsnLoadValue.setMaxAccess(_B)
if mibBuilder.loadTexts:eqliscsiSsnLoadValue.setStatus(_A)
_EqliscsiSessionAttributesTable_Object=MibTable
eqliscsiSessionAttributesTable=_EqliscsiSessionAttributesTable_Object((1,3,6,1,4,1,12740,11,1,2))
if mibBuilder.loadTexts:eqliscsiSessionAttributesTable.setStatus(_A)
_EqliscsiSessionAttributesEntry_Object=MibTableRow
eqliscsiSessionAttributesEntry=_EqliscsiSessionAttributesEntry_Object((1,3,6,1,4,1,12740,11,1,2,1))
if mibBuilder.loadTexts:eqliscsiSessionAttributesEntry.setStatus(_A)
class _EqliscsiSessionAttributesType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('external',1),('syncrepl',2),('xcopy',3),('replica',4)))
_EqliscsiSessionAttributesType_Type.__name__=_F
_EqliscsiSessionAttributesType_Object=MibTableColumn
eqliscsiSessionAttributesType=_EqliscsiSessionAttributesType_Object((1,3,6,1,4,1,12740,11,1,2,1,1),_EqliscsiSessionAttributesType_Type())
eqliscsiSessionAttributesType.setMaxAccess(_B)
if mibBuilder.loadTexts:eqliscsiSessionAttributesType.setStatus(_A)
iscsiSessionStatsEntry.registerAugmentions((_D,_I))
eqliscsiSessionStatsEntry.setIndexNames(*iscsiSessionStatsEntry.getIndexNames())
iscsiSessionAttributesEntry.registerAugmentions((_D,_J))
eqliscsiSessionAttributesEntry.setIndexNames(*iscsiSessionAttributesEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'eqliscsiExtModule':eqliscsiExtModule,'eqliscsiExtObjects':eqliscsiExtObjects,'eqliscsiSessionStatsTable':eqliscsiSessionStatsTable,_I:eqliscsiSessionStatsEntry,'eqliscsiSsnErrorCount':eqliscsiSsnErrorCount,'eqliscsiSsnTimeUp':eqliscsiSsnTimeUp,'eqliscsiSsnTotalDataTrnsfrd':eqliscsiSsnTotalDataTrnsfrd,'eqliscsiNodeUuid':eqliscsiNodeUuid,'eqliscsiSsnTotalDataTrnsfrd64':eqliscsiSsnTotalDataTrnsfrd64,'eqliscsiSsnMembers':eqliscsiSsnMembers,'eqliscsiSsnRouteStats':eqliscsiSsnRouteStats,'eqliscsiSsnLoadValue':eqliscsiSsnLoadValue,'eqliscsiSessionAttributesTable':eqliscsiSessionAttributesTable,_J:eqliscsiSessionAttributesEntry,'eqliscsiSessionAttributesType':eqliscsiSessionAttributesType})