_F='ibBindZonePlusViewName'
_E='ibBindViewName'
_D='ibBindZoneName'
_C='IB-DNSONE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IbString,ibDNSOne=mibBuilder.importSymbols('IB-SMI-MIB','IbString','ibDNSOne')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ibDnsModule=ModuleIdentity((1,3,6,1,4,1,7779,3,1,1,3,1))
if mibBuilder.loadTexts:ibDnsModule.setRevisions(('2010-03-23 00:00','2005-06-09 00:00','2005-01-10 00:00','2004-05-21 00:00'))
_IbZoneStatisticsTable_Object=MibTable
ibZoneStatisticsTable=_IbZoneStatisticsTable_Object((1,3,6,1,4,1,7779,3,1,1,3,1,1))
if mibBuilder.loadTexts:ibZoneStatisticsTable.setStatus(_A)
_IbZoneStatisticsEntry_Object=MibTableRow
ibZoneStatisticsEntry=_IbZoneStatisticsEntry_Object((1,3,6,1,4,1,7779,3,1,1,3,1,1,1))
ibZoneStatisticsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ibZoneStatisticsEntry.setStatus(_A)
_IbBindZoneName_Type=IbString
_IbBindZoneName_Object=MibTableColumn
ibBindZoneName=_IbBindZoneName_Object((1,3,6,1,4,1,7779,3,1,1,3,1,1,1,1),_IbBindZoneName_Type())
ibBindZoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZoneName.setStatus(_A)
_IbBindZoneSuccess_Type=Counter64
_IbBindZoneSuccess_Object=MibTableColumn
ibBindZoneSuccess=_IbBindZoneSuccess_Object((1,3,6,1,4,1,7779,3,1,1,3,1,1,1,2),_IbBindZoneSuccess_Type())
ibBindZoneSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZoneSuccess.setStatus(_A)
_IbBindZoneReferral_Type=Counter64
_IbBindZoneReferral_Object=MibTableColumn
ibBindZoneReferral=_IbBindZoneReferral_Object((1,3,6,1,4,1,7779,3,1,1,3,1,1,1,3),_IbBindZoneReferral_Type())
ibBindZoneReferral.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZoneReferral.setStatus(_A)
_IbBindZoneNxRRset_Type=Counter64
_IbBindZoneNxRRset_Object=MibTableColumn
ibBindZoneNxRRset=_IbBindZoneNxRRset_Object((1,3,6,1,4,1,7779,3,1,1,3,1,1,1,4),_IbBindZoneNxRRset_Type())
ibBindZoneNxRRset.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZoneNxRRset.setStatus(_A)
_IbBindZoneNxDomain_Type=Counter64
_IbBindZoneNxDomain_Object=MibTableColumn
ibBindZoneNxDomain=_IbBindZoneNxDomain_Object((1,3,6,1,4,1,7779,3,1,1,3,1,1,1,5),_IbBindZoneNxDomain_Type())
ibBindZoneNxDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZoneNxDomain.setStatus(_A)
_IbBindZoneRecursion_Type=Counter64
_IbBindZoneRecursion_Object=MibTableColumn
ibBindZoneRecursion=_IbBindZoneRecursion_Object((1,3,6,1,4,1,7779,3,1,1,3,1,1,1,6),_IbBindZoneRecursion_Type())
ibBindZoneRecursion.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZoneRecursion.setStatus(_A)
_IbBindZoneFailure_Type=Counter64
_IbBindZoneFailure_Object=MibTableColumn
ibBindZoneFailure=_IbBindZoneFailure_Object((1,3,6,1,4,1,7779,3,1,1,3,1,1,1,7),_IbBindZoneFailure_Type())
ibBindZoneFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZoneFailure.setStatus(_A)
_IbZonePlusViewStatisticsTable_Object=MibTable
ibZonePlusViewStatisticsTable=_IbZonePlusViewStatisticsTable_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2))
if mibBuilder.loadTexts:ibZonePlusViewStatisticsTable.setStatus(_A)
_IbZonePlusViewStatisticsEntry_Object=MibTableRow
ibZonePlusViewStatisticsEntry=_IbZonePlusViewStatisticsEntry_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2,1))
ibZonePlusViewStatisticsEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:ibZonePlusViewStatisticsEntry.setStatus(_A)
_IbBindZonePlusViewName_Type=IbString
_IbBindZonePlusViewName_Object=MibTableColumn
ibBindZonePlusViewName=_IbBindZonePlusViewName_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2,1,1),_IbBindZonePlusViewName_Type())
ibBindZonePlusViewName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZonePlusViewName.setStatus(_A)
_IbBindZonePlusViewSuccess_Type=Counter64
_IbBindZonePlusViewSuccess_Object=MibTableColumn
ibBindZonePlusViewSuccess=_IbBindZonePlusViewSuccess_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2,1,2),_IbBindZonePlusViewSuccess_Type())
ibBindZonePlusViewSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZonePlusViewSuccess.setStatus(_A)
_IbBindZonePlusViewReferral_Type=Counter64
_IbBindZonePlusViewReferral_Object=MibTableColumn
ibBindZonePlusViewReferral=_IbBindZonePlusViewReferral_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2,1,3),_IbBindZonePlusViewReferral_Type())
ibBindZonePlusViewReferral.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZonePlusViewReferral.setStatus(_A)
_IbBindZonePlusViewNxRRset_Type=Counter64
_IbBindZonePlusViewNxRRset_Object=MibTableColumn
ibBindZonePlusViewNxRRset=_IbBindZonePlusViewNxRRset_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2,1,4),_IbBindZonePlusViewNxRRset_Type())
ibBindZonePlusViewNxRRset.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZonePlusViewNxRRset.setStatus(_A)
_IbBindZonePlusViewNxDomain_Type=Counter64
_IbBindZonePlusViewNxDomain_Object=MibTableColumn
ibBindZonePlusViewNxDomain=_IbBindZonePlusViewNxDomain_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2,1,5),_IbBindZonePlusViewNxDomain_Type())
ibBindZonePlusViewNxDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZonePlusViewNxDomain.setStatus(_A)
_IbBindZonePlusViewRecursion_Type=Counter64
_IbBindZonePlusViewRecursion_Object=MibTableColumn
ibBindZonePlusViewRecursion=_IbBindZonePlusViewRecursion_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2,1,6),_IbBindZonePlusViewRecursion_Type())
ibBindZonePlusViewRecursion.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZonePlusViewRecursion.setStatus(_A)
_IbBindZonePlusViewFailure_Type=Counter64
_IbBindZonePlusViewFailure_Object=MibTableColumn
ibBindZonePlusViewFailure=_IbBindZonePlusViewFailure_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2,1,7),_IbBindZonePlusViewFailure_Type())
ibBindZonePlusViewFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZonePlusViewFailure.setStatus(_A)
_IbBindViewName_Type=IbString
_IbBindViewName_Object=MibTableColumn
ibBindViewName=_IbBindViewName_Object((1,3,6,1,4,1,7779,3,1,1,3,1,2,1,8),_IbBindViewName_Type())
ibBindViewName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindViewName.setStatus(_A)
_IbDDNSUpdateStatistics_ObjectIdentity=ObjectIdentity
ibDDNSUpdateStatistics=_IbDDNSUpdateStatistics_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,3,1,3))
_IbDDNSUpdateSuccess_Type=Counter64
_IbDDNSUpdateSuccess_Object=MibScalar
ibDDNSUpdateSuccess=_IbDDNSUpdateSuccess_Object((1,3,6,1,4,1,7779,3,1,1,3,1,3,1),_IbDDNSUpdateSuccess_Type())
ibDDNSUpdateSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ibDDNSUpdateSuccess.setStatus(_A)
_IbDDNSUpdateFailure_Type=Counter64
_IbDDNSUpdateFailure_Object=MibScalar
ibDDNSUpdateFailure=_IbDDNSUpdateFailure_Object((1,3,6,1,4,1,7779,3,1,1,3,1,3,2),_IbDDNSUpdateFailure_Type())
ibDDNSUpdateFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ibDDNSUpdateFailure.setStatus(_A)
_IbDDNSUpdateReject_Type=Counter64
_IbDDNSUpdateReject_Object=MibScalar
ibDDNSUpdateReject=_IbDDNSUpdateReject_Object((1,3,6,1,4,1,7779,3,1,1,3,1,3,3),_IbDDNSUpdateReject_Type())
ibDDNSUpdateReject.setMaxAccess(_B)
if mibBuilder.loadTexts:ibDDNSUpdateReject.setStatus(_A)
_IbDDNSUpdatePrerequisiteReject_Type=Counter64
_IbDDNSUpdatePrerequisiteReject_Object=MibScalar
ibDDNSUpdatePrerequisiteReject=_IbDDNSUpdatePrerequisiteReject_Object((1,3,6,1,4,1,7779,3,1,1,3,1,3,4),_IbDDNSUpdatePrerequisiteReject_Type())
ibDDNSUpdatePrerequisiteReject.setMaxAccess(_B)
if mibBuilder.loadTexts:ibDDNSUpdatePrerequisiteReject.setStatus(_A)
_IbBindZoneTransferCount_Type=Counter64
_IbBindZoneTransferCount_Object=MibScalar
ibBindZoneTransferCount=_IbBindZoneTransferCount_Object((1,3,6,1,4,1,7779,3,1,1,3,1,4),_IbBindZoneTransferCount_Type())
ibBindZoneTransferCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ibBindZoneTransferCount.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ibDnsModule':ibDnsModule,'ibZoneStatisticsTable':ibZoneStatisticsTable,'ibZoneStatisticsEntry':ibZoneStatisticsEntry,_D:ibBindZoneName,'ibBindZoneSuccess':ibBindZoneSuccess,'ibBindZoneReferral':ibBindZoneReferral,'ibBindZoneNxRRset':ibBindZoneNxRRset,'ibBindZoneNxDomain':ibBindZoneNxDomain,'ibBindZoneRecursion':ibBindZoneRecursion,'ibBindZoneFailure':ibBindZoneFailure,'ibZonePlusViewStatisticsTable':ibZonePlusViewStatisticsTable,'ibZonePlusViewStatisticsEntry':ibZonePlusViewStatisticsEntry,_F:ibBindZonePlusViewName,'ibBindZonePlusViewSuccess':ibBindZonePlusViewSuccess,'ibBindZonePlusViewReferral':ibBindZonePlusViewReferral,'ibBindZonePlusViewNxRRset':ibBindZonePlusViewNxRRset,'ibBindZonePlusViewNxDomain':ibBindZonePlusViewNxDomain,'ibBindZonePlusViewRecursion':ibBindZonePlusViewRecursion,'ibBindZonePlusViewFailure':ibBindZonePlusViewFailure,_E:ibBindViewName,'ibDDNSUpdateStatistics':ibDDNSUpdateStatistics,'ibDDNSUpdateSuccess':ibDDNSUpdateSuccess,'ibDDNSUpdateFailure':ibDDNSUpdateFailure,'ibDDNSUpdateReject':ibDDNSUpdateReject,'ibDDNSUpdatePrerequisiteReject':ibDDNSUpdatePrerequisiteReject,'ibBindZoneTransferCount':ibBindZoneTransferCount})