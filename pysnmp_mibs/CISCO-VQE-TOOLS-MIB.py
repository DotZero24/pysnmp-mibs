_H='ciscoVqeToolsVcdsGroup'
_G='cvqtRequestRate'
_F='cvqtTotalSentResponses'
_E='cvqtTotalReceivedRequests'
_D='cvqtNumberOfSessions'
_C='read-only'
_B='CISCO-VQE-TOOLS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVqeToolsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,969))
if mibBuilder.loadTexts:ciscoVqeToolsMIB.setRevisions(('2009-12-18 13:41',))
_CiscoVqeToolsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVqeToolsMIBNotifs=_CiscoVqeToolsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,969,0))
_CiscoVqeToolsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVqeToolsMIBObjects=_CiscoVqeToolsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,969,1))
_CvqtVcdsInfo_ObjectIdentity=ObjectIdentity
cvqtVcdsInfo=_CvqtVcdsInfo_ObjectIdentity((1,3,6,1,4,1,9,9,969,1,1))
_CvqtNumberOfSessions_Type=Gauge32
_CvqtNumberOfSessions_Object=MibScalar
cvqtNumberOfSessions=_CvqtNumberOfSessions_Object((1,3,6,1,4,1,9,9,969,1,1,1),_CvqtNumberOfSessions_Type())
cvqtNumberOfSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqtNumberOfSessions.setStatus(_A)
if mibBuilder.loadTexts:cvqtNumberOfSessions.setUnits('RTSP connections')
_CvqtTotalReceivedRequests_Type=Counter64
_CvqtTotalReceivedRequests_Object=MibScalar
cvqtTotalReceivedRequests=_CvqtTotalReceivedRequests_Object((1,3,6,1,4,1,9,9,969,1,1,2),_CvqtTotalReceivedRequests_Type())
cvqtTotalReceivedRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqtTotalReceivedRequests.setStatus(_A)
if mibBuilder.loadTexts:cvqtTotalReceivedRequests.setUnits('RTSP requests')
_CvqtTotalSentResponses_Type=Counter64
_CvqtTotalSentResponses_Object=MibScalar
cvqtTotalSentResponses=_CvqtTotalSentResponses_Object((1,3,6,1,4,1,9,9,969,1,1,3),_CvqtTotalSentResponses_Type())
cvqtTotalSentResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqtTotalSentResponses.setStatus(_A)
if mibBuilder.loadTexts:cvqtTotalSentResponses.setUnits('RTSP responses')
_CvqtRequestRate_Type=Gauge32
_CvqtRequestRate_Object=MibScalar
cvqtRequestRate=_CvqtRequestRate_Object((1,3,6,1,4,1,9,9,969,1,1,4),_CvqtRequestRate_Type())
cvqtRequestRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqtRequestRate.setStatus(_A)
if mibBuilder.loadTexts:cvqtRequestRate.setUnits('requests per second')
_CiscoVqeToolsMIBConform_ObjectIdentity=ObjectIdentity
ciscoVqeToolsMIBConform=_CiscoVqeToolsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,969,2))
_CvqtMIBCompliances_ObjectIdentity=ObjectIdentity
cvqtMIBCompliances=_CvqtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,969,2,1))
_CvqtMIBGroups_ObjectIdentity=ObjectIdentity
cvqtMIBGroups=_CvqtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,969,2,2))
ciscoVqeToolsVcdsGroup=ObjectGroup((1,3,6,1,4,1,9,9,969,2,2,1))
ciscoVqeToolsVcdsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ciscoVqeToolsVcdsGroup.setStatus(_A)
cvqtMIBReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,969,2,1,1))
cvqtMIBReadOnlyCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:cvqtMIBReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVqeToolsMIB':ciscoVqeToolsMIB,'ciscoVqeToolsMIBNotifs':ciscoVqeToolsMIBNotifs,'ciscoVqeToolsMIBObjects':ciscoVqeToolsMIBObjects,'cvqtVcdsInfo':cvqtVcdsInfo,_D:cvqtNumberOfSessions,_E:cvqtTotalReceivedRequests,_F:cvqtTotalSentResponses,_G:cvqtRequestRate,'ciscoVqeToolsMIBConform':ciscoVqeToolsMIBConform,'cvqtMIBCompliances':cvqtMIBCompliances,'cvqtMIBReadOnlyCompliance':cvqtMIBReadOnlyCompliance,'cvqtMIBGroups':cvqtMIBGroups,_H:ciscoVqeToolsVcdsGroup})