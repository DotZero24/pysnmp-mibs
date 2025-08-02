_L='ciscoMrpMIBNotificationGroup'
_K='ciscoMrpMIBMainObjectGroup'
_J='ciscoMrpRingOpen'
_I='ciscoMrpDomainIndex'
_H='Unsigned32'
_G='OctetString'
_F='ciscoMrpDomainState'
_E='ciscoMrpDomainName'
_D='ciscoMrpDomainID'
_C='read-only'
_B='current'
_A='CISCO-MRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMrpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,850))
if mibBuilder.loadTexts:ciscoMrpMIB.setRevisions(('2017-09-12 00:00',))
_CiscoMrpMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoMrpMIBNotifs=_CiscoMrpMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,850,0))
_CiscoMrpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoMrpMIBObjects=_CiscoMrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,850,1))
_CiscoMrpDomainTable_Object=MibTable
ciscoMrpDomainTable=_CiscoMrpDomainTable_Object((1,3,6,1,4,1,9,9,850,1,1))
if mibBuilder.loadTexts:ciscoMrpDomainTable.setStatus(_B)
_CiscoMrpDomainEntry_Object=MibTableRow
ciscoMrpDomainEntry=_CiscoMrpDomainEntry_Object((1,3,6,1,4,1,9,9,850,1,1,1))
ciscoMrpDomainEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ciscoMrpDomainEntry.setStatus(_B)
_CiscoMrpDomainIndex_Type=Unsigned32
_CiscoMrpDomainIndex_Object=MibTableColumn
ciscoMrpDomainIndex=_CiscoMrpDomainIndex_Object((1,3,6,1,4,1,9,9,850,1,1,1,1),_CiscoMrpDomainIndex_Type())
ciscoMrpDomainIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoMrpDomainIndex.setStatus(_B)
class _CiscoMrpDomainID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CiscoMrpDomainID_Type.__name__=_G
_CiscoMrpDomainID_Object=MibTableColumn
ciscoMrpDomainID=_CiscoMrpDomainID_Object((1,3,6,1,4,1,9,9,850,1,1,1,2),_CiscoMrpDomainID_Type())
ciscoMrpDomainID.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMrpDomainID.setStatus(_B)
_CiscoMrpDomainName_Type=DisplayString
_CiscoMrpDomainName_Object=MibTableColumn
ciscoMrpDomainName=_CiscoMrpDomainName_Object((1,3,6,1,4,1,9,9,850,1,1,1,3),_CiscoMrpDomainName_Type())
ciscoMrpDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMrpDomainName.setStatus(_B)
class _CiscoMrpDomainState_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CiscoMrpDomainState_Type.__name__=_H
_CiscoMrpDomainState_Object=MibTableColumn
ciscoMrpDomainState=_CiscoMrpDomainState_Object((1,3,6,1,4,1,9,9,850,1,1,1,4),_CiscoMrpDomainState_Type())
ciscoMrpDomainState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMrpDomainState.setStatus(_B)
_CiscoMrpMIBConform_ObjectIdentity=ObjectIdentity
ciscoMrpMIBConform=_CiscoMrpMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,850,2))
_CiscoMrpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoMrpMIBCompliances=_CiscoMrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,850,2,1))
_CiscoMrpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoMrpMIBGroups=_CiscoMrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,850,2,2))
ciscoMrpMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,850,2,2,1))
ciscoMrpMIBMainObjectGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ciscoMrpMIBMainObjectGroup.setStatus(_B)
ciscoMrpRingOpen=NotificationType((1,3,6,1,4,1,9,9,850,0,1))
ciscoMrpRingOpen.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ciscoMrpRingOpen.setStatus(_B)
ciscoMrpMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,850,2,2,2))
ciscoMrpMIBNotificationGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:ciscoMrpMIBNotificationGroup.setStatus(_B)
ciscoMrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,850,2,1,1))
ciscoMrpMIBCompliance.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoMrpMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoMrpMIB':ciscoMrpMIB,'ciscoMrpMIBNotifs':ciscoMrpMIBNotifs,_J:ciscoMrpRingOpen,'ciscoMrpMIBObjects':ciscoMrpMIBObjects,'ciscoMrpDomainTable':ciscoMrpDomainTable,'ciscoMrpDomainEntry':ciscoMrpDomainEntry,_I:ciscoMrpDomainIndex,_D:ciscoMrpDomainID,_E:ciscoMrpDomainName,_F:ciscoMrpDomainState,'ciscoMrpMIBConform':ciscoMrpMIBConform,'ciscoMrpMIBCompliances':ciscoMrpMIBCompliances,'ciscoMrpMIBCompliance':ciscoMrpMIBCompliance,'ciscoMrpMIBGroups':ciscoMrpMIBGroups,_K:ciscoMrpMIBMainObjectGroup,_L:ciscoMrpMIBNotificationGroup})