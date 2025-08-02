_K='cuctTapStreamComplianceGroup'
_J='cuctTapStreamStatus'
_I='cuctTapStreamAcctSessID'
_H='cuctTapStreamCapabilities'
_G='read-create'
_F='Unsigned32'
_E='cTap2StreamIndex'
_D='cTap2MediationContentId'
_C='CISCO-TAP2-MIB'
_B='CISCO-USER-CONNECTION-TAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
cTap2MediationContentId,cTap2StreamIndex=mibBuilder.importSymbols(_C,_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoUserConnectionTapMIB=ModuleIdentity((1,3,6,1,4,1,9,9,400))
if mibBuilder.loadTexts:ciscoUserConnectionTapMIB.setRevisions(('2007-08-09 00:00','2004-03-11 00:00'))
_CUserConnectionTapMIBObjects_ObjectIdentity=ObjectIdentity
cUserConnectionTapMIBObjects=_CUserConnectionTapMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,400,1))
_CuctTapStreamEncodePacket_ObjectIdentity=ObjectIdentity
cuctTapStreamEncodePacket=_CuctTapStreamEncodePacket_ObjectIdentity((1,3,6,1,4,1,9,9,400,1,1))
class _CuctTapStreamCapabilities_Type(Bits):namedValues=NamedValues(*(('tapEnable',0),('acctSessionId',1)))
_CuctTapStreamCapabilities_Type.__name__='Bits'
_CuctTapStreamCapabilities_Object=MibScalar
cuctTapStreamCapabilities=_CuctTapStreamCapabilities_Object((1,3,6,1,4,1,9,9,400,1,1,1),_CuctTapStreamCapabilities_Type())
cuctTapStreamCapabilities.setMaxAccess('read-only')
if mibBuilder.loadTexts:cuctTapStreamCapabilities.setStatus(_A)
_CuctTapStreamTable_Object=MibTable
cuctTapStreamTable=_CuctTapStreamTable_Object((1,3,6,1,4,1,9,9,400,1,1,2))
if mibBuilder.loadTexts:cuctTapStreamTable.setStatus(_A)
_CuctTapStreamEntry_Object=MibTableRow
cuctTapStreamEntry=_CuctTapStreamEntry_Object((1,3,6,1,4,1,9,9,400,1,1,2,1))
cuctTapStreamEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:cuctTapStreamEntry.setStatus(_A)
class _CuctTapStreamAcctSessID_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CuctTapStreamAcctSessID_Type.__name__=_F
_CuctTapStreamAcctSessID_Object=MibTableColumn
cuctTapStreamAcctSessID=_CuctTapStreamAcctSessID_Object((1,3,6,1,4,1,9,9,400,1,1,2,1,1),_CuctTapStreamAcctSessID_Type())
cuctTapStreamAcctSessID.setMaxAccess(_G)
if mibBuilder.loadTexts:cuctTapStreamAcctSessID.setStatus(_A)
_CuctTapStreamStatus_Type=RowStatus
_CuctTapStreamStatus_Object=MibTableColumn
cuctTapStreamStatus=_CuctTapStreamStatus_Object((1,3,6,1,4,1,9,9,400,1,1,2,1,2),_CuctTapStreamStatus_Type())
cuctTapStreamStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cuctTapStreamStatus.setStatus(_A)
_CUserConnectionTapMIBConform_ObjectIdentity=ObjectIdentity
cUserConnectionTapMIBConform=_CUserConnectionTapMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,400,2))
_CUserConnectionTapMIBCompliances_ObjectIdentity=ObjectIdentity
cUserConnectionTapMIBCompliances=_CUserConnectionTapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,400,2,1))
_CUserConnectionTapMIBGroups_ObjectIdentity=ObjectIdentity
cUserConnectionTapMIBGroups=_CUserConnectionTapMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,400,2,2))
cuctTapStreamComplianceGroup=ObjectGroup((1,3,6,1,4,1,9,9,400,2,2,1))
cuctTapStreamComplianceGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cuctTapStreamComplianceGroup.setStatus(_A)
cUserConnectionTapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,400,2,1,1))
cUserConnectionTapMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:cUserConnectionTapMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoUserConnectionTapMIB':ciscoUserConnectionTapMIB,'cUserConnectionTapMIBObjects':cUserConnectionTapMIBObjects,'cuctTapStreamEncodePacket':cuctTapStreamEncodePacket,_H:cuctTapStreamCapabilities,'cuctTapStreamTable':cuctTapStreamTable,'cuctTapStreamEntry':cuctTapStreamEntry,_I:cuctTapStreamAcctSessID,_J:cuctTapStreamStatus,'cUserConnectionTapMIBConform':cUserConnectionTapMIBConform,'cUserConnectionTapMIBCompliances':cUserConnectionTapMIBCompliances,'cUserConnectionTapMIBCompliance':cUserConnectionTapMIBCompliance,'cUserConnectionTapMIBGroups':cUserConnectionTapMIBGroups,_K:cuctTapStreamComplianceGroup})