_S='etsysDiagnosticMessageGroup'
_R='etsysDiagnosticMessageDetailsStatus'
_Q='etsysDiagnosticMessageDetailsText'
_P='etsysDiagnosticMessageStatus'
_O='etsysDiagnosticMessageFWRevision'
_N='etsysDiagnosticMessageSummary'
_M='etsysDiagnosticMessageType'
_L='etsysDiagnosticMessageTime'
_K='etsysDiagnosticMessageChanges'
_J='etsysDiagnosticMessageCount'
_I='etsysDiagnosticMessageDetailsIndex'
_H='not-accessible'
_G='etsysDiagnosticMessageIndex'
_F='Unsigned32'
_E='Bits'
_D='SnmpAdminString'
_C='read-only'
_B='ENTERASYS-DIAGNOSTIC-MESSAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_E,'Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
etsysDiagnosticMessageMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,13))
if mibBuilder.loadTexts:etsysDiagnosticMessageMIB.setRevisions(('2003-01-10 21:17','2002-06-07 14:28','2001-12-03 19:51','2001-08-08 00:00'))
class LongAdminString(TextualConvention,OctetString):status=_A;displayHint='1024a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_EtsysDiagnosticMessage_ObjectIdentity=ObjectIdentity
etsysDiagnosticMessage=_EtsysDiagnosticMessage_ObjectIdentity((1,3,6,1,4,1,5624,1,2,13,1))
_EtsysDiagnosticMessageCount_Type=Counter32
_EtsysDiagnosticMessageCount_Object=MibScalar
etsysDiagnosticMessageCount=_EtsysDiagnosticMessageCount_Object((1,3,6,1,4,1,5624,1,2,13,1,1),_EtsysDiagnosticMessageCount_Type())
etsysDiagnosticMessageCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDiagnosticMessageCount.setStatus(_A)
_EtsysDiagnosticMessageChanges_Type=Counter32
_EtsysDiagnosticMessageChanges_Object=MibScalar
etsysDiagnosticMessageChanges=_EtsysDiagnosticMessageChanges_Object((1,3,6,1,4,1,5624,1,2,13,1,2),_EtsysDiagnosticMessageChanges_Type())
etsysDiagnosticMessageChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDiagnosticMessageChanges.setStatus(_A)
_EtsysDiagnosticMessageTable_Object=MibTable
etsysDiagnosticMessageTable=_EtsysDiagnosticMessageTable_Object((1,3,6,1,4,1,5624,1,2,13,1,3))
if mibBuilder.loadTexts:etsysDiagnosticMessageTable.setStatus(_A)
_EtsysDiagnosticMessageEntry_Object=MibTableRow
etsysDiagnosticMessageEntry=_EtsysDiagnosticMessageEntry_Object((1,3,6,1,4,1,5624,1,2,13,1,3,1))
etsysDiagnosticMessageEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:etsysDiagnosticMessageEntry.setStatus(_A)
class _EtsysDiagnosticMessageIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysDiagnosticMessageIndex_Type.__name__=_F
_EtsysDiagnosticMessageIndex_Object=MibTableColumn
etsysDiagnosticMessageIndex=_EtsysDiagnosticMessageIndex_Object((1,3,6,1,4,1,5624,1,2,13,1,3,1,1),_EtsysDiagnosticMessageIndex_Type())
etsysDiagnosticMessageIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysDiagnosticMessageIndex.setStatus(_A)
_EtsysDiagnosticMessageTime_Type=DateAndTime
_EtsysDiagnosticMessageTime_Object=MibTableColumn
etsysDiagnosticMessageTime=_EtsysDiagnosticMessageTime_Object((1,3,6,1,4,1,5624,1,2,13,1,3,1,2),_EtsysDiagnosticMessageTime_Type())
etsysDiagnosticMessageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDiagnosticMessageTime.setStatus(_A)
class _EtsysDiagnosticMessageType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EtsysDiagnosticMessageType_Type.__name__=_D
_EtsysDiagnosticMessageType_Object=MibTableColumn
etsysDiagnosticMessageType=_EtsysDiagnosticMessageType_Object((1,3,6,1,4,1,5624,1,2,13,1,3,1,3),_EtsysDiagnosticMessageType_Type())
etsysDiagnosticMessageType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDiagnosticMessageType.setStatus(_A)
class _EtsysDiagnosticMessageSummary_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_EtsysDiagnosticMessageSummary_Type.__name__=_D
_EtsysDiagnosticMessageSummary_Object=MibTableColumn
etsysDiagnosticMessageSummary=_EtsysDiagnosticMessageSummary_Object((1,3,6,1,4,1,5624,1,2,13,1,3,1,4),_EtsysDiagnosticMessageSummary_Type())
etsysDiagnosticMessageSummary.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDiagnosticMessageSummary.setStatus(_A)
class _EtsysDiagnosticMessageFWRevision_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EtsysDiagnosticMessageFWRevision_Type.__name__=_D
_EtsysDiagnosticMessageFWRevision_Object=MibTableColumn
etsysDiagnosticMessageFWRevision=_EtsysDiagnosticMessageFWRevision_Object((1,3,6,1,4,1,5624,1,2,13,1,3,1,5),_EtsysDiagnosticMessageFWRevision_Type())
etsysDiagnosticMessageFWRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDiagnosticMessageFWRevision.setStatus(_A)
class _EtsysDiagnosticMessageStatus_Type(Bits):namedValues=NamedValues(('etsysDiagnosticMessageBadChecksum',0))
_EtsysDiagnosticMessageStatus_Type.__name__=_E
_EtsysDiagnosticMessageStatus_Object=MibTableColumn
etsysDiagnosticMessageStatus=_EtsysDiagnosticMessageStatus_Object((1,3,6,1,4,1,5624,1,2,13,1,3,1,6),_EtsysDiagnosticMessageStatus_Type())
etsysDiagnosticMessageStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDiagnosticMessageStatus.setStatus(_A)
_EtsysDiagnosticMessageDetails_ObjectIdentity=ObjectIdentity
etsysDiagnosticMessageDetails=_EtsysDiagnosticMessageDetails_ObjectIdentity((1,3,6,1,4,1,5624,1,2,13,2))
_EtsysDiagnosticMessageDetailsTable_Object=MibTable
etsysDiagnosticMessageDetailsTable=_EtsysDiagnosticMessageDetailsTable_Object((1,3,6,1,4,1,5624,1,2,13,2,1))
if mibBuilder.loadTexts:etsysDiagnosticMessageDetailsTable.setStatus(_A)
_EtsysDiagnosticMessageDetailsEntry_Object=MibTableRow
etsysDiagnosticMessageDetailsEntry=_EtsysDiagnosticMessageDetailsEntry_Object((1,3,6,1,4,1,5624,1,2,13,2,1,1))
etsysDiagnosticMessageDetailsEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:etsysDiagnosticMessageDetailsEntry.setStatus(_A)
class _EtsysDiagnosticMessageDetailsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_EtsysDiagnosticMessageDetailsIndex_Type.__name__=_F
_EtsysDiagnosticMessageDetailsIndex_Object=MibTableColumn
etsysDiagnosticMessageDetailsIndex=_EtsysDiagnosticMessageDetailsIndex_Object((1,3,6,1,4,1,5624,1,2,13,2,1,1,1),_EtsysDiagnosticMessageDetailsIndex_Type())
etsysDiagnosticMessageDetailsIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysDiagnosticMessageDetailsIndex.setStatus(_A)
_EtsysDiagnosticMessageDetailsText_Type=LongAdminString
_EtsysDiagnosticMessageDetailsText_Object=MibTableColumn
etsysDiagnosticMessageDetailsText=_EtsysDiagnosticMessageDetailsText_Object((1,3,6,1,4,1,5624,1,2,13,2,1,1,2),_EtsysDiagnosticMessageDetailsText_Type())
etsysDiagnosticMessageDetailsText.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDiagnosticMessageDetailsText.setStatus(_A)
class _EtsysDiagnosticMessageDetailsStatus_Type(Bits):namedValues=NamedValues(('etsysDiagnosticMessageLastSegment',0))
_EtsysDiagnosticMessageDetailsStatus_Type.__name__=_E
_EtsysDiagnosticMessageDetailsStatus_Object=MibTableColumn
etsysDiagnosticMessageDetailsStatus=_EtsysDiagnosticMessageDetailsStatus_Object((1,3,6,1,4,1,5624,1,2,13,2,1,1,3),_EtsysDiagnosticMessageDetailsStatus_Type())
etsysDiagnosticMessageDetailsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDiagnosticMessageDetailsStatus.setStatus(_A)
_EtsysDiagnosticMessageConformance_ObjectIdentity=ObjectIdentity
etsysDiagnosticMessageConformance=_EtsysDiagnosticMessageConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,13,3))
_EtsysDiagnosticMessageGroups_ObjectIdentity=ObjectIdentity
etsysDiagnosticMessageGroups=_EtsysDiagnosticMessageGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,13,3,1))
_EtsysDiagnosticMessageCompliances_ObjectIdentity=ObjectIdentity
etsysDiagnosticMessageCompliances=_EtsysDiagnosticMessageCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,13,3,2))
etsysDiagnosticMessageGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,13,3,1,1))
etsysDiagnosticMessageGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:etsysDiagnosticMessageGroup.setStatus(_A)
etsysDiagnosticMessageCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,13,3,2,1))
etsysDiagnosticMessageCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:etsysDiagnosticMessageCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LongAdminString':LongAdminString,'etsysDiagnosticMessageMIB':etsysDiagnosticMessageMIB,'etsysDiagnosticMessage':etsysDiagnosticMessage,_J:etsysDiagnosticMessageCount,_K:etsysDiagnosticMessageChanges,'etsysDiagnosticMessageTable':etsysDiagnosticMessageTable,'etsysDiagnosticMessageEntry':etsysDiagnosticMessageEntry,_G:etsysDiagnosticMessageIndex,_L:etsysDiagnosticMessageTime,_M:etsysDiagnosticMessageType,_N:etsysDiagnosticMessageSummary,_O:etsysDiagnosticMessageFWRevision,_P:etsysDiagnosticMessageStatus,'etsysDiagnosticMessageDetails':etsysDiagnosticMessageDetails,'etsysDiagnosticMessageDetailsTable':etsysDiagnosticMessageDetailsTable,'etsysDiagnosticMessageDetailsEntry':etsysDiagnosticMessageDetailsEntry,_I:etsysDiagnosticMessageDetailsIndex,_Q:etsysDiagnosticMessageDetailsText,_R:etsysDiagnosticMessageDetailsStatus,'etsysDiagnosticMessageConformance':etsysDiagnosticMessageConformance,'etsysDiagnosticMessageGroups':etsysDiagnosticMessageGroups,_S:etsysDiagnosticMessageGroup,'etsysDiagnosticMessageCompliances':etsysDiagnosticMessageCompliances,'etsysDiagnosticMessageCompliance':etsysDiagnosticMessageCompliance})