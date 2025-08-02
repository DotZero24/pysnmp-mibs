_M='ciscoDtiExtNotifsGroup'
_L='ciscoDtiExtNotifsControlGroup'
_K='cdeClientStatusChange'
_J='cdeServerStatusChange'
_I='cdeClientStatusChangeEnable'
_H='cdeServerStatusChangeEnable'
_G='read-write'
_F='dtiProtocolServerStatusFlag'
_E='dtiProtocolClientStatusFlag'
_D='TruthValue'
_C='DTI-MIB'
_B='CISCO-DTI-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
dtiProtocolClientStatusFlag,dtiProtocolServerStatusFlag=mibBuilder.importSymbols(_C,_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
ciscoDtiExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,822))
if mibBuilder.loadTexts:ciscoDtiExtMIB.setRevisions(('2014-08-22 00:00',))
_CiscoDtiExtNotifs_ObjectIdentity=ObjectIdentity
ciscoDtiExtNotifs=_CiscoDtiExtNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,822,0))
_CiscoDtiExtObjects_ObjectIdentity=ObjectIdentity
ciscoDtiExtObjects=_CiscoDtiExtObjects_ObjectIdentity((1,3,6,1,4,1,9,9,822,1))
class _CdeServerStatusChangeEnable_Type(TruthValue):defaultValue=2
_CdeServerStatusChangeEnable_Type.__name__=_D
_CdeServerStatusChangeEnable_Object=MibScalar
cdeServerStatusChangeEnable=_CdeServerStatusChangeEnable_Object((1,3,6,1,4,1,9,9,822,1,1),_CdeServerStatusChangeEnable_Type())
cdeServerStatusChangeEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:cdeServerStatusChangeEnable.setStatus(_A)
class _CdeClientStatusChangeEnable_Type(TruthValue):defaultValue=2
_CdeClientStatusChangeEnable_Type.__name__=_D
_CdeClientStatusChangeEnable_Object=MibScalar
cdeClientStatusChangeEnable=_CdeClientStatusChangeEnable_Object((1,3,6,1,4,1,9,9,822,1,2),_CdeClientStatusChangeEnable_Type())
cdeClientStatusChangeEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:cdeClientStatusChangeEnable.setStatus(_A)
_CiscoDtiExtConform_ObjectIdentity=ObjectIdentity
ciscoDtiExtConform=_CiscoDtiExtConform_ObjectIdentity((1,3,6,1,4,1,9,9,822,2))
_CiscoDtiExtCompliances_ObjectIdentity=ObjectIdentity
ciscoDtiExtCompliances=_CiscoDtiExtCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,822,2,1))
_CiscoDtiExtGroups_ObjectIdentity=ObjectIdentity
ciscoDtiExtGroups=_CiscoDtiExtGroups_ObjectIdentity((1,3,6,1,4,1,9,9,822,2,2))
ciscoDtiExtNotifsControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,822,2,2,1))
ciscoDtiExtNotifsControlGroup.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ciscoDtiExtNotifsControlGroup.setStatus(_A)
cdeServerStatusChange=NotificationType((1,3,6,1,4,1,9,9,822,0,1))
cdeServerStatusChange.setObjects((_C,_F))
if mibBuilder.loadTexts:cdeServerStatusChange.setStatus(_A)
cdeClientStatusChange=NotificationType((1,3,6,1,4,1,9,9,822,0,2))
cdeClientStatusChange.setObjects((_C,_E))
if mibBuilder.loadTexts:cdeClientStatusChange.setStatus(_A)
ciscoDtiExtNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,822,2,2,2))
ciscoDtiExtNotifsGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoDtiExtNotifsGroup.setStatus(_A)
ciscoDtiExtCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,822,2,1,1))
ciscoDtiExtCompliance.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoDtiExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDtiExtMIB':ciscoDtiExtMIB,'ciscoDtiExtNotifs':ciscoDtiExtNotifs,_J:cdeServerStatusChange,_K:cdeClientStatusChange,'ciscoDtiExtObjects':ciscoDtiExtObjects,_H:cdeServerStatusChangeEnable,_I:cdeClientStatusChangeEnable,'ciscoDtiExtConform':ciscoDtiExtConform,'ciscoDtiExtCompliances':ciscoDtiExtCompliances,'ciscoDtiExtCompliance':ciscoDtiExtCompliance,'ciscoDtiExtGroups':ciscoDtiExtGroups,_L:ciscoDtiExtNotifsControlGroup,_M:ciscoDtiExtNotifsGroup})