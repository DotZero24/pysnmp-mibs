_L='read-create'
_K='raisecomVrrpTrackIf'
_J='RAISECOM-VRRP-MIB'
_I='Integer32'
_H='OctetString'
_G='vrrpOperVrId'
_F='VRRP-MIB'
_E='TruthValue'
_D='ifIndex'
_C='IF-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_E)
vrrpOperVrId,=mibBuilder.importSymbols(_F,_G)
raisecomVrrp=ModuleIdentity((1,3,6,1,4,1,8886,1,41))
if mibBuilder.loadTexts:raisecomVrrp.setRevisions(('2011-07-26 00:00',))
_RaisecomVrrpNotifications_ObjectIdentity=ObjectIdentity
raisecomVrrpNotifications=_RaisecomVrrpNotifications_ObjectIdentity((1,3,6,1,4,1,8886,1,41,0))
_RaisecomVrrpObjects_ObjectIdentity=ObjectIdentity
raisecomVrrpObjects=_RaisecomVrrpObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,41,1))
_RaisecomVrrpScalarObjects_ObjectIdentity=ObjectIdentity
raisecomVrrpScalarObjects=_RaisecomVrrpScalarObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,41,1,1))
class _RaisecomVrrpPing_Type(TruthValue):defaultValue=1
_RaisecomVrrpPing_Type.__name__=_E
_RaisecomVrrpPing_Object=MibScalar
raisecomVrrpPing=_RaisecomVrrpPing_Object((1,3,6,1,4,1,8886,1,41,1,1,1),_RaisecomVrrpPing_Type())
raisecomVrrpPing.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVrrpPing.setStatus(_A)
class _RaisecomVrrpStatisticsClear_Type(TruthValue):defaultValue=2
_RaisecomVrrpStatisticsClear_Type.__name__=_E
_RaisecomVrrpStatisticsClear_Object=MibScalar
raisecomVrrpStatisticsClear=_RaisecomVrrpStatisticsClear_Object((1,3,6,1,4,1,8886,1,41,1,1,2),_RaisecomVrrpStatisticsClear_Type())
raisecomVrrpStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVrrpStatisticsClear.setStatus(_A)
_RaisecomVrrpOperTable_Object=MibTable
raisecomVrrpOperTable=_RaisecomVrrpOperTable_Object((1,3,6,1,4,1,8886,1,41,1,2))
if mibBuilder.loadTexts:raisecomVrrpOperTable.setStatus(_A)
_RaisecomVrrpOperEntry_Object=MibTableRow
raisecomVrrpOperEntry=_RaisecomVrrpOperEntry_Object((1,3,6,1,4,1,8886,1,41,1,2,1))
raisecomVrrpOperEntry.setIndexNames((0,_C,_D),(0,_F,_G))
if mibBuilder.loadTexts:raisecomVrrpOperEntry.setStatus(_A)
class _RaisecomVrrpOperDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RaisecomVrrpOperDesc_Type.__name__=_H
_RaisecomVrrpOperDesc_Object=MibTableColumn
raisecomVrrpOperDesc=_RaisecomVrrpOperDesc_Object((1,3,6,1,4,1,8886,1,41,1,2,1,1),_RaisecomVrrpOperDesc_Type())
raisecomVrrpOperDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVrrpOperDesc.setStatus(_A)
class _RaisecomVrrpOperPreemptDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomVrrpOperPreemptDelay_Type.__name__=_I
_RaisecomVrrpOperPreemptDelay_Object=MibTableColumn
raisecomVrrpOperPreemptDelay=_RaisecomVrrpOperPreemptDelay_Object((1,3,6,1,4,1,8886,1,41,1,2,1,2),_RaisecomVrrpOperPreemptDelay_Type())
raisecomVrrpOperPreemptDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomVrrpOperPreemptDelay.setStatus(_A)
if mibBuilder.loadTexts:raisecomVrrpOperPreemptDelay.setUnits('second')
_RaisecomVrrpTrackIfTable_Object=MibTable
raisecomVrrpTrackIfTable=_RaisecomVrrpTrackIfTable_Object((1,3,6,1,4,1,8886,1,41,1,3))
if mibBuilder.loadTexts:raisecomVrrpTrackIfTable.setStatus(_A)
_RaisecomVrrpTrackIfEntry_Object=MibTableRow
raisecomVrrpTrackIfEntry=_RaisecomVrrpTrackIfEntry_Object((1,3,6,1,4,1,8886,1,41,1,3,1))
raisecomVrrpTrackIfEntry.setIndexNames((0,_C,_D),(0,_F,_G),(0,_J,_K))
if mibBuilder.loadTexts:raisecomVrrpTrackIfEntry.setStatus(_A)
_RaisecomVrrpTrackIf_Type=Integer32
_RaisecomVrrpTrackIf_Object=MibTableColumn
raisecomVrrpTrackIf=_RaisecomVrrpTrackIf_Object((1,3,6,1,4,1,8886,1,41,1,3,1,1),_RaisecomVrrpTrackIf_Type())
raisecomVrrpTrackIf.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:raisecomVrrpTrackIf.setStatus(_A)
_RaisecomVrrpTrackIfPriChg_Type=Integer32
_RaisecomVrrpTrackIfPriChg_Object=MibTableColumn
raisecomVrrpTrackIfPriChg=_RaisecomVrrpTrackIfPriChg_Object((1,3,6,1,4,1,8886,1,41,1,3,1,2),_RaisecomVrrpTrackIfPriChg_Type())
raisecomVrrpTrackIfPriChg.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomVrrpTrackIfPriChg.setStatus(_A)
_RaisecomVrrpTrackIfRowStatus_Type=RowStatus
_RaisecomVrrpTrackIfRowStatus_Object=MibTableColumn
raisecomVrrpTrackIfRowStatus=_RaisecomVrrpTrackIfRowStatus_Object((1,3,6,1,4,1,8886,1,41,1,3,1,3),_RaisecomVrrpTrackIfRowStatus_Type())
raisecomVrrpTrackIfRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomVrrpTrackIfRowStatus.setStatus(_A)
_RaisecomVrrpConformance_ObjectIdentity=ObjectIdentity
raisecomVrrpConformance=_RaisecomVrrpConformance_ObjectIdentity((1,3,6,1,4,1,8886,1,41,2))
mibBuilder.exportSymbols(_J,**{'raisecomVrrp':raisecomVrrp,'raisecomVrrpNotifications':raisecomVrrpNotifications,'raisecomVrrpObjects':raisecomVrrpObjects,'raisecomVrrpScalarObjects':raisecomVrrpScalarObjects,'raisecomVrrpPing':raisecomVrrpPing,'raisecomVrrpStatisticsClear':raisecomVrrpStatisticsClear,'raisecomVrrpOperTable':raisecomVrrpOperTable,'raisecomVrrpOperEntry':raisecomVrrpOperEntry,'raisecomVrrpOperDesc':raisecomVrrpOperDesc,'raisecomVrrpOperPreemptDelay':raisecomVrrpOperPreemptDelay,'raisecomVrrpTrackIfTable':raisecomVrrpTrackIfTable,'raisecomVrrpTrackIfEntry':raisecomVrrpTrackIfEntry,_K:raisecomVrrpTrackIf,'raisecomVrrpTrackIfPriChg':raisecomVrrpTrackIfPriChg,'raisecomVrrpTrackIfRowStatus':raisecomVrrpTrackIfRowStatus,'raisecomVrrpConformance':raisecomVrrpConformance})