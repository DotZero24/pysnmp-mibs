_Q='cicServiceGroup'
_P='cicServiceRepeatResult'
_O='cicServiceRepeatOwner'
_N='cicServiceRepetition'
_M='cicServiceGraceTime'
_L='cicServiceAdminState'
_K='cicServiceOperState'
_J='CIfCallServiceAdminState'
_I='read-only'
_H='inService'
_G='Unsigned32'
_F='ifIndex'
_E='IF-MIB'
_D='ConfigIterator'
_C='read-write'
_B='CISCO-IF-CALL-SERVICE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
BulkConfigResult,ConfigIterator=mibBuilder.importSymbols('CISCO-TC','BulkConfigResult',_D)
ifIndex,=mibBuilder.importSymbols(_E,_F)
OwnerString,=mibBuilder.importSymbols('RMON-MIB','OwnerString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoIfCallServiceMIB=ModuleIdentity((1,3,6,1,4,1,9,9,9968))
if mibBuilder.loadTexts:ciscoIfCallServiceMIB.setRevisions(('2003-04-25 00:00',))
class CIfCallServiceOperState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('outOfService',2),('oosPending',3)))
class CIfCallServiceAdminState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('forcedOutOfService',2),('gracefulOutOfService',3)))
_CiscoIfCallServiceMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIfCallServiceMIBNotifs=_CiscoIfCallServiceMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,9968,0))
_CiscoIfCallServiceMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIfCallServiceMIBObjects=_CiscoIfCallServiceMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9968,1))
_CicServiceConfig_ObjectIdentity=ObjectIdentity
cicServiceConfig=_CicServiceConfig_ObjectIdentity((1,3,6,1,4,1,9,9,9968,1,1))
_CicServiceTable_Object=MibTable
cicServiceTable=_CicServiceTable_Object((1,3,6,1,4,1,9,9,9968,1,1,1))
if mibBuilder.loadTexts:cicServiceTable.setStatus(_A)
_CicServiceEntry_Object=MibTableRow
cicServiceEntry=_CicServiceEntry_Object((1,3,6,1,4,1,9,9,9968,1,1,1,1))
cicServiceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cicServiceEntry.setStatus(_A)
_CicServiceOperState_Type=CIfCallServiceOperState
_CicServiceOperState_Object=MibTableColumn
cicServiceOperState=_CicServiceOperState_Object((1,3,6,1,4,1,9,9,9968,1,1,1,1,1),_CicServiceOperState_Type())
cicServiceOperState.setMaxAccess(_I)
if mibBuilder.loadTexts:cicServiceOperState.setStatus(_A)
class _CicServiceAdminState_Type(CIfCallServiceAdminState):defaultValue=1
_CicServiceAdminState_Type.__name__=_J
_CicServiceAdminState_Object=MibTableColumn
cicServiceAdminState=_CicServiceAdminState_Object((1,3,6,1,4,1,9,9,9968,1,1,1,1,2),_CicServiceAdminState_Type())
cicServiceAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cicServiceAdminState.setStatus(_A)
class _CicServiceGraceTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CicServiceGraceTime_Type.__name__=_G
_CicServiceGraceTime_Object=MibTableColumn
cicServiceGraceTime=_CicServiceGraceTime_Object((1,3,6,1,4,1,9,9,9968,1,1,1,1,3),_CicServiceGraceTime_Type())
cicServiceGraceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cicServiceGraceTime.setStatus(_A)
if mibBuilder.loadTexts:cicServiceGraceTime.setUnits('seconds')
class _CicServiceRepetition_Type(ConfigIterator):defaultValue=1
_CicServiceRepetition_Type.__name__=_D
_CicServiceRepetition_Object=MibTableColumn
cicServiceRepetition=_CicServiceRepetition_Object((1,3,6,1,4,1,9,9,9968,1,1,1,1,4),_CicServiceRepetition_Type())
cicServiceRepetition.setMaxAccess(_C)
if mibBuilder.loadTexts:cicServiceRepetition.setStatus(_A)
_CicServiceRepeatOwner_Type=OwnerString
_CicServiceRepeatOwner_Object=MibTableColumn
cicServiceRepeatOwner=_CicServiceRepeatOwner_Object((1,3,6,1,4,1,9,9,9968,1,1,1,1,5),_CicServiceRepeatOwner_Type())
cicServiceRepeatOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:cicServiceRepeatOwner.setStatus(_A)
_CicServiceRepeatResult_Type=BulkConfigResult
_CicServiceRepeatResult_Object=MibTableColumn
cicServiceRepeatResult=_CicServiceRepeatResult_Object((1,3,6,1,4,1,9,9,9968,1,1,1,1,6),_CicServiceRepeatResult_Type())
cicServiceRepeatResult.setMaxAccess(_I)
if mibBuilder.loadTexts:cicServiceRepeatResult.setStatus(_A)
_CiscoIfCallServiceMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIfCallServiceMIBConformance=_CiscoIfCallServiceMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,9968,2))
_CicServiceCompliances_ObjectIdentity=ObjectIdentity
cicServiceCompliances=_CicServiceCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,9968,2,1))
_CicServiceGroups_ObjectIdentity=ObjectIdentity
cicServiceGroups=_CicServiceGroups_ObjectIdentity((1,3,6,1,4,1,9,9,9968,2,2))
cicServiceGroup=ObjectGroup((1,3,6,1,4,1,9,9,9968,2,2,1))
cicServiceGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cicServiceGroup.setStatus(_A)
cicServiceCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,9968,2,1,1))
cicServiceCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:cicServiceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CIfCallServiceOperState':CIfCallServiceOperState,_J:CIfCallServiceAdminState,'ciscoIfCallServiceMIB':ciscoIfCallServiceMIB,'ciscoIfCallServiceMIBNotifs':ciscoIfCallServiceMIBNotifs,'ciscoIfCallServiceMIBObjects':ciscoIfCallServiceMIBObjects,'cicServiceConfig':cicServiceConfig,'cicServiceTable':cicServiceTable,'cicServiceEntry':cicServiceEntry,_K:cicServiceOperState,_L:cicServiceAdminState,_M:cicServiceGraceTime,_N:cicServiceRepetition,_O:cicServiceRepeatOwner,_P:cicServiceRepeatResult,'ciscoIfCallServiceMIBConformance':ciscoIfCallServiceMIBConformance,'cicServiceCompliances':cicServiceCompliances,'cicServiceCompliance':cicServiceCompliance,'cicServiceGroups':cicServiceGroups,_Q:cicServiceGroup})