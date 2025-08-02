_Y='ciscoBitsClockNotifGroup'
_X='ciscoBitsClockSourceGroup'
_W='ciscoBitsClockHoldover'
_V='ciscoBitsClockFreerun'
_U='ciscoBitsClockSource'
_T='cBitsClkNotifEnabled'
_S='cBitsClkSourceInactiveSeconds'
_R='cBitsClkSourceActiveSeconds'
_Q='cBitsClkSourceTimestamp'
_P='seconds'
_O='read-write'
_N='tertiary'
_M='secondary'
_L='primary'
_K='TruthValue'
_J='entPhysicalIndex'
_I='cBitsClkSourceDescription'
_H='cBitsClkSourceRoleCurrent'
_G='cBitsClkSourceRoleAdmin'
_F='Integer32'
_E='entPhysicalDescr'
_D='read-only'
_C='ENTITY-MIB'
_B='current'
_A='CISCO-BITS-CLOCK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalDescr,entPhysicalIndex=mibBuilder.importSymbols(_C,_E,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_K)
ciscoBitsClockMIB=ModuleIdentity((1,3,6,1,4,1,9,9,459))
if mibBuilder.loadTexts:ciscoBitsClockMIB.setRevisions(('2005-01-21 00:00',))
_CiscoBitsClockMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoBitsClockMIBNotifs=_CiscoBitsClockMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,459,0))
_CiscoBitsClockMIBObjects_ObjectIdentity=ObjectIdentity
ciscoBitsClockMIBObjects=_CiscoBitsClockMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,459,1))
_CBitsClkSourceTable_Object=MibTable
cBitsClkSourceTable=_CBitsClkSourceTable_Object((1,3,6,1,4,1,9,9,459,1,1))
if mibBuilder.loadTexts:cBitsClkSourceTable.setStatus(_B)
_CBitsClkSourceEntry_Object=MibTableRow
cBitsClkSourceEntry=_CBitsClkSourceEntry_Object((1,3,6,1,4,1,9,9,459,1,1,1))
cBitsClkSourceEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cBitsClkSourceEntry.setStatus(_B)
class _CBitsClkSourceRoleAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_CBitsClkSourceRoleAdmin_Type.__name__=_F
_CBitsClkSourceRoleAdmin_Object=MibTableColumn
cBitsClkSourceRoleAdmin=_CBitsClkSourceRoleAdmin_Object((1,3,6,1,4,1,9,9,459,1,1,1,1),_CBitsClkSourceRoleAdmin_Type())
cBitsClkSourceRoleAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:cBitsClkSourceRoleAdmin.setStatus(_B)
class _CBitsClkSourceRoleCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unavailable',0),(_L,1),(_M,2),(_N,3)))
_CBitsClkSourceRoleCurrent_Type.__name__=_F
_CBitsClkSourceRoleCurrent_Object=MibTableColumn
cBitsClkSourceRoleCurrent=_CBitsClkSourceRoleCurrent_Object((1,3,6,1,4,1,9,9,459,1,1,1,2),_CBitsClkSourceRoleCurrent_Type())
cBitsClkSourceRoleCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:cBitsClkSourceRoleCurrent.setStatus(_B)
_CBitsClkSourceTimestamp_Type=TimeStamp
_CBitsClkSourceTimestamp_Object=MibTableColumn
cBitsClkSourceTimestamp=_CBitsClkSourceTimestamp_Object((1,3,6,1,4,1,9,9,459,1,1,1,3),_CBitsClkSourceTimestamp_Type())
cBitsClkSourceTimestamp.setMaxAccess(_O)
if mibBuilder.loadTexts:cBitsClkSourceTimestamp.setStatus(_B)
_CBitsClkSourceActiveSeconds_Type=Counter32
_CBitsClkSourceActiveSeconds_Object=MibTableColumn
cBitsClkSourceActiveSeconds=_CBitsClkSourceActiveSeconds_Object((1,3,6,1,4,1,9,9,459,1,1,1,4),_CBitsClkSourceActiveSeconds_Type())
cBitsClkSourceActiveSeconds.setMaxAccess(_D)
if mibBuilder.loadTexts:cBitsClkSourceActiveSeconds.setStatus(_B)
if mibBuilder.loadTexts:cBitsClkSourceActiveSeconds.setUnits(_P)
_CBitsClkSourceInactiveSeconds_Type=Counter32
_CBitsClkSourceInactiveSeconds_Object=MibTableColumn
cBitsClkSourceInactiveSeconds=_CBitsClkSourceInactiveSeconds_Object((1,3,6,1,4,1,9,9,459,1,1,1,5),_CBitsClkSourceInactiveSeconds_Type())
cBitsClkSourceInactiveSeconds.setMaxAccess(_D)
if mibBuilder.loadTexts:cBitsClkSourceInactiveSeconds.setStatus(_B)
if mibBuilder.loadTexts:cBitsClkSourceInactiveSeconds.setUnits(_P)
_CBitsClkSourceDescription_Type=SnmpAdminString
_CBitsClkSourceDescription_Object=MibTableColumn
cBitsClkSourceDescription=_CBitsClkSourceDescription_Object((1,3,6,1,4,1,9,9,459,1,1,1,6),_CBitsClkSourceDescription_Type())
cBitsClkSourceDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:cBitsClkSourceDescription.setStatus(_B)
class _CBitsClkNotifEnabled_Type(TruthValue):defaultValue=2
_CBitsClkNotifEnabled_Type.__name__=_K
_CBitsClkNotifEnabled_Object=MibScalar
cBitsClkNotifEnabled=_CBitsClkNotifEnabled_Object((1,3,6,1,4,1,9,9,459,1,2),_CBitsClkNotifEnabled_Type())
cBitsClkNotifEnabled.setMaxAccess(_O)
if mibBuilder.loadTexts:cBitsClkNotifEnabled.setStatus(_B)
_CiscoBitsClockMIBConform_ObjectIdentity=ObjectIdentity
ciscoBitsClockMIBConform=_CiscoBitsClockMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,459,2))
_CiscoBitsClockMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoBitsClockMIBCompliances=_CiscoBitsClockMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,459,2,1))
_CiscoBitsClockMIBGroups_ObjectIdentity=ObjectIdentity
ciscoBitsClockMIBGroups=_CiscoBitsClockMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,459,2,2))
ciscoBitsClockSourceGroup=ObjectGroup((1,3,6,1,4,1,9,9,459,2,2,1))
ciscoBitsClockSourceGroup.setObjects(*((_A,_G),(_A,_H),(_A,_Q),(_A,_R),(_A,_S),(_A,_I),(_A,_T)))
if mibBuilder.loadTexts:ciscoBitsClockSourceGroup.setStatus(_B)
ciscoBitsClockSource=NotificationType((1,3,6,1,4,1,9,9,459,0,1))
ciscoBitsClockSource.setObjects(*((_C,_E),(_A,_I),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoBitsClockSource.setStatus(_B)
ciscoBitsClockFreerun=NotificationType((1,3,6,1,4,1,9,9,459,0,2))
ciscoBitsClockFreerun.setObjects((_C,_E))
if mibBuilder.loadTexts:ciscoBitsClockFreerun.setStatus(_B)
ciscoBitsClockHoldover=NotificationType((1,3,6,1,4,1,9,9,459,0,3))
ciscoBitsClockHoldover.setObjects((_C,_E))
if mibBuilder.loadTexts:ciscoBitsClockHoldover.setStatus(_B)
ciscoBitsClockNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,459,2,2,2))
ciscoBitsClockNotifGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoBitsClockNotifGroup.setStatus(_B)
ciscoBitsClockMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,459,2,1,1))
ciscoBitsClockMIBCompliance.setObjects(*((_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoBitsClockMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoBitsClockMIB':ciscoBitsClockMIB,'ciscoBitsClockMIBNotifs':ciscoBitsClockMIBNotifs,_U:ciscoBitsClockSource,_V:ciscoBitsClockFreerun,_W:ciscoBitsClockHoldover,'ciscoBitsClockMIBObjects':ciscoBitsClockMIBObjects,'cBitsClkSourceTable':cBitsClkSourceTable,'cBitsClkSourceEntry':cBitsClkSourceEntry,_G:cBitsClkSourceRoleAdmin,_H:cBitsClkSourceRoleCurrent,_Q:cBitsClkSourceTimestamp,_R:cBitsClkSourceActiveSeconds,_S:cBitsClkSourceInactiveSeconds,_I:cBitsClkSourceDescription,_T:cBitsClkNotifEnabled,'ciscoBitsClockMIBConform':ciscoBitsClockMIBConform,'ciscoBitsClockMIBCompliances':ciscoBitsClockMIBCompliances,'ciscoBitsClockMIBCompliance':ciscoBitsClockMIBCompliance,'ciscoBitsClockMIBGroups':ciscoBitsClockMIBGroups,_X:ciscoBitsClockSourceGroup,_Y:ciscoBitsClockNotifGroup})