_C='DisplayString'
_B='accessible-for-notify'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nortelNetworkManagementInterfaceMIBs,=mibBuilder.importSymbols('NORTEL-GENERIC-MIB','nortelNetworkManagementInterfaceMIBs')
NortelNMIadminState,NortelNMIneType,NortelNMIoperState,NortelNMIunknownStatusValue=mibBuilder.importSymbols('NORTEL-NMI-TC-MIB','NortelNMIadminState','NortelNMIneType','NortelNMIoperState','NortelNMIunknownStatusValue')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
nortelNMInotificationsMIB=ModuleIdentity((1,3,6,1,4,1,562,29,1,6))
if mibBuilder.loadTexts:nortelNMInotificationsMIB.setRevisions(('1999-07-19 00:00','1999-06-24 00:00','1999-05-31 00:00','1999-04-12 00:00','1999-03-22 00:00'))
_NortelNMIcurrentTxNotificationSequenceNum_Type=Unsigned32
_NortelNMIcurrentTxNotificationSequenceNum_Object=MibScalar
nortelNMIcurrentTxNotificationSequenceNum=_NortelNMIcurrentTxNotificationSequenceNum_Object((1,3,6,1,4,1,562,29,1,6,1),_NortelNMIcurrentTxNotificationSequenceNum_Type())
nortelNMIcurrentTxNotificationSequenceNum.setMaxAccess('read-only')
if mibBuilder.loadTexts:nortelNMIcurrentTxNotificationSequenceNum.setStatus(_A)
_NortelNMIcommonNotiVarbinds_ObjectIdentity=ObjectIdentity
nortelNMIcommonNotiVarbinds=_NortelNMIcommonNotiVarbinds_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,2))
if mibBuilder.loadTexts:nortelNMIcommonNotiVarbinds.setStatus(_A)
_NortelNMInotifyNeType_Type=NortelNMIneType
_NortelNMInotifyNeType_Object=MibScalar
nortelNMInotifyNeType=_NortelNMInotifyNeType_Object((1,3,6,1,4,1,562,29,1,6,2,1),_NortelNMInotifyNeType_Type())
nortelNMInotifyNeType.setMaxAccess(_B)
if mibBuilder.loadTexts:nortelNMInotifyNeType.setStatus(_A)
class _NortelNMInotifyNeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NortelNMInotifyNeName_Type.__name__=_C
_NortelNMInotifyNeName_Object=MibScalar
nortelNMInotifyNeName=_NortelNMInotifyNeName_Object((1,3,6,1,4,1,562,29,1,6,2,2),_NortelNMInotifyNeName_Type())
nortelNMInotifyNeName.setMaxAccess(_B)
if mibBuilder.loadTexts:nortelNMInotifyNeName.setStatus(_A)
_NortelNMInotifyNeAdminState_Type=NortelNMIadminState
_NortelNMInotifyNeAdminState_Object=MibScalar
nortelNMInotifyNeAdminState=_NortelNMInotifyNeAdminState_Object((1,3,6,1,4,1,562,29,1,6,2,3),_NortelNMInotifyNeAdminState_Type())
nortelNMInotifyNeAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:nortelNMInotifyNeAdminState.setStatus(_A)
_NortelNMInotifyNeOperState_Type=NortelNMIoperState
_NortelNMInotifyNeOperState_Object=MibScalar
nortelNMInotifyNeOperState=_NortelNMInotifyNeOperState_Object((1,3,6,1,4,1,562,29,1,6,2,4),_NortelNMInotifyNeOperState_Type())
nortelNMInotifyNeOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:nortelNMInotifyNeOperState.setStatus(_A)
_NortelNMInotifyNeUnknownStatus_Type=NortelNMIunknownStatusValue
_NortelNMInotifyNeUnknownStatus_Object=MibScalar
nortelNMInotifyNeUnknownStatus=_NortelNMInotifyNeUnknownStatus_Object((1,3,6,1,4,1,562,29,1,6,2,5),_NortelNMInotifyNeUnknownStatus_Type())
nortelNMInotifyNeUnknownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nortelNMInotifyNeUnknownStatus.setStatus(_A)
_NortelNMIconfigNotiMIB_ObjectIdentity=ObjectIdentity
nortelNMIconfigNotiMIB=_NortelNMIconfigNotiMIB_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,3))
if mibBuilder.loadTexts:nortelNMIconfigNotiMIB.setStatus(_A)
_NortelNMIfaultNotiMIB_ObjectIdentity=ObjectIdentity
nortelNMIfaultNotiMIB=_NortelNMIfaultNotiMIB_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,4))
if mibBuilder.loadTexts:nortelNMIfaultNotiMIB.setStatus(_A)
_NortelNMIinfoNotiMIB_ObjectIdentity=ObjectIdentity
nortelNMIinfoNotiMIB=_NortelNMIinfoNotiMIB_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,5))
if mibBuilder.loadTexts:nortelNMIinfoNotiMIB.setStatus(_A)
mibBuilder.exportSymbols('NORTEL-NMI-NOTIFICATIONS-MIB',**{'nortelNMInotificationsMIB':nortelNMInotificationsMIB,'nortelNMIcurrentTxNotificationSequenceNum':nortelNMIcurrentTxNotificationSequenceNum,'nortelNMIcommonNotiVarbinds':nortelNMIcommonNotiVarbinds,'nortelNMInotifyNeType':nortelNMInotifyNeType,'nortelNMInotifyNeName':nortelNMInotifyNeName,'nortelNMInotifyNeAdminState':nortelNMInotifyNeAdminState,'nortelNMInotifyNeOperState':nortelNMInotifyNeOperState,'nortelNMInotifyNeUnknownStatus':nortelNMInotifyNeUnknownStatus,'nortelNMIconfigNotiMIB':nortelNMIconfigNotiMIB,'nortelNMIfaultNotiMIB':nortelNMIfaultNotiMIB,'nortelNMIinfoNotiMIB':nortelNMIinfoNotiMIB})