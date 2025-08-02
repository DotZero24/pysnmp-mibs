_G='dpDdpClientGlobalState'
_F='read-write'
_E='TruthValue'
_D='Unsigned32'
_C='dpDdpClientControlGroup'
_B='DLINKPRIME-DDP-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
dlinkPrimeDdpClientMIB=ModuleIdentity((1,3,6,1,4,1,171,15,2))
if mibBuilder.loadTexts:dlinkPrimeDdpClientMIB.setRevisions(('2014-04-26 00:00',))
_DpDdpClientNotifications_ObjectIdentity=ObjectIdentity
dpDdpClientNotifications=_DpDdpClientNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,2,0))
_DpDdpClientObjects_ObjectIdentity=ObjectIdentity
dpDdpClientObjects=_DpDdpClientObjects_ObjectIdentity((1,3,6,1,4,1,171,15,2,1))
_DpDdpClientCtrl_ObjectIdentity=ObjectIdentity
dpDdpClientCtrl=_DpDdpClientCtrl_ObjectIdentity((1,3,6,1,4,1,171,15,2,1,1))
class _DpDdpClientGlobalState_Type(TruthValue):defaultValue=1
_DpDdpClientGlobalState_Type.__name__=_E
_DpDdpClientGlobalState_Object=MibScalar
dpDdpClientGlobalState=_DpDdpClientGlobalState_Object((1,3,6,1,4,1,171,15,2,1,1,1),_DpDdpClientGlobalState_Type())
dpDdpClientGlobalState.setMaxAccess(_F)
if mibBuilder.loadTexts:dpDdpClientGlobalState.setStatus(_A)
class _DpDdpClientReportTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(30,30),ValueRangeConstraint(60,60),ValueRangeConstraint(90,90),ValueRangeConstraint(120,120))
_DpDdpClientReportTimer_Type.__name__=_D
_DpDdpClientReportTimer_Object=MibScalar
dpDdpClientReportTimer=_DpDdpClientReportTimer_Object((1,3,6,1,4,1,171,15,2,1,1,2),_DpDdpClientReportTimer_Type())
dpDdpClientReportTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:dpDdpClientReportTimer.setStatus(_A)
if mibBuilder.loadTexts:dpDdpClientReportTimer.setUnits('second')
_DpDdpClientConformance_ObjectIdentity=ObjectIdentity
dpDdpClientConformance=_DpDdpClientConformance_ObjectIdentity((1,3,6,1,4,1,171,15,2,2))
_DpDdpClientCompliances_ObjectIdentity=ObjectIdentity
dpDdpClientCompliances=_DpDdpClientCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,2,2,1))
_DpDdpClientGroups_ObjectIdentity=ObjectIdentity
dpDdpClientGroups=_DpDdpClientGroups_ObjectIdentity((1,3,6,1,4,1,171,15,2,2,2))
dpDdpClientControlGroup=ObjectGroup((1,3,6,1,4,1,171,15,2,2,2,1))
dpDdpClientControlGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:dpDdpClientControlGroup.setStatus(_A)
dpDdpClientCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,2,2,1,1))
dpDdpClientCompliance.setObjects(*((_B,_C),(_B,_C)))
if mibBuilder.loadTexts:dpDdpClientCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeDdpClientMIB':dlinkPrimeDdpClientMIB,'dpDdpClientNotifications':dpDdpClientNotifications,'dpDdpClientObjects':dpDdpClientObjects,'dpDdpClientCtrl':dpDdpClientCtrl,_G:dpDdpClientGlobalState,'dpDdpClientReportTimer':dpDdpClientReportTimer,'dpDdpClientConformance':dpDdpClientConformance,'dpDdpClientCompliances':dpDdpClientCompliances,'dpDdpClientCompliance':dpDdpClientCompliance,'dpDdpClientGroups':dpDdpClientGroups,_C:dpDdpClientControlGroup})