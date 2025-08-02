_F='refreshOID'
_E='statusOID'
_D='accessible-for-notify'
_C='moduleInfo'
_B='SUNMANAGEMENTCENTER-TRAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
traps=ModuleIdentity((1,3,6,1,4,1,42,2,12,2,0))
if mibBuilder.loadTexts:traps.setRevisions(('1999-07-20 15:05',))
_Sun_ObjectIdentity=ObjectIdentity
sun=_Sun_ObjectIdentity((1,3,6,1,4,1,42))
_Prod_ObjectIdentity=ObjectIdentity
prod=_Prod_ObjectIdentity((1,3,6,1,4,1,42,2))
_Sunsymon_ObjectIdentity=ObjectIdentity
sunsymon=_Sunsymon_ObjectIdentity((1,3,6,1,4,1,42,2,12))
_Agent_ObjectIdentity=ObjectIdentity
agent=_Agent_ObjectIdentity((1,3,6,1,4,1,42,2,12,2))
_Base_ObjectIdentity=ObjectIdentity
base=_Base_ObjectIdentity((1,3,6,1,4,1,42,2,12,2,1))
_StatusOID_Type=ObjectIdentifier
_StatusOID_Object=MibScalar
statusOID=_StatusOID_Object((1,3,6,1,4,1,42,2,12,2,1,3,1),_StatusOID_Type())
statusOID.setMaxAccess(_D)
if mibBuilder.loadTexts:statusOID.setStatus(_A)
_RefreshOID_Type=ObjectIdentifier
_RefreshOID_Object=MibScalar
refreshOID=_RefreshOID_Object((1,3,6,1,4,1,42,2,12,2,1,3,2),_RefreshOID_Type())
refreshOID.setMaxAccess(_D)
if mibBuilder.loadTexts:refreshOID.setStatus(_A)
_ModuleInfo_Type=OctetString
_ModuleInfo_Object=MibScalar
moduleInfo=_ModuleInfo_Object((1,3,6,1,4,1,42,2,12,2,1,3,5),_ModuleInfo_Type())
moduleInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleInfo.setStatus(_A)
trapInfoGroup=ObjectGroup((1,3,6,1,4,1,42,2,12,2,1,3))
trapInfoGroup.setObjects(*((_B,_E),(_B,_F),(_B,_C)))
if mibBuilder.loadTexts:trapInfoGroup.setStatus(_A)
statusChange=NotificationType((1,3,6,1,4,1,42,2,12,2,0,1))
statusChange.setObjects((_B,_E))
if mibBuilder.loadTexts:statusChange.setStatus(_A)
valueRefresh=NotificationType((1,3,6,1,4,1,42,2,12,2,0,2))
valueRefresh.setObjects((_B,_F))
if mibBuilder.loadTexts:valueRefresh.setStatus(_A)
moduleLoaded=NotificationType((1,3,6,1,4,1,42,2,12,2,0,4))
moduleLoaded.setObjects((_B,_C))
if mibBuilder.loadTexts:moduleLoaded.setStatus(_A)
moduleUnloaded=NotificationType((1,3,6,1,4,1,42,2,12,2,0,5))
moduleUnloaded.setObjects((_B,_C))
if mibBuilder.loadTexts:moduleUnloaded.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sun':sun,'prod':prod,'sunsymon':sunsymon,'agent':agent,'traps':traps,'statusChange':statusChange,'valueRefresh':valueRefresh,'moduleLoaded':moduleLoaded,'moduleUnloaded':moduleUnloaded,'base':base,'trapInfoGroup':trapInfoGroup,_E:statusOID,_F:refreshOID,_C:moduleInfo})