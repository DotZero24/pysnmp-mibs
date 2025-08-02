_J='DisplayString'
_I='Unsigned32'
_H='MibTableColumn'
_G='MibTableRow'
_F='MibTable'
_E='MibScalar'
_D='ObjectIdentity'
_C='NotificationType'
_B='ModuleIdentity'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress',_B,'MibIdentifier',_C,_D,_E,_F,_G,_H,'TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
ModuleIdentity,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Unsigned32,apex=mibBuilder.importSymbols('TRANGO-APEX-MIB',_B,_C,_D,_E,_F,_G,_H,_I,'apex')
class DisplayString(OctetString):0
_Trangotrap_ObjectIdentity=ObjectIdentity
trangotrap=_Trangotrap_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6))
_Traplock_ObjectIdentity=ObjectIdentity
traplock=_Traplock_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,3))
_Trapthreshold_ObjectIdentity=ObjectIdentity
trapthreshold=_Trapthreshold_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,4))
_Trapmse_ObjectIdentity=ObjectIdentity
trapmse=_Trapmse_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,4,1))
_Trapber_ObjectIdentity=ObjectIdentity
trapber=_Trapber_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,4,2))
_Trapfer_ObjectIdentity=ObjectIdentity
trapfer=_Trapfer_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,4,3))
_Traprssi_ObjectIdentity=ObjectIdentity
traprssi=_Traprssi_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,4,4))
_Trapidutemp_ObjectIdentity=ObjectIdentity
trapidutemp=_Trapidutemp_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,4,5))
_Trapodutemp_ObjectIdentity=ObjectIdentity
trapodutemp=_Trapodutemp_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,4,6))
_Trapinport_ObjectIdentity=ObjectIdentity
trapinport=_Trapinport_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,4,7))
_Trapoutport_ObjectIdentity=ObjectIdentity
trapoutport=_Trapoutport_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,4,8))
_Trapstandby_ObjectIdentity=ObjectIdentity
trapstandby=_Trapstandby_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,5))
_Trapeth_ObjectIdentity=ObjectIdentity
trapeth=_Trapeth_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,6))
_Trapethstatus_ObjectIdentity=ObjectIdentity
trapethstatus=_Trapethstatus_ObjectIdentity((1,3,6,1,4,1,5454,1,60,6,6,1))
trapReboot=NotificationType((1,3,6,1,4,1,5454,1,60,6,1))
if mibBuilder.loadTexts:trapReboot.setStatus(_A)
trapStartUp=NotificationType((1,3,6,1,4,1,5454,1,60,6,2))
if mibBuilder.loadTexts:trapStartUp.setStatus(_A)
trapModemLock=NotificationType((1,3,6,1,4,1,5454,1,60,6,3,1))
if mibBuilder.loadTexts:trapModemLock.setStatus(_A)
trapTimingLock=NotificationType((1,3,6,1,4,1,5454,1,60,6,3,2))
if mibBuilder.loadTexts:trapTimingLock.setStatus(_A)
trapInnerCodeLock=NotificationType((1,3,6,1,4,1,5454,1,60,6,3,3))
if mibBuilder.loadTexts:trapInnerCodeLock.setStatus(_A)
trapEqualizerLock=NotificationType((1,3,6,1,4,1,5454,1,60,6,3,4))
if mibBuilder.loadTexts:trapEqualizerLock.setStatus(_A)
trapFrameSyncLock=NotificationType((1,3,6,1,4,1,5454,1,60,6,3,5))
if mibBuilder.loadTexts:trapFrameSyncLock.setStatus(_A)
trapMSEMinThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,1,1))
if mibBuilder.loadTexts:trapMSEMinThreshold.setStatus(_A)
trapMSEMaxThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,1,2))
if mibBuilder.loadTexts:trapMSEMaxThreshold.setStatus(_A)
trapBERMinThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,2,1))
if mibBuilder.loadTexts:trapBERMinThreshold.setStatus(_A)
trapBERMaxThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,2,2))
if mibBuilder.loadTexts:trapBERMaxThreshold.setStatus(_A)
trapFERMinThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,3,1))
if mibBuilder.loadTexts:trapFERMinThreshold.setStatus(_A)
trapFERMaxThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,3,2))
if mibBuilder.loadTexts:trapFERMaxThreshold.setStatus(_A)
trapRSSIMinThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,4,1))
if mibBuilder.loadTexts:trapRSSIMinThreshold.setStatus(_A)
trapRSSIMaxThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,4,2))
if mibBuilder.loadTexts:trapRSSIMaxThreshold.setStatus(_A)
trapIDUTempMinThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,5,1))
if mibBuilder.loadTexts:trapIDUTempMinThreshold.setStatus(_A)
trapIDUTempMaxThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,5,2))
if mibBuilder.loadTexts:trapIDUTempMaxThreshold.setStatus(_A)
trapODUTempMinThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,6,1))
if mibBuilder.loadTexts:trapODUTempMinThreshold.setStatus(_A)
trapODUTempMaxThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,6,2))
if mibBuilder.loadTexts:trapODUTempMaxThreshold.setStatus(_A)
trapInPortUtilMinThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,7,1))
if mibBuilder.loadTexts:trapInPortUtilMinThreshold.setStatus(_A)
trapInPortUtilMaxThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,7,2))
if mibBuilder.loadTexts:trapInPortUtilMaxThreshold.setStatus(_A)
trapOutPortUtilMinThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,8,1))
if mibBuilder.loadTexts:trapOutPortUtilMinThreshold.setStatus(_A)
trapOutPortUtilMaxThreshold=NotificationType((1,3,6,1,4,1,5454,1,60,6,4,8,2))
if mibBuilder.loadTexts:trapOutPortUtilMaxThreshold.setStatus(_A)
trapStandbyLinkDown=NotificationType((1,3,6,1,4,1,5454,1,60,6,5,1))
if mibBuilder.loadTexts:trapStandbyLinkDown.setStatus(_A)
trapStandbyLinkUp=NotificationType((1,3,6,1,4,1,5454,1,60,6,5,2))
if mibBuilder.loadTexts:trapStandbyLinkUp.setStatus(_A)
trapSwitchover=NotificationType((1,3,6,1,4,1,5454,1,60,6,5,3))
if mibBuilder.loadTexts:trapSwitchover.setStatus(_A)
trapEth1StatusUpdate=NotificationType((1,3,6,1,4,1,5454,1,60,6,6,1,1))
if mibBuilder.loadTexts:trapEth1StatusUpdate.setStatus(_A)
trapEth2StatusUpdate=NotificationType((1,3,6,1,4,1,5454,1,60,6,6,1,2))
if mibBuilder.loadTexts:trapEth2StatusUpdate.setStatus(_A)
trapEth3StatusUpdate=NotificationType((1,3,6,1,4,1,5454,1,60,6,6,1,3))
if mibBuilder.loadTexts:trapEth3StatusUpdate.setStatus(_A)
trapEth4StatusUpdate=NotificationType((1,3,6,1,4,1,5454,1,60,6,6,1,4))
if mibBuilder.loadTexts:trapEth4StatusUpdate.setStatus(_A)
trapDownShift=NotificationType((1,3,6,1,4,1,5454,1,60,6,8))
if mibBuilder.loadTexts:trapDownShift.setStatus(_A)
trapRapidPortShutdown=NotificationType((1,3,6,1,4,1,5454,1,60,6,9))
if mibBuilder.loadTexts:trapRapidPortShutdown.setStatus(_A)
trapRPSPortUp=NotificationType((1,3,6,1,4,1,5454,1,60,6,10))
if mibBuilder.loadTexts:trapRPSPortUp.setStatus(_A)
mibBuilder.exportSymbols('TRANGO-APEX-TRAP-MIB',**{_J:DisplayString,'trangotrap':trangotrap,'trapReboot':trapReboot,'trapStartUp':trapStartUp,'traplock':traplock,'trapModemLock':trapModemLock,'trapTimingLock':trapTimingLock,'trapInnerCodeLock':trapInnerCodeLock,'trapEqualizerLock':trapEqualizerLock,'trapFrameSyncLock':trapFrameSyncLock,'trapthreshold':trapthreshold,'trapmse':trapmse,'trapMSEMinThreshold':trapMSEMinThreshold,'trapMSEMaxThreshold':trapMSEMaxThreshold,'trapber':trapber,'trapBERMinThreshold':trapBERMinThreshold,'trapBERMaxThreshold':trapBERMaxThreshold,'trapfer':trapfer,'trapFERMinThreshold':trapFERMinThreshold,'trapFERMaxThreshold':trapFERMaxThreshold,'traprssi':traprssi,'trapRSSIMinThreshold':trapRSSIMinThreshold,'trapRSSIMaxThreshold':trapRSSIMaxThreshold,'trapidutemp':trapidutemp,'trapIDUTempMinThreshold':trapIDUTempMinThreshold,'trapIDUTempMaxThreshold':trapIDUTempMaxThreshold,'trapodutemp':trapodutemp,'trapODUTempMinThreshold':trapODUTempMinThreshold,'trapODUTempMaxThreshold':trapODUTempMaxThreshold,'trapinport':trapinport,'trapInPortUtilMinThreshold':trapInPortUtilMinThreshold,'trapInPortUtilMaxThreshold':trapInPortUtilMaxThreshold,'trapoutport':trapoutport,'trapOutPortUtilMinThreshold':trapOutPortUtilMinThreshold,'trapOutPortUtilMaxThreshold':trapOutPortUtilMaxThreshold,'trapstandby':trapstandby,'trapStandbyLinkDown':trapStandbyLinkDown,'trapStandbyLinkUp':trapStandbyLinkUp,'trapSwitchover':trapSwitchover,'trapeth':trapeth,'trapethstatus':trapethstatus,'trapEth1StatusUpdate':trapEth1StatusUpdate,'trapEth2StatusUpdate':trapEth2StatusUpdate,'trapEth3StatusUpdate':trapEth3StatusUpdate,'trapEth4StatusUpdate':trapEth4StatusUpdate,'trapDownShift':trapDownShift,'trapRapidPortShutdown':trapRapidPortShutdown,'trapRPSPortUp':trapRPSPortUp})