_I='zyTrtcmDscpProfileName'
_H='ZYXEL-TRTCM-MIB'
_G='read-only'
_F='read-create'
_E='Integer32'
_D='dot1dBasePort'
_C='BRIDGE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_C,_D)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelTrtcm=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,85))
_ZyxelTrtcmSetup_ObjectIdentity=ObjectIdentity
zyxelTrtcmSetup=_ZyxelTrtcmSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,85,1))
_ZyTctcmState_Type=EnabledStatus
_ZyTctcmState_Object=MibScalar
zyTctcmState=_ZyTctcmState_Object((1,3,6,1,4,1,890,1,15,3,85,1,1),_ZyTctcmState_Type())
zyTctcmState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTctcmState.setStatus(_A)
class _ZyTrtcmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('colorAware',0),('colorBlind',1)))
_ZyTrtcmMode_Type.__name__=_E
_ZyTrtcmMode_Object=MibScalar
zyTrtcmMode=_ZyTrtcmMode_Object((1,3,6,1,4,1,890,1,15,3,85,1,2),_ZyTrtcmMode_Type())
zyTrtcmMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTrtcmMode.setStatus(_A)
_ZyxelTrtcmPortTable_Object=MibTable
zyxelTrtcmPortTable=_ZyxelTrtcmPortTable_Object((1,3,6,1,4,1,890,1,15,3,85,1,3))
if mibBuilder.loadTexts:zyxelTrtcmPortTable.setStatus(_A)
_ZyxelTrtcmPortEntry_Object=MibTableRow
zyxelTrtcmPortEntry=_ZyxelTrtcmPortEntry_Object((1,3,6,1,4,1,890,1,15,3,85,1,3,1))
zyxelTrtcmPortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelTrtcmPortEntry.setStatus(_A)
_ZyTrtcmPortState_Type=EnabledStatus
_ZyTrtcmPortState_Object=MibTableColumn
zyTrtcmPortState=_ZyTrtcmPortState_Object((1,3,6,1,4,1,890,1,15,3,85,1,3,1,1),_ZyTrtcmPortState_Type())
zyTrtcmPortState.setMaxAccess(_F)
if mibBuilder.loadTexts:zyTrtcmPortState.setStatus(_A)
_ZyTrtcmPortCir_Type=Integer32
_ZyTrtcmPortCir_Object=MibTableColumn
zyTrtcmPortCir=_ZyTrtcmPortCir_Object((1,3,6,1,4,1,890,1,15,3,85,1,3,1,2),_ZyTrtcmPortCir_Type())
zyTrtcmPortCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTrtcmPortCir.setStatus(_A)
_ZyTrtcmPortPir_Type=Integer32
_ZyTrtcmPortPir_Object=MibTableColumn
zyTrtcmPortPir=_ZyTrtcmPortPir_Object((1,3,6,1,4,1,890,1,15,3,85,1,3,1,3),_ZyTrtcmPortPir_Type())
zyTrtcmPortPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTrtcmPortPir.setStatus(_A)
_ZyTrtcmPortDscpProfile_Type=DisplayString
_ZyTrtcmPortDscpProfile_Object=MibTableColumn
zyTrtcmPortDscpProfile=_ZyTrtcmPortDscpProfile_Object((1,3,6,1,4,1,890,1,15,3,85,1,3,1,4),_ZyTrtcmPortDscpProfile_Type())
zyTrtcmPortDscpProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTrtcmPortDscpProfile.setStatus(_A)
_ZyTrtcmMaxNumberOfDscpProfiles_Type=Integer32
_ZyTrtcmMaxNumberOfDscpProfiles_Object=MibScalar
zyTrtcmMaxNumberOfDscpProfiles=_ZyTrtcmMaxNumberOfDscpProfiles_Object((1,3,6,1,4,1,890,1,15,3,85,1,4),_ZyTrtcmMaxNumberOfDscpProfiles_Type())
zyTrtcmMaxNumberOfDscpProfiles.setMaxAccess(_G)
if mibBuilder.loadTexts:zyTrtcmMaxNumberOfDscpProfiles.setStatus(_A)
_ZyxelTrtcmDscpProfileTable_Object=MibTable
zyxelTrtcmDscpProfileTable=_ZyxelTrtcmDscpProfileTable_Object((1,3,6,1,4,1,890,1,15,3,85,1,5))
if mibBuilder.loadTexts:zyxelTrtcmDscpProfileTable.setStatus(_A)
_ZyxelTrtcmDscpProfileEntry_Object=MibTableRow
zyxelTrtcmDscpProfileEntry=_ZyxelTrtcmDscpProfileEntry_Object((1,3,6,1,4,1,890,1,15,3,85,1,5,1))
zyxelTrtcmDscpProfileEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zyxelTrtcmDscpProfileEntry.setStatus(_A)
_ZyTrtcmDscpProfileName_Type=DisplayString
_ZyTrtcmDscpProfileName_Object=MibTableColumn
zyTrtcmDscpProfileName=_ZyTrtcmDscpProfileName_Object((1,3,6,1,4,1,890,1,15,3,85,1,5,1,1),_ZyTrtcmDscpProfileName_Type())
zyTrtcmDscpProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zyTrtcmDscpProfileName.setStatus(_A)
_ZyTrtcmDscpProfileDscpGreen_Type=Integer32
_ZyTrtcmDscpProfileDscpGreen_Object=MibTableColumn
zyTrtcmDscpProfileDscpGreen=_ZyTrtcmDscpProfileDscpGreen_Object((1,3,6,1,4,1,890,1,15,3,85,1,5,1,2),_ZyTrtcmDscpProfileDscpGreen_Type())
zyTrtcmDscpProfileDscpGreen.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTrtcmDscpProfileDscpGreen.setStatus(_A)
_ZyTrtcmDscpProfileDscpYellow_Type=Integer32
_ZyTrtcmDscpProfileDscpYellow_Object=MibTableColumn
zyTrtcmDscpProfileDscpYellow=_ZyTrtcmDscpProfileDscpYellow_Object((1,3,6,1,4,1,890,1,15,3,85,1,5,1,3),_ZyTrtcmDscpProfileDscpYellow_Type())
zyTrtcmDscpProfileDscpYellow.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTrtcmDscpProfileDscpYellow.setStatus(_A)
_ZyTrtcmDscpProfileDscpRed_Type=Integer32
_ZyTrtcmDscpProfileDscpRed_Object=MibTableColumn
zyTrtcmDscpProfileDscpRed=_ZyTrtcmDscpProfileDscpRed_Object((1,3,6,1,4,1,890,1,15,3,85,1,5,1,4),_ZyTrtcmDscpProfileDscpRed_Type())
zyTrtcmDscpProfileDscpRed.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTrtcmDscpProfileDscpRed.setStatus(_A)
_ZyTrtcmDscpProfileRowstatus_Type=RowStatus
_ZyTrtcmDscpProfileRowstatus_Object=MibTableColumn
zyTrtcmDscpProfileRowstatus=_ZyTrtcmDscpProfileRowstatus_Object((1,3,6,1,4,1,890,1,15,3,85,1,5,1,5),_ZyTrtcmDscpProfileRowstatus_Type())
zyTrtcmDscpProfileRowstatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zyTrtcmDscpProfileRowstatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'zyxelTrtcm':zyxelTrtcm,'zyxelTrtcmSetup':zyxelTrtcmSetup,'zyTctcmState':zyTctcmState,'zyTrtcmMode':zyTrtcmMode,'zyxelTrtcmPortTable':zyxelTrtcmPortTable,'zyxelTrtcmPortEntry':zyxelTrtcmPortEntry,'zyTrtcmPortState':zyTrtcmPortState,'zyTrtcmPortCir':zyTrtcmPortCir,'zyTrtcmPortPir':zyTrtcmPortPir,'zyTrtcmPortDscpProfile':zyTrtcmPortDscpProfile,'zyTrtcmMaxNumberOfDscpProfiles':zyTrtcmMaxNumberOfDscpProfiles,'zyxelTrtcmDscpProfileTable':zyxelTrtcmDscpProfileTable,'zyxelTrtcmDscpProfileEntry':zyxelTrtcmDscpProfileEntry,_I:zyTrtcmDscpProfileName,'zyTrtcmDscpProfileDscpGreen':zyTrtcmDscpProfileDscpGreen,'zyTrtcmDscpProfileDscpYellow':zyTrtcmDscpProfileDscpYellow,'zyTrtcmDscpProfileDscpRed':zyTrtcmDscpProfileDscpRed,'zyTrtcmDscpProfileRowstatus':zyTrtcmDscpProfileRowstatus})